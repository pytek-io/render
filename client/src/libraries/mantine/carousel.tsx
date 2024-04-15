import { registerComponents, registerModuleDeferred } from "../../app";
import { lazy } from "react";
import '@mantine/core/styles.css';
import '@mantine/carousel/styles.css';
const components = [
  ['Carousel', '', lazy(() => import("../../fragments/mantine/carousel/carousel.tsx")), true],
];
export function register() {
  registerModuleDeferred("mantine/carousel", async () => {
    registerComponents(components, "mantine/carousel");
  });
}