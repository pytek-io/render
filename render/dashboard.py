import os
import platform

import anyio
import render_aggrid as aggrid
import render_antd as antd
import render_html as html
from psutil import Process
from render_utils.common import create_file_chooser
from render_utils.formatters import (
    compose,
    filesize,
    pythonTimeStampToJSDate,
    round_value,
    toLocaleString,
    transform_if_number,
)

import render as r

Title = antd.Typography.Title
Header, Content, Footer, Sider = (
    antd.Layout.Header,
    antd.Layout.Content,
    antd.Layout.Footer,
    antd.Layout.Sider,
)
TITLE = "Render dashboard"
format_date = r.js_arrow("format_date", "(value) => new Date(value.value * 1000).toLocaleString()")


def create_columns():
    return [
        aggrid.AgGridColumn(field="id", headerName="Kernel id", width=100, sortable=True),
        aggrid.AgGridColumn(field="process_id", headerName="Pid", width=90, sortable=True),
        aggrid.AgGridColumn(
            field="rss",
            headerName="Real Mem",
            width=100,
            sortable=True,
            valueFormatter=transform_if_number(filesize),
            type="rightAligned",
        ),
        aggrid.AgGridColumn(
            field="cpu",
            headerName="CPU%",
            width=80,
            sortable=True,
            valueFormatter=transform_if_number(round_value(2)),
            type="rightAligned",
        ),
        aggrid.AgGridColumn(field="status", headerName="Status", width=90, sortable=True),
        aggrid.AgGridColumn(field="apps", headerName="Apps", width=250, sortable=True),
        aggrid.AgGridColumn(
            field="start",
            headerName="Start",
            valueFormatter=transform_if_number(compose(pythonTimeStampToJSDate, toLocaleString)),
            width=160,
            sortable=True,
        ),
    ]


CREATION_FIELDS = ["id", "process_id", "application"]
UPDATE_FIELDS = ["id", "rss", "cpu"]
ALMOST_BLACK = "#0f1724"


def gather_process_info(process_id):
    try:
        ps_process = Process(process_id)
        return {
            "process_id": ps_process.pid,
            "rss": ps_process.memory_info().rss,
            "cpu": ps_process.cpu_percent(),
            "status": ps_process.status(),
        }
    except Exception as e:
        return {"status": str(e)}


class App:
    def __init__(self, window) -> None:
        self.window: r.Window = window
        self.grid = aggrid.AgGridReact(
            create_columns,
            getRowId=r.js_arrow("data.id", "({data}) => data.id"),
            defaultColDef={"resizable": True, "filter": True, "sortable": True},
            componentDidMount=self.main,
            onGridReady=lambda: window.task_group.start_soon(self.update_processes_details),
        )

    async def main(self):
        await self.grid.applyTransactionAsync(
            {
                "add": [
                    dict(
                        id=kernel_id,
                        start=start,
                        apps=",".join(sessions.values()),
                        **gather_process_info(pid),
                    )
                    for kernel_id, (
                        pid,
                        start,
                        sessions,
                    ) in self.window.kernel.kernels.items()
                ]
            }
        )
        with self.window.kernel.subscribe_to_kernel_updates() as update_stream:
            async for code, message in update_stream:
                if code == "new kernel":
                    kernel_id, pid, start_time = message
                    await self.grid.applyTransactionAsync(
                        {
                            "add": [
                                {
                                    "id": kernel_id,
                                    "start": start_time,
                                    **gather_process_info(pid),
                                }
                            ]
                        }
                    )
                elif code == "assigned session":
                    kernel_id, session_id, session = message
                    await self.grid.applyTransactionAsync(
                        {"udpate": [{"id": kernel_id, "session": session}]}
                    )
                elif code == "kernel ended":
                    kernel_id = message
                    await self.grid.applyTransactionAsync({"remove": [{"id": kernel_id}]})

    async def update_processes_details(self):
        while True:
            update = [
                {
                    "id": kernel_id,
                    "start": start_time,
                    "apps": ",".join(sessions.values()),
                    **gather_process_info(pid),
                }
                for kernel_id, (
                    pid,
                    start_time,
                    sessions,
                ) in self.window.kernel.kernels.items()
            ]
            await self.grid.applyTransactionAsync({"update": update})
            await anyio.sleep(1)


async def app(window: r.Window):
    application = App(window)
    await window.subscribe_to_kernel_updates()

    def on_ok(selected_path):
        window.call_js_method("window.open", ["/app/" + selected_path[:-3].replace(os.sep, ".")])

    file_selection_window, show_file_selection_window = create_file_chooser(
        title="Select app to launch", on_ok=on_ok
    )
    return antd.Layout(
        [
            Header(
                antd.Row(
                    [
                        antd.Col(
                            Title(f"{platform.node()}", level=4, style={"color": "white"}),
                            style={"float": "left", "color": "white"},
                        ),
                        antd.Col(
                            antd.Button("Launch app", onClick=show_file_selection_window),
                            style={"float": "right"},
                        ),
                    ],
                    style={"width": "100%"},
                    align="middle",
                    justify="space-between",
                ),
                id="header",
                style={"width": "100%", "background": ALMOST_BLACK},
            ),
            file_selection_window,
            html.div(application.grid, style={"height": "100%"}),
        ],
        style={"height": "100%", "width": "100%"},
    )
