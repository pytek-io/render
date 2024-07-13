/* AUTO GENERATED FILE - DO NOT EDIT! */

import { registerComponent, registerModuleDeferred, registerMethod } from "../../app";
import { lazy } from "react";
import '@mantine/core/styles.css';
import '@mantine/code-highlight/styles.css';
export function register() {
  registerModuleDeferred("mantine/code-highlight", async () => {
    registerComponent('InlineCodeHighlight', '', lazy(() => import("../../fragments/mantine/code-highlight/inlinecodehighlight.tsx")), 'mantine/code-highlight', true)
    registerComponent('CodeHighlight', '', lazy(() => import("../../fragments/mantine/code-highlight/codehighlight.tsx")), 'mantine/code-highlight', true)
    registerComponent('CodeHighlight', 'Tabs', lazy(() => import("../../fragments/mantine/code-highlight/codehighlight_tabs.tsx")), 'mantine/code-highlight', true)
  });
}