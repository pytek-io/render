import { registerComponents, registerModuleDeferred } from "../../app";
import { lazy } from "react";
import '@mantine/core/styles.css';
import '@mantine/code-highlight/styles.css';
const components = [
  ['InlineCodeHighlight', '', lazy(() => import("../../fragments/mantine/code-highlight/inlinecodehighlight.tsx")), true],
  ['CodeHighlight', '', lazy(() => import("../../fragments/mantine/code-highlight/codehighlight.tsx")), true],
  ['CodeHighlight', 'Tabs', lazy(() => import("../../fragments/mantine/code-highlight/codehighlight_tabs.tsx")), true],
];
export function register() {
  registerModuleDeferred("mantine/code-highlight", async () => {
    registerComponents(components, "mantine/code-highlight");
  });
}