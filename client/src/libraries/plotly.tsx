import { registerComponent, registerModuleDeferred } from "../app";

export function register() {
  registerModuleDeferred("plotly", async () => {
    registerComponent(
      "Plot", "",
      (await import("react-plotly.js")).default,
      "plotly"
    );
  });
}
