import { registerComponents, registerModuleDeferred } from "../../app";
import { lazy } from "react";
const components = [
  ["Sparkline", lazy(() => import("../../fragments/mantine/charts/sparkline.tsx"))],
  ["LineChart", lazy(() => import("../../fragments/mantine/charts/linechart.tsx"))],
  ["DonutChart", lazy(() => import("../../fragments/mantine/charts/donutchart.tsx"))],
  ["RadarChart", lazy(() => import("../../fragments/mantine/charts/radarchart.tsx"))],
  ["AreaChart", lazy(() => import("../../fragments/mantine/charts/areachart.tsx"))],
  ["BarChart", lazy(() => import("../../fragments/mantine/charts/barchart.tsx"))],
  ["PieChart", lazy(() => import("../../fragments/mantine/charts/piechart.tsx"))],
];
export function register() {
  registerModuleDeferred("mantine/charts", async () => {
    import('@mantine/charts/styles.css');
    registerComponents("mantine/charts", components, true);
  });
}