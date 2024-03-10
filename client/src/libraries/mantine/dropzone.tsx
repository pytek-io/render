import { registerComponents, registerModuleDeferred } from "../../app";
import { lazy } from "react";
import '@mantine/core/styles.css';
import '@mantine/dropzone/styles.css';
const components = [
  ["Dropzone", lazy(() => import("../../fragments/mantine/dropzone/dropzone.tsx"))],
  ["Dropzone.FullScreen", lazy(() => import("../../fragments/mantine/dropzone/dropzone_fullscreen.tsx"))],
];
export function register() {
  registerModuleDeferred("mantine/dropzone", async () => {
    registerComponents("mantine/dropzone", components, true);
  });
}