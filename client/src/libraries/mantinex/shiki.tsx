import { registerComponents, registerModuleDeferred } from "../../app";
import { lazy } from "react";
import '@mantine/core/styles.css';
import '@mantinex/shiki/styles.css';
const components = [
  ['CodeHighlight', ['Tabs'], lazy(() => import("../../fragments/mantinex/shiki/codehighlight.tsx"))],
];
export function register() {
  registerModuleDeferred("mantinex/shiki", async () => {
    registerComponents(components, "mantinex/shiki", true);
  });
}