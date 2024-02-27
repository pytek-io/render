import { registerComponent, registerModuleDeferred } from "../app";

export function register_mantine_prism() {
  const module_name = "mantine_prism";
  registerModuleDeferred(module_name, async () => {
    const module = await import("@mantine/code-highlight");
    registerComponent("Prism", module.Prism, module_name);
  });
}
