import { registerComponents, registerModuleDeferred, registerMethod } from "../../app";
import { lazy } from "react";
import '@mantine/core/styles.css';
import '@mantine/dropzone/styles.css';
const components = [
  ['Dropzone', '', lazy(() => import("../../fragments/mantine/dropzone/dropzone.tsx")), true],
  ['Dropzone', 'FullScreen', lazy(() => import("../../fragments/mantine/dropzone/dropzone_fullscreen.tsx")), true],
];
export function register() {
  registerModuleDeferred("mantine/dropzone", async () => {
    registerComponents(components, "mantine/dropzone");
  });
}