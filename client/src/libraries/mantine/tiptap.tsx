import { registerComponents, registerModuleDeferred } from "../../app";
import { lazy } from "react";
import '@mantine/core/styles.css';
import '@mantine/tiptap/styles.css';
const components = [
  ['RichTextEditor', [], lazy(() => import("../../fragments/mantine/tiptap/richtexteditor.tsx"))],
];
export function register() {
  registerModuleDeferred("mantine/tiptap", async () => {
    registerComponents(components, "mantine/tiptap", true);
  });
}