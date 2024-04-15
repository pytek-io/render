import { registerComponents, registerModuleDeferred } from "../../app";
import { lazy } from "react";
import '@mantine/core/styles.css';
import '@mantinex/shiki/styles.css';
const components = [
  ['CodeHighlight', '', lazy(() => import("../../fragments/mantinex/shiki/codehighlight.tsx")), true],
  ['CodeHighlight', 'Tabs', lazy(() => import("../../fragments/mantinex/shiki/codehighlight_tabs.tsx")), true],
];
export function register() {
  registerModuleDeferred("mantinex/shiki", async () => {
    registerComponents(components, "mantinex/shiki");
  });
}