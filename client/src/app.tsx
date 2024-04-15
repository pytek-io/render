import React, { Suspense } from "react";
import ReactDOM from "react-dom";
import { createRoot } from "react-dom/client";
import "regenerator-runtime/runtime.js";
import WeakValueMap from "./weakvaluemap";

const R = require("ramda");
const autoBind = require("auto-bind");

import { decodeMulti, encode } from "@msgpack/msgpack";

window.React = React;

// this is to fix modules that are meant to run in node and the browser (eg: spectacle)
window.process = {
  env: {
    NODE_ENV: "development",
  },
};

window.reflect = {};
const component_records = new Map();
const dom_object_or_refs = new WeakValueMap();
const pending_calls = new WeakValueMap();
window.reflect.component_records = component_records;
window.reflect.dom_object_or_refs = dom_object_or_refs;

let current_promise_id = 1; // starting from 1 to make it nullable
const pending_promises = new Map();
const variables = new Map();

export function registerMethod(name: string, method: string) {
  if (window.methodRegister == undefined) {
    window.methodRegister = new Map();
  }
  window.methodRegister.set(name, method);
}

function add_links(links: [string, string][][]) {
  for (const link of links) {
    const element = document.createElement("link");
    for (const [name, value] of link) {
      if (value != null) {
        element.setAttribute(name, value);
      }
    }
    document.getElementsByTagName("head")[0].appendChild(element);
  }
}

// function resolveMethod(name: string) {
//   const [method, ...qualifiers] = name.split(".");
//   let result = window.methodRegister.get(method);
//   if (result == undefined) {
//     throw new Error(`failed to resolve "${name}" callback`);
//   }
//   for (const qualifier of qualifiers) {
//     result = result[qualifier];
//     if (result == undefined) {
//       throw new Error(`failed to resolve "${qualifier}" in ${name}`);
//     }
//   }
//   return result;
// }

function resolveMethod(name: string) {
  const result = window.methodRegister.get(name);
  if (result == undefined) {
    throw new Error(`failed to resolve "${name}" callback`);
  }
  return result;
}

export function fetch_attribute(attribute_path: string) {
  const attributes = attribute_path ? attribute_path.split(".") : [];
  return (object: any) => {
    let result = object;
    for (const attribute of attributes) {
      result = result[attribute];
      if (result === undefined) {
        console.error(`Invalid attribute path ${attribute_path}`, object);
      }
    }
    return result;
  };
}
function new_fetch_attribute(attributes: string[]) {
  return (object: any) => {
    let result = object;
    for (let i = 0; i < attributes.length; i++) {
      // some components (eg: ant.Autocomplete) return undefined when their value is undefined 
      if (result === undefined) {
        return result;
      }
      const attribute = attributes[i];
      if (attribute == "[]") {
        if (result.constructor.name == "Array") {
          return result.map(new_fetch_attribute(attributes.slice(i + 1, attributes.length)))
        }
        return [`Unexpected ${result} at ${attributes}`]
      }
      if (attribute.constructor.name == "String" && attribute.substring(attribute.length - 2, attribute.length) == "()") {
        result = result[attribute.substring(0, attribute.length - 2)]()
      } else {
        result = result[attribute];
      }
    }
    return result;
  };
}


function new_fetch_attributes(attribute_paths) {
  return (values) => {
    const result = [];
    for (const attribute_path of attribute_paths) {
      result.push(new_fetch_attribute(attribute_path)(values));
    }
    return result;
  };
}


function isTouchDevice() {
  return (
    "ontouchstart" in window ||
    navigator.maxTouchPoints > 0 ||
    navigator.msMaxTouchPoints > 0
  );
}

function getOS() {
  var userAgent = window.navigator.userAgent,
    platform =
      window.navigator?.userAgentData?.platform ?? window.navigator.platform,
    macosPlatforms = ["Macintosh", "MacIntel", "MacPPC", "Mac68K", "macOS"],
    windowsPlatforms = ["Win32", "Win64", "Windows", "WinCE"],
    iosPlatforms = ["iPhone", "iPad", "iPod"],
    os = null;
  if (macosPlatforms.indexOf(platform) !== -1) {
    os = "MacOS";
  } else if (iosPlatforms.indexOf(platform) !== -1) {
    os = "iOS";
  } else if (windowsPlatforms.indexOf(platform) !== -1) {
    os = "Windows";
  } else if (/Android/.test(userAgent)) {
    os = "Android";
  } else if (!os && /Linux/.test(platform)) {
    os = "Linux";
  }
  return os;
}

function wrap_inside_suspense(lazy_component) {
  return ({ children, ...props }) => {
    return React.createElement(Suspense, {}, React.createElement(lazy_component, props,
      ...(children
        ? children.constructor.name == "Array"
          ? children
          : [children]
        : [])
    ));
  }
}

export function registerComponent(name, sub_class, constructor, namespace, lazy = false) {
  const render_namespace = "render_" + namespace;
  if (window[render_namespace] == undefined) {
    window[render_namespace] = {};
  }
  let component_name = name;
  if (sub_class == undefined) {
    console.log(`registering undefined ${name} in ${namespace}`);
  }
  if (sub_class.length > 0) {
    const wrapping_class = window[render_namespace][name];
    if (wrapping_class == undefined) {
      throw new Error(`Failed to find wrapping class ${name} for ${sub_class}`);
    }
    wrapping_class[sub_class] = constructor;
    component_name = `${name}.${sub_class}`;
  } else {
    window[render_namespace][name] = constructor;
  }
  // fixme: we can probably move this at the top level
  if (window.componentRegister == undefined) {
    window.componentRegister = new Map();
  }
  if (!window.componentRegister.has(namespace)) {
    window.componentRegister.set(namespace, new Map());
  }
  window.componentRegister.get(namespace).set(component_name, lazy ? wrap_inside_suspense(constructor) : constructor);
}

export function registerComponents(components, namespace) {
  for (const [name, sub_class, constructor, lazy] of components) {
    registerComponent(name, sub_class, constructor, namespace, lazy);
  }
}

export function registerModuleDeferred(name, callback) {
  if (window.modules_callbacks == undefined) {
    window.modules_callbacks = new Map();
  }
  window.modules_callbacks.set(name, callback);
}

export function registerModuleAttributes(namespace: string, module) {
  for (const [name, attribute] of Object.entries(module)) {
    try {
      registerComponent(name, [], attribute, namespace);
    } catch (e) {
      console.error(`failed to register ${name} in ${namespace}`, e);
    }
  }
}

export async function loadScript(module_name, url: string) {
  await new Promise((resolve, fail) => {
    const tag = document.createElement("script");
    tag.onload = resolve;
    tag.onerror = fail;
    tag.src = url;
    document.body.appendChild(tag);
  });
  console.log("loaded module", module_name, url);
  return window[module_name];
}

function resolveComponent({ module, js_name }: { module: string, js_name: string }) {
  const componentsForNamespace = window.componentRegister.get(module);
  if (!componentsForNamespace) {
    throw new Error(`unknown library ${module}`);
  }
  let actual_component = componentsForNamespace.get(js_name);
  if (actual_component === undefined) {
    throw new Error(`constructor ${js_name} not found in ${module} module`);
  }
  return actual_component;
}

const CLIENT_MESSAGE_PREFIX = 0;


class Context {
  constructor() {
    this.socket = null;
    this.callbacks = new Map();
    this.buffer = [];
    this.original_message = null;
    this.flush_pending = false;
    this.session_id = 0;
    this.kernel_id = 0;
    this.start_time = 0;
    this.dev = false;
    autoBind(this);
  }

  send(...msg: any[]) {
    if (msg.length == 1) {
      msg = msg[0]
    }
    this.buffer.push(msg);
    if (!this.flush_pending) {
      this.flush_pending = true;
      setTimeout(this._flush_buffer, 0);
    }
  }

  async _flush_buffer() {
    if (
      this.socket == null ||
      this.socket.readyState === 0
    ) {
      setTimeout(this._flush_buffer, 100);
    } else {
      this.flush_pending = false;
      while (this.buffer.length > 0) {
        let message = this.buffer.shift();
        this.socket.send(new Uint8Array([...encode(CLIENT_MESSAGE_PREFIX), ...encode(context.session_id), ...encode(message)]));
      }
    }
  }
}

function changeFavicon(src) {
  const oldLink = document.getElementById("dynamic-favicon");
  let link = document.createElement("link");
  link.id = "dynamic-favicon";
  link.rel = "shortcut icon";
  // fully specifying the address to create a dedicated connection as the original
  // connection can be closed before we have time to return the icon
  // link.href = `${location}/${src}`;
  link.href = src;
  if (oldLink) {
    document.head.removeChild(oldLink);
  }
  document.head.appendChild(link);
}

function invoke_method(object, data) {
  const [_, method_name, serialized_call_args, result_id] = data;
  let call_result = null;
  let success = false;
  try {
    const call_args = serialized_call_args.map((arg) =>
      deserializeComponentOrData(null, `${method_name} arguments`, arg)
    );
    for (let i = 0; i + 1 < method_name.length; i++) {
      object = object[method_name[i]];
    }
    // no such thing as a bound method in JS so we need to call this in one go...
    call_result = object[method_name[method_name.length - 1]](...call_args);
    success = true;
  } catch (e) {
    console.error(object, method_name[method_name.length - 1]);
    call_result = `${method_name} call failed: ${e.message}`;
  }
  if (result_id != null) {
    context.send("remote call outcome", [
      result_id,
      success,
      serialize_value(call_result),
    ]);
  }
}

function format_time(seconds) {
  var numhours = parseInt(
    Math.floor(((seconds % 31536000) % 86400) / 3600),
    10
  );
  var numminutes = parseInt(
    Math.floor((((seconds % 31536000) % 86400) % 3600) / 60),
    10
  );
  var numseconds = parseInt((((seconds % 31536000) % 86400) % 3600) % 60, 10);
  return (
    (numhours < 10 ? "0" + numhours : numhours) +
    ":" +
    (numminutes < 10 ? "0" + numminutes : numminutes) +
    ":" +
    (numseconds < 10 ? "0" + numseconds : numseconds)
  );
}

function update_component_state(component_record, update) {
  const { props, children, constructor } = build_children_and_props(
    component_record,
    update
  );
  const { state } = component_record;
  // FIXME: should we remove null props?
  state["props"] = Object.assign({}, state["props"], props);
  if (constructor) {
    state["constructor"] = constructor;
  }
  if (children != null) {
    state["children"] = children;
  }
}

const context = new Context();

window.reflect.context = context; // this is used by the callbacks

function onHashChange() {
  context.send("hash", location.hash.slice(1));
}

function apply_component_update(
  component_record: ComponentRecord,
  update: any
) {
  update_component_state(component_record, update);
  if (component_record.is_mounted) {
    component_record.component.setState(component_record.state);
  } else {
    component_record.pending_updates.push(component_record.state);
  }
}

function sendBrowserDetails() {
  context.send("browser_details", {
    width: window.outerWidth,
    height: window.outerHeight,
    platform: getOS(),
    userAgent: navigator.userAgent,
    is_touch_device: isTouchDevice(),
  });
}

function create_js_callback(name, definition) {
  const method = R.curry(eval(definition));
  return (...args) => {
    try {
      return method(...args);
    } catch (e) {
      console.error(e, name, definition)
    }
  };
}

function process_message(event) {
  const message = event.data;
  if (message) {
    const [_message_type, _session_id, decoded_message] = decodeMulti(message);
    const [_message_id, [code, data]] = decoded_message;
    if (code != "pong" && code != "python") {
      window.last_message = decoded_message;
    }

    switch (code) {
      case "session":
        const [session_id, kernel_id, pid, start_time, dev, script_path] = data;
        context.session_id = session_id;
        context.kernel_id = kernel_id;
        context.start_time = start_time;
        context.dev = dev;
        if (location.pathname == "/") {
          history.pushState({}, null, "app/" + script_path);
        }
        console.log(
          `session: ${session_id}, kernel_id: ${kernel_id}, pid: ${pid}`
        );
        break;
      case "load js module":
        const callback = window.modules_callbacks.get(data);
        if (!callback) {
          throw new Error(`failed to load unknown module ${data}`);
        }
        callback().then(() => {
          context.send("module loaded", data);
          console.info(`loaded ${data} module`);
        });
        break;
      case "root":
        deserializeComponentOrData(component_records.get(0), `${method_name} arguments`, data);
        createRoot(document.getElementById("root")).render(
          component_records.get(0).react_element
        );
        break;
      case "update":
        const [update_id, updates] = data;
        for (const [_data_type, update] of updates) {
          const component_record = component_records.get(update.nb);
          if (component_record == undefined) {
            throw new Error(
              `failed to find component_record for component ${update.nb
              }, existing keys: ${Array.from(component_records.keys()).join()}`
            );
          }
          apply_component_update(component_record, update);
        }
        break;
      case "remote call":
        const [object_id] = data;
        try {
          let maybe_object = dom_object_or_refs.get(object_id);
          // we might receive calls before the object/components have been created/rendered
          if (maybe_object == undefined) {
            let pending_calls_for_object = pending_calls.get(object_id);
            if (pending_calls_for_object == undefined) {
              pending_calls_for_object = [];
              pending_calls.set(object_id, pending_calls_for_object);
            }
            pending_calls_for_object.push(data);
          } else {
            invoke_method(maybe_object, data);
          }
        } catch (e) {
          context.send("remote call error", [data, `${e}`]);
          throw e;
        }
        break;
      case "promise_result":
        const [promise_id, succeded, result] = data;
        pending_promises[promise_id][succeded ? 0 : 1](result);
        pending_promises.delete(promise_id);
        break;
      case "js free method call":
        const [method_name, call_args] = deserializeComponentOrData(
          null,
          `${method_name} arguments`,
          data
        );
        resolveMethod(method_name)(...call_args);
        break;
      case "delete":
        component_records.delete(data);
        dom_object_or_refs.delete(data);
        break;
      case "console":
        const [method, args] = data;
        console[method](...args);
        break;
      case "python":
        console.log(`> ${data.join("")}`);
        break;
      case "update tab name":
        document.title = data;
        break;
      case "add links":
        add_links(data);
        break;
      case "variable":
        const [variable_id, operation, operation_args] = data;
        switch (operation) {
          case "create":
            variables.set(variable_id, { value: operation_args });
            break;
          case "delete":
            variables.delete(operation_args);
            break;
          case "invoke":
            const [method, invoke_args] = operation_args;
            variables.get(variable_id).value[method](...invoke_args);
        }
        break;
      case "favicon":
        changeFavicon(data);
        break;
      case "error":
        window.alert(data);
        break;
      case "fatal error":
        console.error(data);
        ReactDOM.render(
          React.createElement("pre", { style: {} }, data),
          document.getElementById("root")
        );
        break;
      case "method_def":
        const [name, definition] = data;
        try {
          registerMethod(name, create_js_callback(name, definition));
        } catch (e) {
          console.error("invalid method definition", data, e);
        }
        break;
      case "slave process terminated":
        console.error("slave process terminated", data);
        context.socket.close();
        break;
      case "pong":
        console.debug("received pong");
        break;
      case "session end":
        console.info("session ended");
        // location.reload();
        break;
      default:
        throw new Error(
          `unexpected code received "${code}" , "${decoded_message}"`
        );
    }
  }
}


function create_websocket() {
  const start = new Date();
  const address =
    (location.protocol == "https:" ? "wss://" : "ws://") +
    location.host +
    "/ws";
  let socket = new WebSocket(address);
  socket.binaryType = "arraybuffer";
  socket.onopen = () => {
    let location = window.location.pathname.slice(1);
    if (location.startsWith("app/")) {
      location = location.slice(4)
    }
    context.send([`${location}${window.location.hash}`, navigator.userAgent, window.outerWidth, window.outerHeight, context.kernel_id, context.start_time, context.session_id]);
    window.addEventListener("hashchange", onHashChange);
  };
  socket.onclose = function (e) {
    console.info(`Session lasted ${format_time((new Date() - start) / 1000)}`, e);
    for (let call_backs of context.callbacks.values()) {
      call_backs["terminate"]();
    }
    context.socket = null;
    if (context.dev || confirm("Session ended, do you want to reload the page?")) {
      location.reload();
    }
  };
  socket.onerror = function (err) {
    console.info("error callback", err);
  };
  // FIXME: we should ensure that messages are processed sequentially (so make this method sync...???)
  socket.onmessage = process_message;
  return socket;
}

export async function main() {
  context.socket = create_websocket();
}

export function send_message_to_server(message) {
  context.send("message_from_client", message);
}

window.reflect.send_message_to_server = send_message_to_server;

function serialize_value(value: any) {
  if (typeof value == "object" && value != null) {
    const value_type = value.constructor.name;
    switch (value_type) {
      case "Date":
        return ["datetime", value.getTime()];
      // FIXME: Ant returns moment objects, the class name is shorten in prod...
      case "M":
      case "k": // it seems that the constructor is also abbreviated to this???
      case "Moment":
        return ["datetime", value.valueOf()];
      case "Array":
        return ["list", value.map(serialize_value)];
      case "Object":
        return [
          "dict",
          Object.entries(value).map(([name, value]) => [
            name,
            serialize_value(value),
          ]),
        ];
      default:
        console.error("serializing", value_type, value);
        throw new Error(`unsupported return type ${value_type}, ${value}`);
    }
  }
  return ["value", value];
}

const create_callback = (component_record, callback_details) => {
  const {
    description,
    callback_id,
    js_name,
    data_paths,
    stop_propagation,
    is_promise,
    prevent_default,
    input_control_params,
  } = callback_details;
  let method = null;
  if (data_paths) {
    method = new_fetch_attributes(data_paths);
  }
  return (...args) => {
    // FIXME: this should be constructed outside the method (we should even create wrap the onChange method if any)
    if (input_control_params) {
      const [value_name, new_value_path] = input_control_params;
      component_record.state.props[value_name] = fetch_attribute(
        new_value_path
      )(...args);
      component_record.component.setState(component_record.state);
      // workaround for antd input components screwing zoom on mobile (doesn't work on FF unfortunately)
    }
    if (stop_propagation) {
      args[0].stopPropagation();
    }
    if (prevent_default) {
      args[0].preventDefault();
    }
    if (callback_id == undefined) {
      return null;
    }
    let value = [];
    if (method) {
      value = method(args);
    }
    try {
      value = serialize_value(value);
    } catch (e) {
      console.log(e);
      throw new Error(
        `failed to serialize ${value} ${js_name} ${data_paths} result, ${value} ${e}`
      );
    }
    let promise_id = is_promise ? current_promise_id : null;
    context.send("event", [description, callback_id, promise_id, value]);
    if (is_promise) {
      return new Promise((resolve, reject) => {
        pending_promises[promise_id] = [resolve, reject];
        current_promise_id += 1;
      }).catch((error) => console.error(error));
    }

  };
};

function build_children_and_props(component_record, update) {
  const { nb, _children, props, key, error } = update;
  const props_defs = Object.fromEntries(
    Object.entries(props || []).map(([name, details]) => {
      return [name, deserializeComponentOrData(component_record, name, details)];
    })
  );
  const _props = { key, ...props_defs };
  let children = null;
  if (error) {
    children = [React.createElement("pre", { style: { color: "red", "borderStyle": "dotted" } }, error)];
  } else {
    children =
      _children != null && _children != undefined
        ? _children.map((data_args: any) => {
          return deserializeComponentOrData(component_record, "children", data_args, true);
        })
        : null;
  }
  component_record.state["children"] = children;
  const result = { ["props"]: _props, ["children"]: children };
  if (update.module) {
    result.constructor = resolveComponent(update);
  }
  return result;
}

function deserialize_js_method(component_record, name, data_args) {
  const [method_name, serialized_args] = data_args;
  const curried_args = serialized_args.map((arg) =>
    deserializeComponentOrData(component_record, `${name} arguments`, arg)
  );
  let method = resolveMethod(method_name);
  const curried_method =
    curried_args.length > 0 ? method(...curried_args) : method;
  if (curried_method == undefined || null) {
    throw new Error(
      `Invalid argument ${name}, js method ${method_name}, curried with ${curried_args} ${method}`
    );
  }
  return curried_method;
}

type ComponentRecord = {
  pending_updates: any[];
  state: any;
  is_mounted: boolean;
};

function createOrReuseComponent(details) {
  let component_record: ComponentRecord = component_records.get(details.nb);
  if (details.reuse) {
    if (component_record) {
      return component_record.react_element;
    } else {
      throw new Error(`Component ${details.nb} is missing. {}`);
    }
  }
  // the root component_record is created a null component
  if (component_record != undefined && component_record.react_element) {
    update_component_state(component_record, details);
    return component_record.react_element;
  }
  component_record = {
    state: { props: {} },
    pending_updates: [],
    is_mounted: false,
  };
  component_records.set(details.nb, component_record);
  // rmk: we need to build a valid component_record before calling this method
  component_record.state = build_children_and_props(component_record, details);
  const constructor = resolveComponent(details);
  // rmk: we might have a race condition if we have received an update before reaching that line (not sure it is possible though)
  component_record.react_element = details.statefull
    ? React.createElement(StateComponent, {
      ["key"]: details.key,
      constructor,
      details,
      component_record: component_record,
    })
    : React.createElement(
      constructor,
      component_record.state.props,
      ...(component_record.state.children || [])
    );
  return component_record.react_element;
}

function deserializeComponentOrData(
  component_record,
  name: string,
  [dataType, details],
  call_method = false
) {
  switch (dataType) {
    case "value":
      return details;
    case "component":
      return createOrReuseComponent(details);
    case "dict":
      return Object.fromEntries(
        details.map(([name, value]) => [
          name,
          deserializeComponentOrData(component_record, name, value),
        ])
      );
    case "list":
      return details.map((value, index) =>
        deserializeComponentOrData(component_record, index, value)
      );
    case "date":
      return new Date(details * 1000);
    case "js_method":
      const method = deserialize_js_method(component_record, name, details);
      return call_method ? method() : method;
    case "js_expression":
      return () => eval(details);
    case "callback":
      return create_callback(component_record, details);
    case "object":
      return variables.get(details);
    default:
      throw new Error(`unexpected ${dataType}: ${details}`);
  }
}

class StateComponent extends React.Component {
  constructor(props: any) {
    super(props);
    const { details, component_record, onFinish } = props;
    this.state = component_record.state;
    //FIXME this is a bit messy
    this.state.component_record = component_record;
    // FIXME we should move this out (so that we don't need to wrap component needlessly)
    if (details.ref_hook) {
      this.state.props[details.ref_hook] = (ref) => {
        // we sometime get a null reference which upset the weakMapValue...
        if (ref) {
          dom_object_or_refs.set(details.nb, ref);
        }
      };
    }
    component_record.component = this;
    if (onFinish) {
      onFinish();
    }
  }

  render() {
    let { props, children, constructor, error } = this.state;
    if (error) {
      console.error(error);
      [constuctor, props, children] = ["pre", {}, error];
    }
    try {
      if (
        constructor.displayName == "Tooltip" &&
        children &&
        children.length == 1 &&
        typeof children[0] == "object" &&
        children[0].type.name == "StateComponent"
      ) {
        // this is a workaround for components which do not support having a StateComponent as unique child (eg: Ant.Tooltip)
        children = [React.createElement("div", { ["key"]: 0 }, ...children)];
      }
      return React.createElement(constructor, props, ...(children || []));
    } catch (e) {
      console.error(e, constructor, props);
      throw e;
    }
  }

  componentDidMount() {
    this.state.component_record.is_mounted = true;
    for (const state of this.state.component_record.pending_updates) {
      this.setState(state);
    }
    this.state.component_record.pending_updates = [];
    const pending_calls_for_object = pending_calls.get(this.props.details.nb);
    if (pending_calls_for_object != undefined) {
      pending_calls.delete(this.props.details.nb);
      let ref = dom_object_or_refs.get(this.props.details.nb);
      pending_calls_for_object.map((args) => invoke_method(ref, args));
    }
    // the root eventDidMount event might be send before the location (because of the fact that the sending order is not completly determinstic until the websocket is open)
    // if (this.props.details.nb > 0) {
    context.send("componentDidMount", this.props.details.nb);
    // }
  }

  componentWillUnmount() {
    this.state.component_record.is_mounted = false;
    context.send("componentWillUnmount", this.props.details.nb);
  }
}

class ErrorBoundary extends React.Component {
  constructor(props) {
    super(props);
    this.state = { hasError: false, error: null };
  }

  static getDerivedStateFromError(error: Error) {
    return { hasError: true, error: error.toLocaleString() };
  }

  componentDidCatch(error: Error, errorInfo) {
    console.error(error, errorInfo);
  }

  render() {
    if (this.state.hasError) {
      return React.createElement(
        "h3",
        { style: { color: "red" } },
        `"${this.state.error}", see details in error log.`
      );
    }
    return this.props.underlying_children;
  }
}

registerComponent("ErrorBoundary", "", ErrorBoundary, "core");

function ServerErrorTraceback({ traceback }) {
  return <pre>{traceback}</pre>;
}

registerComponent("ServerErrorTraceback", "", ServerErrorTraceback, "core");
