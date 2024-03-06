import { registerComponents, registerModuleDeferred } from "../../app";
import { lazy } from "react";
const components = [
  ["RichTextEditor", lazy(() => import("../../fragments/mantine/tiptap/richtexteditor.tsx"))],
];
export function register() {
  registerModuleDeferred("mantine/tiptap", async () => {
    import('@mantine/tiptap/styles.css');
    registerComponents("mantine/tiptap", components, true);
  });
}