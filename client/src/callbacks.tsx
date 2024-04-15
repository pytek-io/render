import { registerMethod } from "./app";

function update_element_prop(tag_name: string, property_path: string[], properties) {
    let element = document.getElementsByTagName(tag_name);
    for (const key of property_path) {
        element = element[key];
    }
    for (const [key, value] of properties) {
        element[key] = value;
    }
}

function call_js_builtin_method(path: string, args: any[]) {
    const parsed_name = path.split(".");
    let actual_object = window;
    for (let i = 0; i + 1 < parsed_name.length; i++) {
        actual_object = actual_object[parsed_name[i]];
        if (actual_object === undefined) {
            throw new Error(`invalid method ${path}`);
        }
    }
    actual_object[parsed_name[parsed_name.length - 1]](...args);
}

function add_event_listener(eventName: string, callBack) {
    document.addEventListener(eventName, (event) => {
        window.reflect.context.send("event fired", [eventName, callBack(event)]);
    });
}

export function register_callbacks() {
    registerMethod("", "call_js_builtin_method", call_js_builtin_method);
    registerMethod("", "add_event_listener", add_event_listener);
    registerMethod("", "update_element_prop", update_element_prop);
    registerMethod("", "window.open", window.open);
    registerMethod("", "constant", (x: any) => () => x);
    registerMethod("", "identity", (x: any) => x);
    registerMethod("", "key", (event: any) => event.key);
    registerMethod("", "id", (data: any) => data.id);

    registerMethod("", "location.reload", () => window.location.reload());
    registerMethod("", "reset_zoom", () => {
        const viewportmeta = document.querySelector("meta[name=viewport]");
        viewportmeta.setAttribute("content", "width=device-width, initial-scale=0");
    });
    registerMethod("", "history.pushState", (newUrl: string) =>
        history.pushState({}, null, newUrl)
    );
    registerMethod("", "trigger.resize", () =>
        window.dispatchEvent(new Event("resize"))
    );
    registerMethod("", "update_full_screen", (full_screen: boolean) => {
        if (full_screen) {
            document.documentElement.requestFullscreen();
        } else {
            document.exitFullscreen();
        }
    });
    registerMethod("", "update_hash", (content: null|string) => {
        if (window.location.hash || (content != null && content != "")) {
            window.location.hash = content;
        }
    });
}