import { registerComponents, registerModuleDeferred, registerMethod } from "../../app";
import { lazy } from "react";
import '@mantine/core/styles.css';
import '@mantine/spotlight/styles.css';
const components = [
  ['Spotlight', '', lazy(() => import("../../fragments/mantine/spotlight/spotlight.tsx")), true],
];
export function register() {
  registerModuleDeferred("mantine/spotlight", async () => {
    registerComponents(components, "mantine/spotlight");
  });
}