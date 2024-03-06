import { registerComponents, registerModuleDeferred } from "../../app";
import { lazy } from "react";
const components = [
  ["CodeHighlight", lazy(() => import("../../fragments/mantine/code-highlight/codehighlight.tsx"))],
  ["CodeHighlight.Tabs", lazy(() => import("../../fragments/mantine/code-highlight/codehighlight_tabs.tsx"))],
];
export function register() {
  registerModuleDeferred("mantine/code-highlight", async () => {
    import('@mantine/code-highlight/styles.css');
    registerComponents("mantine/code-highlight", components, true);
  });
}