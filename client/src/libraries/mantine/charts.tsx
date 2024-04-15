import { registerComponents, registerModuleDeferred } from "../../app";
import { lazy } from "react";
import '@mantine/core/styles.css';
import '@mantine/charts/styles.css';
const components = [
  ['Sparkline', '', lazy(() => import("../../fragments/mantine/charts/sparkline.tsx")), true],
  ['LineChart', '', lazy(() => import("../../fragments/mantine/charts/linechart.tsx")), true],
  ['DonutChart', '', lazy(() => import("../../fragments/mantine/charts/donutchart.tsx")), true],
  ['RadarChart', '', lazy(() => import("../../fragments/mantine/charts/radarchart.tsx")), true],
  ['AreaChart', '', lazy(() => import("../../fragments/mantine/charts/areachart.tsx")), true],
  ['BarChart', '', lazy(() => import("../../fragments/mantine/charts/barchart.tsx")), true],
  ['PieChart', '', lazy(() => import("../../fragments/mantine/charts/piechart.tsx")), true],
];
export function register() {
  registerModuleDeferred("mantine/charts", async () => {
    registerComponents(components, "mantine/charts");
  });
}