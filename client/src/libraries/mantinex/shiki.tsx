/* AUTO GENERATED FILE - DO NOT EDIT! */

import { registerComponent, registerModuleDeferred, registerMethod } from "../../app";
import { lazy } from "react";
import '@mantine/core/styles.css';
import '@mantinex/shiki/styles.css';
export function register() {
  registerModuleDeferred("mantinex/shiki", async () => {
    registerComponent('CodeHighlight', '', lazy(() => import("../../fragments/mantinex/shiki/codehighlight.tsx")), 'mantinex/shiki', true)
    registerComponent('CodeHighlight', 'Tabs', lazy(() => import("../../fragments/mantinex/shiki/codehighlight_tabs.tsx")), 'mantinex/shiki', true)
  });
}