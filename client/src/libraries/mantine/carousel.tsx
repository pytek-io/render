import { registerComponents, registerModuleDeferred } from "../../app";
import { lazy } from "react";
const components = [
  ["Carousel", lazy(() => import("../../fragments/mantine/carousel/carousel.tsx"))],
];
export function register() {
  registerModuleDeferred("mantine/carousel", async () => {
    import('@mantine/carousel/styles.css');
    registerComponents("mantine/carousel", components, true);
  });
}