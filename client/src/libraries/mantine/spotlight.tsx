import { registerComponents, registerModuleDeferred } from "../../app";
import { lazy } from "react";
const components = [
  ["Spotlight", lazy(() => import("../../fragments/mantine/spotlight/spotlight.tsx"))],
];
export function register() {
  registerModuleDeferred("mantine/spotlight", async () => {
    import('@mantine/spotlight/styles.css');
    registerComponents("mantine/spotlight", components, true);
  });
}