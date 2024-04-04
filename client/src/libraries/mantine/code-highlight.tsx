import { registerComponents, registerModuleDeferred } from "../../app";
import { lazy } from "react";
import '@mantine/core/styles.css';
import '@mantine/code-highlight/styles.css';
const components = [
  ['InlineCodeHighlight', [], lazy(() => import("../../fragments/mantine/code-highlight/inlinecodehighlight.tsx"))],
  ['CodeHighlight', ['Tabs'], lazy(() => import("../../fragments/mantine/code-highlight/codehighlight.tsx"))],
];
export function register() {
  registerModuleDeferred("mantine/code-highlight", async () => {
    registerComponents(components, "mantine/code-highlight", true);
  });
}