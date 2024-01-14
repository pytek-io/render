import { registerComponent, registerModuleDeferred } from "../app";

export function register() {
  registerModuleDeferred("altair", async () => {
    const { Vega } = await import("react-vega");
    // not sure we need the forward ref, but just in case...
    const MyVega = React.forwardRef((props, ref) => {
      let actual_style = {};
      let { style, ...rest } = props;
      if (style) {
        let { height, width }  = style;
        if (!height) {
          style[height] = "inherit"
        }
        if (!width) {
          style["width"] ="inherit"
        }
        actual_style = style
      }
      const modified_props = {
        style: actual_style,
        ...rest,
      };
      return <Vega ref={ref} {...modified_props} />;
    });
    registerComponent("Chart", MyVega, "altair");
  });
}
