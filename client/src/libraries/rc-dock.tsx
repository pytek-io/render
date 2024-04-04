import { registerComponent, registerModuleDeferred } from "../app";

export function register() {
  registerModuleDeferred("rc-dock", async () => {
    const [{ DockLayout }, _] = await Promise.all([
      import("rc-dock"),
      import("../../rc-dock.css"),
    ]);
    // this could be implemented in python but for some reasons it freezes the whole component when inserting a new component
    const MyDockLayout = React.forwardRef((props, ref) => {
      return (
        <DockLayout
          ref={ref}
          onLayoutChange={() => window.dispatchEvent(new Event("resize"))}
          {...props}
        />
      );
    });
    registerComponent("DockLayout", "", MyDockLayout, "rc-dock");
  });
}
