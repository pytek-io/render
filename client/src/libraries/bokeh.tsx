import { registerComponent, registerModuleDeferred, loadScript } from "../app";
import React from "react";

const URI = "https://cdn.bokeh.org/bokeh/release/bokeh-2.4.2.min.js";

export function register() {
  registerModuleDeferred("bokeh", async () => {
    const Bokeh = await loadScript("Bokeh", URI);
    var counter = 0;
    class Figure extends React.Component {
      constructor(props) {
        super(props);
      }

      render() {
        const style = {
          width: this.props.width,
          height: this.props.height,
        };
        counter = counter + 1;
        return React.createElement(
          "div",
          {
            style: style,
            ref: (el) => el ? Bokeh.embed.embed_item(this.props.options, el.id) : null,
            className: "BokehFigure",
            id: `bokeh_${counter}_id`,
          },
          null
        );
      }
    }
    registerComponent("Figure", Figure, "bokeh");
  });
}
