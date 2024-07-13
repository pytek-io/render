/* AUTO GENERATED FILE - DO NOT EDIT! */

import { registerComponent, registerModuleDeferred, registerMethod } from "../../app";
import { lazy } from "react";
import '@mantine/core/styles.css';
import '@mantine/spotlight/styles.css';
export function register() {
  registerModuleDeferred("mantine/spotlight", async () => {
    registerComponent('Spotlight', '', lazy(() => import("../../fragments/mantine/spotlight/spotlight.tsx")), 'mantine/spotlight', true)
  });
}