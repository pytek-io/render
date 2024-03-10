import { registerComponents, registerModuleDeferred } from "../../app";
import { lazy } from "react";
import '@mantine/core/styles.css';
import '@mantine/nprogress/styles.css';
const components = [
  ["NavigationProgress", lazy(() => import("../../fragments/mantine/nprogress/navigationprogress.tsx"))],
];
export function register() {
  registerModuleDeferred("mantine/nprogress", async () => {
    registerComponents("mantine/nprogress", components, true);
  });
}