/* AUTO GENERATED FILE - DO NOT EDIT! */

import { registerComponent, registerModuleDeferred, registerMethod } from "../../app";
import { lazy } from "react";
import '@mantine/core/styles.css';
import '@mantine/dropzone/styles.css';
export function register() {
  registerModuleDeferred("mantine/dropzone", async () => {
    registerComponent('Dropzone', '', lazy(() => import("../../fragments/mantine/dropzone/dropzone.tsx")), 'mantine/dropzone', true)
    registerComponent('Dropzone', 'FullScreen', lazy(() => import("../../fragments/mantine/dropzone/dropzone_fullscreen.tsx")), 'mantine/dropzone', true)
  });
}