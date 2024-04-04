import { registerComponents, registerModuleDeferred } from "../../app";
import { lazy } from "react";
import '@mantine/core/styles.css';
import '@mantine/dropzone/styles.css';
const components = [
  ['Dropzone', ['FullScreen'], lazy(() => import("../../fragments/mantine/dropzone/dropzone.tsx"))],
];
export function register() {
  registerModuleDeferred("mantine/dropzone", async () => {
    registerComponents(components, "mantine/dropzone", true);
  });
}