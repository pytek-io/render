/* AUTO GENERATED FILE - DO NOT EDIT! */

import { registerComponent, registerModuleDeferred, registerMethod } from "../../app";
import { lazy } from "react";
import '@mantine/core/styles.css';
import '@mantine/carousel/styles.css';
export function register() {
  registerModuleDeferred("mantine/carousel", async () => {
    registerComponent('Carousel', '', lazy(() => import("../../fragments/mantine/carousel/carousel.tsx")), 'mantine/carousel', true)
  });
}