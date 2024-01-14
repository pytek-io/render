from ._auto import AgGridColumn, AgGridReact

ColumnGroup = AgGridColumn

CREATE_CONTEXT_MENU_ITEMS_JS = """(callback_id, params, args) => {
    if (!args.node) {
        return [];
    }
    return params.map(({ name, confirmation, code }) => {
        return { name, action: () => render.notify_event(callback_id, [code, args.node.id]) };
    });
}"""