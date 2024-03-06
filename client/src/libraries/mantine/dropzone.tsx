import { registerComponents, registerModuleDeferred } from "../../app";
import { lazy } from "react";
const components = [
  ["Dropzone", lazy(() => import("../../fragments/mantine/dropzone/dropzone.tsx"))],
  ["Dropzone.FullScreen", lazy(() => import("../../fragments/mantine/dropzone/dropzone_fullscreen.tsx"))],
];
export function register() {
  registerModuleDeferred("mantine/dropzone", async () => {
    import('@mantine/dropzone/styles.css');
    registerComponents("mantine/dropzone", components, true);
  });
}