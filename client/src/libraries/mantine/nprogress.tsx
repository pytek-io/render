import { registerComponents, registerModuleDeferred } from "../../app";
import { lazy } from "react";
const components = [
  ["NavigationProgress", lazy(() => import("../../fragments/mantine/nprogress/navigationprogress.tsx"))],
];
export function register() {
  registerModuleDeferred("mantine/nprogress", async () => {
    import('@mantine/nprogress/styles.css');
    registerComponents("mantine/nprogress", components, true);
  });
}