import { registerComponents, registerModuleDeferred } from "../../app";
import { lazy } from "react";
import '@mantine/core/styles.css';
import '@mantine/carousel/styles.css';
const components = [
  ["Carousel", lazy(() => import("../../fragments/mantine/carousel/carousel.tsx"))],
];
export function register() {
  registerModuleDeferred("mantine/carousel", async () => {
    registerComponents("mantine/carousel", components, true);
  });
}