import { registerComponents, registerModuleDeferred } from "../../app";
import { lazy } from "react";
import '@mantine/core/styles.css';
import '@mantine/spotlight/styles.css';
const components = [
  ["Spotlight", lazy(() => import("../../fragments/mantine/spotlight/spotlight.tsx"))],
];
export function register() {
  registerModuleDeferred("mantine/spotlight", async () => {
    registerComponents("mantine/spotlight", components, true);
  });
}