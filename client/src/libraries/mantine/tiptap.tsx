/* AUTO GENERATED FILE - DO NOT EDIT! */

import { registerComponent, registerModuleDeferred, registerMethod } from "../../app";
import { lazy } from "react";
import '@mantine/core/styles.css';
import '@mantine/tiptap/styles.css';
export function register() {
  registerModuleDeferred("mantine/tiptap", async () => {
    registerComponent('RichTextEditor', '', lazy(() => import("../../fragments/mantine/tiptap/richtexteditor.tsx")), 'mantine/tiptap', true)
  });
}