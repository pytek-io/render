/* AUTO GENERATED FILE - DO NOT EDIT! */

import { registerComponent, registerModuleDeferred, registerMethod } from "../../app";
import { lazy } from "react";
import '@mantine/core/styles.css';
import '@mantine/nprogress/styles.css';
export function register() {
  registerModuleDeferred("mantine/nprogress", async () => {
    registerComponent('NavigationProgress', '', lazy(() => import("../../fragments/mantine/nprogress/navigationprogress.tsx")), 'mantine/nprogress', true)
  });
}