import { registerModule, registerModuleDeferred } from "../app";

export function register() {
  registerModuleDeferred("mantine", async () => {
    registerModule("mantine", await import("@mantine/core"));
  });
}
