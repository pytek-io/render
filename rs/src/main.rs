use async_channel;
use axum::{
    error_handling::HandleErrorLayer,
    extract::{
        ws::{Message, WebSocket, WebSocketUpgrade},
        Extension, TypedHeader,
    },
    handler::Handler,
    http::{StatusCode, Uri},
    response::{Html, IntoResponse},
    routing::{get, get_service},
    Router,
};
use clap::Parser;
use colored::Colorize;
use futures::stream::{SplitSink, SplitStream};
use futures::{SinkExt, StreamExt};
use normpath::PathExt;
use num_derive::FromPrimitive;
use num_traits::FromPrimitive;
use rmp_serde::encode::to_vec;
use rmp_serde::Deserializer as RmpDeserializer;
use serde::de::DeserializeOwned;
use serde::Serialize;
use std::collections::{BTreeMap, BTreeSet};
use std::error::Error;
use std::fmt;
use std::fs;
use std::io::Cursor;
use std::io::Read;
use std::ops::RangeFrom;
use std::path::PathBuf;
use std::process;
use std::str;
use std::time::{Duration, SystemTime, UNIX_EPOCH};
use std::{borrow::Cow, net::SocketAddr, sync::Arc};
use sys_info;
use tokio::io::{AsyncBufReadExt, AsyncRead, BufReader};
use tokio::sync::{mpsc, RwLock};
use tokio::{process::Command as TokioCommand, sync::oneshot};
use tokio::{signal, time::sleep};
use tower::{BoxError, ServiceBuilder};
use tower_http::trace::TraceLayer;
use tower_http::{add_extension::AddExtensionLayer, services::ServeDir};

#[macro_use]
extern crate simple_error;
extern crate env_logger;
#[macro_use]
extern crate log;

#[derive(Debug)]
struct RenderError {
    details: String,
}

impl RenderError {
    fn new(msg: &str) -> RenderError {
        RenderError {
            details: msg.to_string(),
        }
    }
}

impl fmt::Display for RenderError {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(f, "{}", self.details)
    }
}

impl Error for RenderError {
    fn description(&self) -> &str {
        &self.details
    }
}

const NOT_A_SESSION_ID: usize = 0;
const KERNEL_MESSAGE_TYPE: usize = 1;
const CLIENT_MESSAGE_PREFIX: usize = 0;
const KERNEL_TIMEOUT: Duration = Duration::from_secs(1);
// giving time to a kernel to print anything before killing it
const KERNEL_GRACE_PERIOD: Duration = Duration::from_secs(1);
const MAX_KERNELS_UPDATE_LAG: usize = 100;

type SessionMessageDataType = u32;
type KernelIdType = u32;
type SessionIdType = usize;
type ProcessIdType = u32;
type EpochTimeType = u64;

#[derive(FromPrimitive)]
enum SessionMessageType {
    MessageToClient = 1,
    SessionEnd = 2,
    SubscribeToKernelUpdates = 3,
}

enum MessageToKernel {
    MessageFromClientToKernel(Message),
    NewSession((SessionIdType, String, mpsc::UnboundedSender<Message>)),
    LostConnectionToClient(SessionIdType),
}

type AxumRawMessage = std::option::Option<std::result::Result<Message, axum::Error>>;
type Result<T> = std::result::Result<T, Box<dyn Error>>;
type ServerPtr = Arc<Server>;

static PRINT_PYTHON_LOCATION: &str = "import sys; print(sys.executable)";
static PRINT_PYTHON_VERSION: &str = "import platform; print(platform.python_version())";
static PRINT_REFLECT_PATH: &str = "import render, os; print(os.path.dirname(render.__file__))";
static PRINT_REFLECT_VERSION: &str = "import render; print(render.__version__)";

static START_SCRIPT_PATH: &str = "src=\"";
static END_SCRIPT_PATH: &str = "></script>";

#[derive(Parser)]
struct Options {
    #[clap(long, default_value = "8080")]
    port: u16,
    #[clap(long, default_value = "render.dashboard")]
    default_app: String,
    #[clap(long)]
    dev: bool,
    #[clap(long, default_value = ".")]
    app_folder: String,
    #[clap(long, default_value = "1")]
    max_sessions: usize,
}

type KernelPtr = Arc<Kernel>;
type KernelRegistry = BTreeMap<KernelIdType, KernelPtr>;
type PendingKernelRegistry = BTreeMap<ProcessIdType, oneshot::Receiver<tokio::process::Child>>;

fn read_data_mp<T>(reader: &mut dyn Read, description: &str) -> Result<T>
where
    T: DeserializeOwned,
{
    T::deserialize(&mut RmpDeserializer::new(reader))
        .map_err(|error| format!("Failed to deserialize {}: {}.", description, error).into())
}

fn serialize<S>(arg: &S) -> Vec<u8>
where
    S: Serialize,
{
    to_vec(&arg).unwrap()
}

fn coerce_to_binary(message: AxumRawMessage) -> Result<Vec<u8>> {
    match message.unwrap().unwrap() {
        Message::Binary(m) => Ok(m),
        _ => Err(Box::new(RenderError::new("Unexpected message format"))),
    }
}

fn send_message_to_kernel_process(
    sink: &mpsc::UnboundedSender<MessageToKernel>,
    code: &str,
    message: &[u8],
) -> Result<()> {
    sink.send(MessageToKernel::MessageFromClientToKernel(Message::Binary(
        [
            serialize(&KERNEL_MESSAGE_TYPE).as_slice(),
            serialize(&code).as_slice(),
            message,
        ]
        .concat(),
    )))
    .map_err(|e| format!("Failed to send message to kernel process. {e}"))?;
    Ok(())
}

struct Kernel {
    pid: ProcessIdType,
    start_time: EpochTimeType,
    sink: mpsc::UnboundedSender<MessageToKernel>,
    server_stream: RwLock<Option<mpsc::UnboundedReceiver<MessageToKernel>>>,
    session_descriptions: RwLock<BTreeMap<usize, String>>,
    nb_pending_sessions: RwLock<usize>,
    alive: RwLock<bool>,
}

impl Kernel {
    fn new(pid: ProcessIdType) -> Self {
        let (sink, stream) = mpsc::unbounded_channel();
        Self {
            pid,
            start_time: SystemTime::now()
                .duration_since(UNIX_EPOCH)
                .expect("Failed to compute Epoch time")
                .as_secs(),
            sink,
            server_stream: RwLock::new(Some(stream)),
            session_descriptions: RwLock::new(BTreeMap::new()),
            nb_pending_sessions: RwLock::new(1),
            alive: RwLock::new(true),
        }
    }
}

enum KernelUpdate {
    NewKernel((KernelIdType, KernelPtr)),
    KernelEnded(KernelIdType),
}

struct Server {
    session_counter: RwLock<RangeFrom<SessionIdType>>,
    kernel_counter: RwLock<RangeFrom<KernelIdType>>,
    arguments: Options,
    pending_kernels: RwLock<PendingKernelRegistry>,
    kernels: RwLock<KernelRegistry>,
    render_folder: PathBuf,
    app_folder: String,
    max_sessions: usize,
    html: String,
    new_kernel_sender: async_channel::Sender<(KernelIdType, KernelPtr)>,
    new_kernel_receiver: async_channel::Receiver<(KernelIdType, KernelPtr)>,
    kernel_updates_sender: mpsc::Sender<KernelUpdate>,
    subscribed_kernels: RwLock<BTreeSet<KernelIdType>>,
    port: String,
}

impl Server {
    async fn wait_for_available_kernel(&self) -> Result<(KernelIdType, KernelPtr)> {
        for (kernel_id, kernel) in self.kernels.read().await.iter() {
            // session_descriptions_read prevents a race condition don't remove it
            let session_descriptions_read = kernel.session_descriptions.read().await;
            if *kernel.alive.read().await
                && session_descriptions_read.len() < self.max_sessions
                && *kernel.nb_pending_sessions.read().await == 0
            {
                info!("Reusing existing kernel {kernel_id}.");
                *kernel.nb_pending_sessions.write().await += 1;
                return Ok((*kernel_id, kernel.clone()));
            }
        }
        if self.arguments.dev {
            println!("Waiting for kernel to connect.");
        } else {
            self.spawn_kernel().await?;
        }
        Ok(self.new_kernel_receiver.recv().await?)
    }

    async fn send_kernel_update(&self, code: &str, message: &[u8]) {
        let message = [serialize(&code).as_slice(), message].concat();
        for kernel_id in self.subscribed_kernels.read().await.iter() {
            if let Some(kernel) = self.kernels.read().await.get(kernel_id) {
                if *kernel.alive.read().await {
                    if let Err(e) =
                        send_message_to_kernel_process(&kernel.sink, "kernel update", &message)
                    {
                        warn!("Failed to send '{code}' kernel update to kernel. {e}.");
                    }
                }
            }
        }
    }

    async fn manage_client_connection(
        &self,
        kernel_to_client_sink: mpsc::UnboundedSender<MessageToKernel>,
        mut kernel_to_client_stream: mpsc::UnboundedReceiver<Message>,
        connection_to_client_sink: &mut SplitSink<WebSocket, Message>,
        mut connection_to_client_stream: SplitStream<WebSocket>,
    ) -> std::result::Result<(String, bool), String> {
        Ok(loop {
            tokio::select! {
                message = kernel_to_client_stream.recv() => {
                    match message {
                        Some(m) => if let Err(e) = connection_to_client_sink.send(m).await {
                            break (format!("Failed to send message to client. {e}"), false);
                        },
                        None => {
                            break (format!("Kernel stream has been closed."), true);
                        }
                    }
                },
                message = connection_to_client_stream.next() => {
                   if let Some(message) = message {
                            match message {
                                Ok(message) => {
                                    match message {
                                        Message::Binary(_) => {
                                            kernel_to_client_sink.send(MessageToKernel::MessageFromClientToKernel(message)).map_err(
                                                |e| format!("Failed to forward message to session. {e}"))?;
                                        }
                                        Message::Close(_) => {
                                            break (format!("Received close message from client connection."), false);
                                        }
                                        _ => {}
                                    }
                                },
                                Err(e) => {
                                    break (format!("Session received error from client connection. {e}"), false);
                                }
                            }
                    } else {
                        break (format!("Session received None from client connection."), false);
                    }
                },
            }
        })
    }

    async fn register_kernel(&self, kernel_id: KernelIdType, kernel: KernelPtr) -> KernelIdType {
        self.kernels.write().await.insert(kernel_id, kernel.clone());
        self.send_kernel_update(
            "new kernel",
            &serialize(&(kernel_id, kernel.pid, kernel.start_time)),
        )
        .await;
        if let Err(e) = self.new_kernel_sender.send((kernel_id, kernel)).await {
            error!("Failed to send new kernel {kernel_id}. {e}");
        }
        self.publish_kernel_update().await;
        kernel_id
    }

    async fn unregister_kernel(&self, kernel_id: KernelIdType) {
        self.kernels.write().await.remove(&kernel_id);
        self.send_kernel_update("kernel ended", &serialize(&kernel_id))
            .await;
    }

    async fn publish_kernel_update(&self) {
        let mut message = Vec::new();
        let kernels_read = self.kernels.read().await;
        for (kernel_id, kernel) in kernels_read.iter() {
            message.push((
                kernel_id,
                (
                    kernel.pid,
                    kernel.start_time,
                    kernel.session_descriptions.read().await.clone(),
                ),
            ));
        }
        self.send_kernel_update("kernels", &serialize(&message))
            .await;
    }

    async fn manage_kernel_impl(
        &self,
        kernel_id: KernelIdType,
        kernel: KernelPtr,
        mut kernel_sink: SplitSink<WebSocket, Message>,
        mut kernel_stream: SplitStream<WebSocket>,
    ) -> Result<()> {
        let mut connections_to_client: BTreeMap<usize, mpsc::UnboundedSender<Message>> =
            BTreeMap::new();
        let mut server_stream = kernel.server_stream.write().await.take().unwrap();
        send_message_to_kernel_process(
            &kernel.sink,
            "kernel settings",
            &serialize(&(&self.app_folder, kernel_id, self.arguments.dev)),
        )?;
        loop {
            tokio::select! {
                message = server_stream.recv() => {
                    if let Some(message) = message {
                        match message {
                            MessageToKernel::MessageFromClientToKernel(message) => {
                                if let Err(e) = kernel_sink.send(message).await {
                                    error!("Failed to forward message to kernel {kernel_id}. {e}");
                                    break;
                                }
                            },
                            MessageToKernel::NewSession((session_id, uri, kernel_to_client_sink)) => {
                                connections_to_client.insert(session_id, kernel_to_client_sink);
                                kernel.session_descriptions.write().await.insert(session_id, uri);
                                *kernel.nb_pending_sessions.write().await -= 1;
                            },
                            MessageToKernel::LostConnectionToClient(session_id) => {
                                connections_to_client.remove(&session_id);
                                let mut kernel_session_descriptions_write = kernel.session_descriptions.write().await;
                                kernel_session_descriptions_write.remove(&session_id);
                                if self.arguments.dev {
                                    continue;
                                }
                                if kernel_session_descriptions_write.is_empty() && *kernel.nb_pending_sessions.read().await == 0 {
                                    info!("Session {session_id} lost connection to client. Kernel {kernel_id} has no more sessions, terminating it.", kernel_id = kernel_id);
                                    *kernel.alive.write().await = false;
                                    break;
                                }
                              }
                        }
                    }
                },
                message = kernel_stream.next() => {
                    let maybe_message = match message {
                        Some(content) => content,
                        None => {
                            warn!("Connection to kernel received empty message, closing connection.");
                            break;
                        }
                    };
                    let message = match maybe_message {
                        Ok(content) => content,
                        Err(e) => {
                            warn!("Connection to kernel failed. {e}.");
                            break;
                        } // we receive an error when a kernel dies
                    };
                    match message {
                        Message::Binary(ref message_as_binary) => {
                            let mut cursor = Cursor::new(&message_as_binary);
                            let session_message_type: SessionMessageType = FromPrimitive::from_u32(
                                read_data_mp::<SessionMessageDataType>(&mut cursor, "message type")
                                    .expect("webserver received invalid message from kernel"),
                            )
                            .expect("Failed to decode session_message_type value.");
                            match session_message_type {
                                SessionMessageType::MessageToClient => {
                                    let session_id = read_data_mp(&mut cursor, "session id")
                                    .expect("webserver received invalid message from kernel");
                                        if let Some(connection_to_session) = connections_to_client.get_mut(&session_id) {
                                        if let Err(e) = connection_to_session.send(message) {
                                            error!("Failed to forward message to session {session_id}, {e}")
                                        }
                                    } else {
                                        error!("Kernel sent a message to session {session_id} that is no longer registered.");
                                    }
                                }
                                SessionMessageType::SessionEnd => {
                                    let session_id = read_data_mp(&mut cursor, "session id")
                                    .expect("webserver received invalid message from kernel");
                                        // session_descriptions_write prevents a race condition don't remove it
                                    let mut session_descriptions_write = kernel.session_descriptions.write().await;
                                    session_descriptions_write.remove(&session_id);
                                    connections_to_client.remove(&session_id);
                                    if session_descriptions_write.is_empty() && *kernel.nb_pending_sessions.read().await == 0 {
                                        info!("Kernel {kernel_id} has no more sessions, terminating it.", kernel_id = kernel_id);
                                        *kernel.alive.write().await = false;
                                        break;
                                    }
                                }
                                SessionMessageType::SubscribeToKernelUpdates => {
                                    info!("Kernel {kernel_id} subscribed to kernel updates.");
                                    self.subscribed_kernels.write().await.insert(kernel_id);
                                    self.publish_kernel_update().await;
                                }
                            };
                        }
                        Message::Close(_) => {
                            error!("Kernel send a connection close message.");
                            break;
                        }
                        _ => {}
                    }
                }
            }
        }
        self.subscribed_kernels.write().await.remove(&kernel_id);
        Ok(())
    }

    async fn spawn_kernel(&self) -> Result<()> {
        let mut kernel_process = TokioCommand::new("python")
            .args(vec!["-u", "-m", "render.kernel", "--port", &self.port])
            .kill_on_drop(true)
            .current_dir(self.arguments.app_folder.clone())
            .stdout(process::Stdio::piped())
            .stderr(process::Stdio::piped())
            .spawn()
            .map_err(|e| format!("Failed to launch kernel. {}.", e))
            .map_err(|e| format!("Failed to spawn python kernel {e}", e = e))?;
        let pid = kernel_process.id().unwrap();
        info!("Kernel process, pid {pid}, spawned.");
        let stdout = kernel_process.stdout.take().unwrap();
        tokio::spawn(async move { print_child_process_stream(stdout).await });
        let stderr = kernel_process.stderr.take().unwrap();
        tokio::spawn(async move { print_child_process_stream(stderr).await });
        let (kernel_process_sender, kernel_process_receiver) = oneshot::channel();
        self.pending_kernels
            .write()
            .await
            .insert(pid, kernel_process_receiver);
        kernel_process_sender
            .send(kernel_process)
            .expect("Failed to send kernel process.");
        sleep(KERNEL_TIMEOUT).await;
        if self.pending_kernels.write().await.remove(&pid).is_some() {
            return Err(format!("Kernel failed to connect after {:?}.", KERNEL_TIMEOUT).into());
        }
        Ok(())
    }

    async fn manage_client_connection_impl(&self, connection: WebSocket) -> Result<SessionIdType> {
        let (mut client_sink, mut client_stream) = connection.split();
        let mut message = Cursor::new(coerce_to_binary(client_stream.next().await)?);
        assert!(read_data_mp::<usize>(&mut message, "client type id")? == CLIENT_MESSAGE_PREFIX);
        let _uninitialized_session_id = read_data_mp::<SessionIdType>(&mut message, "session id")?;
        let (
            uri,
            browser,
            width,
            height,
            previous_kernel_id,
            previous_start_time,
            previous_session_id,
        ) = read_data_mp::<(String, String, u64, u64, KernelIdType, u64, SessionIdType)>(
            &mut message,
            "session parameters",
        )?;
        info!("New connection for uri {uri} from {browser}, previous kernel {previous_kernel_id}, previous session {previous_session_id}.");
        let uri = if uri.is_empty() {
            self.arguments.default_app.clone()
        } else {
            uri
        };
        let (session_sink, session_stream) = mpsc::unbounded_channel();
        let mut current_kernel = None;
        if let Some(existing_kernel) = self
            .kernels
            .read()
            .await
            .get(&previous_kernel_id)
            .map(|k| k.clone())
        {
            if existing_kernel.start_time == previous_start_time
                && existing_kernel
                    .session_descriptions
                    .read()
                    .await
                    .contains_key(&previous_session_id)
            {
                info!(
                    "Reusing existing kernel {previous_kernel_id} for session {previous_session_id}."
                );
                current_kernel = Some(existing_kernel);
            }
        };
        let (kernel_id, session_id, kernel_ptr) = if let Some(kernel_ptr) = current_kernel.take() {
            (previous_kernel_id, previous_session_id, kernel_ptr)
        } else {
            let (kernel_id, kernel) = self.wait_for_available_kernel().await?;
            let session_id = self
                .session_counter
                .write()
                .await
                .next()
                .expect("Internal error, failed to generate session id");
            send_message_to_kernel_process(
                &kernel.sink,
                "start session",
                serialize(&(session_id, &uri, &browser, kernel.start_time, width, height))
                    .as_slice(),
            )
            .expect("Failed to send start session to kernel process.");
            self.send_kernel_update(
                "assigned session",
                &serialize(&(kernel_id, session_id, &uri)),
            )
            .await;
            (kernel_id, session_id, kernel)
        };
        info!("Starting session {session_id} on kernel {kernel_id}.");
        kernel_ptr
            .sink
            .send(MessageToKernel::NewSession((
                session_id,
                uri.clone(),
                session_sink,
            )))
            .expect("Failed to send new session to kernel.");
        let connection_outcome = self
            .manage_client_connection(
                kernel_ptr.sink.clone(),
                session_stream,
                &mut client_sink,
                client_stream,
            )
            .await;
        kernel_ptr
            .sink
            .send(MessageToKernel::LostConnectionToClient(session_id))
            .expect("Failed to send new session to kernel.");
        match connection_outcome {
            Err(message) => {
                error!("Session {session_id} ended. {message}");
                client_sink
                    .send(Message::Binary(
                        [
                            serialize(&0).as_slice(),
                            serialize(&0).as_slice(),
                            serialize(&(0, ("session end", &message.to_string()))).as_slice(),
                        ]
                        .concat(),
                    ))
                    .await?;
            }
            Ok((message, connection_closed_explicitely)) => {
                info!("Session {session_id} ended. {message}");
                if connection_closed_explicitely {
                    if let Err(e) = send_message_to_kernel_process(
                        &kernel_ptr.sink,
                        "terminate session",
                        serialize(&session_id).as_slice(),
                    ) {
                        error!(
                            "Failed to send terminate session {} to kernel process. {e}",
                            session_id
                        );
                    } else {
                        info!("Terminated session {}.", session_id);
                    }
                }
            }
        }
        Ok(session_id)
    }

    async fn manage_kernel_connection_impl(&self, socket: WebSocket) -> Result<()> {
        let (kernel_sink, mut kernel_stream) = socket.split();
        let pid = read_data_mp(
            &mut Cursor::new(&coerce_to_binary(kernel_stream.next().await).unwrap()),
            "process id",
        )?;
        // will kill the child process on connection termination if we spawned it.
        let _maybe_process =
            if let Some(maybe_process_receiver) = self.pending_kernels.write().await.remove(&pid) {
                Some(
                    maybe_process_receiver
                        .await
                        .expect("Failed to receive kernel process."),
                )
            } else {
                None
            };
        let kernel = Arc::new(Kernel::new(pid));
        let kernel_id = self
            .kernel_counter
            .write()
            .await
            .next()
            .expect("Failed to generate kernel id.");
        info!("Kernel process, pid {pid}, connected to server, will be kernel {kernel_id}.");
        let _kernel_life_manager = KernelLifeManager::new(
            self.kernel_updates_sender.clone(),
            kernel_id,
            kernel.clone(),
        );
        self.manage_kernel_impl(kernel_id, kernel, kernel_sink, kernel_stream)
            .await?;
        info!(
            "Connection to kernel {kernel_id} ended, will be killed in {:?}",
            KERNEL_GRACE_PERIOD
        );
        sleep(KERNEL_GRACE_PERIOD).await;
        Ok(())
    }

    async fn manage_kernel_updates(
        &self,
        mut kernel_updates_receiver: mpsc::Receiver<KernelUpdate>,
    ) {
        while let Some(message) = kernel_updates_receiver.recv().await {
            match message {
                KernelUpdate::NewKernel((kernel_id, kernel_ptr)) => {
                    self.register_kernel(kernel_id, kernel_ptr).await;
                }
                KernelUpdate::KernelEnded(kernel_id) => {
                    self.unregister_kernel(kernel_id).await;
                }
            }
        }
    }
}
struct KernelLifeManager {
    kernel_id: KernelIdType,
    kernel_updates_sender: mpsc::Sender<KernelUpdate>,
}

impl KernelLifeManager {
    fn new(
        kernel_updates_sender: mpsc::Sender<KernelUpdate>,
        kernel_id: KernelIdType,
        kernel: KernelPtr,
    ) -> Self {
        kernel_updates_sender
            .try_send(KernelUpdate::NewKernel((kernel_id, kernel)))
            .expect("Failed to send new kernel signal.");
        Self {
            kernel_id,
            kernel_updates_sender,
        }
    }
}

impl Drop for KernelLifeManager {
    fn drop(&mut self) {
        if let Err(e) = self
            .kernel_updates_sender
            .try_send(KernelUpdate::KernelEnded(self.kernel_id))
        {
            error!("Failed to send kernel ended signal. {e}");
        }
    }
}

async fn manage_client_connection(server: ServerPtr, connection: WebSocket) {
    if let Err(e) = server.manage_client_connection_impl(connection).await {
        error!("Connection to client failed. {e}");
    }
}

async fn invoke_python_command(command: &str) -> Result<String> {
    let output = match TokioCommand::new("python")
        .args(&["-c", command])
        .output()
        .await
    {
        Ok(message) => message,
        Err(e) => {
            if let Some(code) = e.raw_os_error() {
                if code == 2 {
                    return Err(Box::new(RenderError::new(&format!("Failed to invoke Python intepreter. {}. Make sure your Python environment in correctly setup before launching Render.", e.to_string()))));
                }
            }
            return Err(Box::new(RenderError::new(&format!(
                "Failed to invoke Python command {}. {}",
                command,
                e.to_string()
            ))));
        }
    };
    if output.status.success() {
        let mut result = str::from_utf8(&output.stdout)
            .map_err(|x| format!("Python command {} failed. {}", command, x.to_string()))?
            .to_string();
        result.retain(|c| c != '\n' && c != '\r');
        Ok(result)
    } else {
        bail!(str::from_utf8(&output.stderr)?)
    }
}

async fn print_child_process_stream<T>(reader: T)
where
    T: AsyncRead + Unpin,
{
    let mut buffer = BufReader::new(reader).lines();
    while let Ok(line) = buffer.next_line().await {
        if let Some(line) = line {
            println!("{}", line);
        } else {
            break;
        }
    }
}

async fn manage_http_request(
    _user_agent: Option<TypedHeader<headers::UserAgent>>,
    uri: Uri,
    Extension(server): Extension<ServerPtr>,
) -> Html<String> {
    info!("Serving html page at {uri}.");
    Html(server.html.clone())
}

async fn handle_error(error: BoxError) -> impl IntoResponse {
    if error.is::<tower::timeout::error::Elapsed>() {
        return (StatusCode::REQUEST_TIMEOUT, Cow::from("request timed out"));
    }

    if error.is::<tower::load_shed::error::Overloaded>() {
        return (
            StatusCode::SERVICE_UNAVAILABLE,
            Cow::from("service is overloaded, try again later"),
        );
    }
    (
        StatusCode::INTERNAL_SERVER_ERROR,
        Cow::from(format!("Unhandled internal error: {}", error)),
    )
}

async fn manage_connection_to_kernel(server: ServerPtr, socket: WebSocket) {
    if let Err(e) = server.manage_kernel_connection_impl(socket).await {
        error!("Connection to kernel failed. {e}")
    }
}

async fn accept_kernel_connection(
    ws: WebSocketUpgrade,
    Extension(server): Extension<ServerPtr>,
) -> impl IntoResponse {
    ws.on_upgrade(|socket: WebSocket| manage_connection_to_kernel(server, socket))
}

async fn accept_client_connection(
    ws: WebSocketUpgrade,
    _user_agent: Option<TypedHeader<headers::UserAgent>>,
    Extension(server): Extension<ServerPtr>,
) -> impl IntoResponse {
    ws.on_upgrade(|socket: WebSocket| manage_client_connection(server, socket))
}

async fn handler_404() -> impl IntoResponse {
    (StatusCode::NOT_FOUND, "Invalid app request.")
}

async fn websocket_server(server: ServerPtr) -> Result<()> {
    let external_routes = Router::new()
        .nest(
            "/js",
            get_service(ServeDir::new(server.render_folder.join("js"))).handle_error(
                |error: std::io::Error| async move {
                    (
                        StatusCode::INTERNAL_SERVER_ERROR,
                        format!("Unhandled internal error: {}", error),
                    )
                },
            ),
        )
        .nest(
            "/static",
            get_service(ServeDir::new(server.render_folder.join("static"))).handle_error(
                |error: std::io::Error| async move {
                    (
                        StatusCode::INTERNAL_SERVER_ERROR,
                        format!("Unhandled internal error: {}", error),
                    )
                },
            ),
        )
        .nest(
            "/data",
            get_service(ServeDir::new(&server.app_folder)).handle_error(
                |error: std::io::Error| async move {
                    (
                        StatusCode::INTERNAL_SERVER_ERROR,
                        format!("Unhandled internal error: {}", error),
                    )
                },
            ),
        )
        .nest("/app", get(manage_http_request))
        .route("/", get(manage_http_request))
        .route("/ws", get(accept_client_connection))
        .route("/ws_kernels", get(accept_kernel_connection))
        .fallback(handler_404.into_service())
        .layer(
            ServiceBuilder::new()
                // Handle errors from middleware
                .layer(HandleErrorLayer::new(handle_error))
                .load_shed()
                .concurrency_limit(1024)
                .timeout(Duration::from_secs(10))
                .layer(TraceLayer::new_for_http())
                .layer(AddExtensionLayer::new(server.clone()))
                .into_inner(),
        );
    axum::Server::bind(&SocketAddr::from(([0, 0, 0, 0], server.arguments.port)))
        .serve(external_routes.into_make_service())
        .await
        .map_err(|e| format!("Failed to start web server. {e}").into())
}

async fn launch_default_app(port: u16) {
    sleep(Duration::from_secs(1)).await;
    if let Err(e) = invoke_python_command(&format!(
        "import webbrowser; webbrowser.open('http://localhost:{}')",
        port
    ))
    .await
    {
        warn!("Failed to launch default app: {e}");
    }
}

async fn main_aync_impl(_terminate: tokio::sync::mpsc::Sender<i32>) -> Result<()> {
    if let Err(_) = enable_ansi_support::enable_ansi_support() {
        println!("{}", "Unable to activate ansi color support. Display will most likely contain ansi color in Power Shell.".to_string().red())
    }
    let render_folder = invoke_python_command(PRINT_REFLECT_PATH).await?;
    let client_version = invoke_python_command(PRINT_REFLECT_VERSION).await?;
    println!(
        "{}: {} {}",
        "OS".green(),
        &sys_info::os_type()?,
        sys_info::os_release()?
    );
    println!("{}: {}", "Render".green(), &client_version);
    println!(
        "{}: {}",
        "Python version".green(),
        invoke_python_command(PRINT_PYTHON_VERSION).await?,
    );
    println!(
        "{}: {}",
        "Python location".green(),
        invoke_python_command(PRINT_PYTHON_LOCATION).await?
    );
    let server_version = option_env!("CARGO_PKG_VERSION").unwrap_or("NOT_FOUND");
    if client_version != server_version {
        panic!(
            "Render client and server versions are not matching: {} != {}",
            client_version, server_version
        );
    }
    let render_folder = PathBuf::from(&render_folder);
    let opts: Options = Options::parse();
    let app_folder = PathBuf::from(&opts.app_folder)
        .normalize()
        .expect(format!("invalid app folder {}", opts.app_folder).as_str())
        .into_path_buf();
    let python_path = invoke_python_command(&format!(
        "import os; print(os.environ.get('PYTHONPATH', ''))"
    ))
    .await?;
    println!("{}: {}", "PYTHONPATH".green(), python_path);
    println!(
        "{}: {}",
        "Apps folder".green(),
        app_folder.to_str().unwrap().blue()
    );
    println!("{}: {}", "Default app".green(), opts.default_app);
    println!(
        "Serving apps locally at: {}",
        format!("http://localhost:{}", opts.port).blue()
    );

    let content = fs::read_to_string(
        &render_folder
            .join("index.html")
            .to_str()
            .expect("Should have been able to append path"),
    )
    .expect("Failed to read index.html");
    let start = content
        .find(START_SCRIPT_PATH)
        .expect(&format!("Failed to find {START_SCRIPT_PATH} in {content}"));
    let end = content
        .find(END_SCRIPT_PATH)
        .expect(&format!("Failed to find {END_SCRIPT_PATH} in {content}"));
    let script_path = &content[start + START_SCRIPT_PATH.len()..end];
    let html = format!(
        r#"<!DOCTYPE html>
    <html>
      <head>
        <title>Render app</title>
        <meta charset="UTF-8">
        <meta content="width=device-width, initial-scale=1.0, maximum-scale=1" name="viewport">
        <meta content="Render web app" name="description">
        <meta content="no-cache, no-store, must-revalidate" http-equiv="Cache-Control">
        <meta content="no-cache" http-equiv="Pragma">
        <meta content="0" http-equiv="Expires">
        <link href="/static/cogs.svg" rel="icon" type="image/x-icon">
        <script defer="" src="{script_path}"></script>
      </head>
      <body style="height: 100%; background-color: rgb(15, 23, 36)">
        <div id="root" style="height: 100%">
          <div style="height: 100%; display: flex; justify-content: center;align-items: center;">
            <img alt="Loading data" src="/static/three_cogs_colors_vs.svg" width="40%">
          </div>
        </div>
        <style>
    html {{
      height: 100%;
    }},
    </style>
      </body>
    </html>"#
    );
    let max_sessions = if opts.dev { 1000 } else { opts.max_sessions };
    let port_as_str = opts.port.to_string();
    let port = opts.port;
    let (kernel_updates_sender, kernel_updates_receiver) = mpsc::channel(MAX_KERNELS_UPDATE_LAG);
    let (new_kernel_sender, new_kernel_receiver) = async_channel::unbounded();
    let server = Arc::new(Server {
        kernel_counter: RwLock::new(1..),
        arguments: opts,
        pending_kernels: RwLock::new(PendingKernelRegistry::new()),
        kernels: RwLock::new(KernelRegistry::new()),
        subscribed_kernels: RwLock::new(BTreeSet::new()),
        session_counter: RwLock::new((NOT_A_SESSION_ID + 1)..),
        render_folder: render_folder.clone(),
        app_folder: app_folder.to_str().unwrap().to_string(),
        max_sessions,
        html,
        new_kernel_sender,
        new_kernel_receiver,
        port: port_as_str,
        kernel_updates_sender,
    });
    let server_clone = server.clone();
    tokio::spawn(async move {
        launch_default_app(port).await;
    });
    tokio::spawn(async move {
        server_clone
            .manage_kernel_updates(kernel_updates_receiver)
            .await;
    });
    websocket_server(server).await?;
    Ok(())
}

async fn main_aync(terminate: tokio::sync::mpsc::Sender<i32>) {
    if let Err(e) = main_aync_impl(terminate).await {
        error!(
            "Main thread failed, terminating application. {}",
            e.to_string()
        );
    } else {
        error!("Render terminated");
    }
}

fn main() {
    env_logger::builder().format_timestamp_millis().init();
    let runtime = tokio::runtime::Builder::new_multi_thread()
        .enable_all()
        .build()
        .unwrap();
    let (termination_sender, mut termination_receiver) = mpsc::channel(1);
    let termination_sender_clone = termination_sender.clone();
    runtime.spawn(async move {
        signal::ctrl_c().await.expect("failed to listen for event");
        termination_sender_clone.send(0).await.unwrap();
    });
    let termination_sender_clone = termination_sender.clone();
    runtime.spawn(async move {
        main_aync(termination_sender_clone).await;
        termination_sender.send(0).await.unwrap();
    });
    runtime.handle().clone().block_on(async move {
        termination_receiver.recv().await;
        info!("shutting down render");
        runtime.shutdown_background();
    });
    std::process::exit(1);
}
