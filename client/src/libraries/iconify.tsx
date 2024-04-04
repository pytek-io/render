import { registerComponent, registerModuleDeferred } from "../app";


export function register() {
  registerModuleDeferred("iconify", async () => {
    const iconify = (await import("@iconify/react"));
    registerComponent("Icon", "", iconify.Icon, "iconify");
    registerComponent("InlineIcon", "", iconify.InlineIcon, "iconify");
  });
}
