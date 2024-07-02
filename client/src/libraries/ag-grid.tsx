import {
  registerComponent,
  registerModuleDeferred,
} from "../app";

const URI =
  "https://cdnjs.cloudflare.com/ajax/libs/ag-grid/25.1.0/ag-grid-community.min.js";


export function register() {
  registerModuleDeferred("ag-grid", async () => {
    const [numeral, filesize, module, _, _1] = await Promise.all([
      import("numeral"),
      import("filesize"),
      import("ag-grid-react"),
      import("ag-grid-enterprise"),
      import("ag-grid-community/dist/styles/ag-grid.css"),
    ]);
    window.numeral = numeral.default;
    window.filesize = filesize.default;
    const { AgGridColumn, AgGridReact } = module;

    registerComponent("AgGridReact", "", AgGridReact, "ag-grid");
    registerComponent("AgGridColumn", "", AgGridColumn, "ag-grid");
  });
}
