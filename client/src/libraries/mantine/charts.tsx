/* AUTO GENERATED FILE - DO NOT EDIT! */

import { registerComponent, registerModuleDeferred, registerMethod } from "../../app";
import { lazy } from "react";
import '@mantine/core/styles.css';
import '@mantine/charts/styles.css';
export function register() {
  registerModuleDeferred("mantine/charts", async () => {
    registerComponent('Sparkline', '', lazy(() => import("../../fragments/mantine/charts/sparkline.tsx")), 'mantine/charts', true)
    registerComponent('LineChart', '', lazy(() => import("../../fragments/mantine/charts/linechart.tsx")), 'mantine/charts', true)
    registerComponent('DonutChart', '', lazy(() => import("../../fragments/mantine/charts/donutchart.tsx")), 'mantine/charts', true)
    registerComponent('RadarChart', '', lazy(() => import("../../fragments/mantine/charts/radarchart.tsx")), 'mantine/charts', true)
    registerComponent('AreaChart', '', lazy(() => import("../../fragments/mantine/charts/areachart.tsx")), 'mantine/charts', true)
    registerComponent('BarChart', '', lazy(() => import("../../fragments/mantine/charts/barchart.tsx")), 'mantine/charts', true)
    registerComponent('PieChart', '', lazy(() => import("../../fragments/mantine/charts/piechart.tsx")), 'mantine/charts', true)
  });
}