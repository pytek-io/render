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
    function convert_row_data(data) {
      if (data && data.constructor.name != "Array") {
        let actual_data = [];
        const entries = Object.values(data);
        const keys = Object.keys(data);
        for (var i = 0; i < entries[0].length; i++) {
          const obj = {};
          for (var j = 0; j < entries.length; j++) {
            obj[keys[j]] = entries[j][i];
          }
          actual_data.push(obj);
        }
        return actual_data;
      }
      return data;
    }
    const MyAgGridReact = React.forwardRef((props, ref) => {
      let { rowData, ...rest } = props;
      return (
        <AgGridReact
          ref={ref}
          rowData={convert_row_data(rowData)}
          {...rest}
        ></AgGridReact>
      );
    });
    registerComponent("AgGridReact", MyAgGridReact, "ag-grid");
    registerComponent("AgGridColumn", AgGridColumn, "ag-grid");
  });
}
