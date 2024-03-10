import { registerComponents, registerModuleDeferred } from "../../app";
import { lazy } from "react";
const components = [
  ["CodeHighlight", lazy(() => import("../../fragments/mantinex/shiki/codehighlight.tsx"))],
  ["CodeHighlight.Tabs", lazy(() => import("../../fragments/mantinex/shiki/codehighlight_tabs.tsx"))],
];
export function register() {
  registerModuleDeferred("mantinex/shiki", async () => {
    import('@mantinex/shiki/styles.css');
    registerComponents("mantinex/shiki", components, true);
  });
}