import { registerModuleAttributes, registerModuleDeferred } from "../app";

export function register() {
  registerModuleDeferred("mantine", async () => {
    registerModuleAttributes("mantine", await import("@mantine/core"));
  });
}
