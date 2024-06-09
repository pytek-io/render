import { registerComponents, registerModuleDeferred, registerMethod } from "../../app";
import { lazy } from "react";
import '@mantine/core/styles.css';
import '@mantine/dates/styles.css';
const components = [
  ['MonthPicker', '', lazy(() => import("../../fragments/mantine/dates/monthpicker.tsx")), true],
  ['DatePicker', '', lazy(() => import("../../fragments/mantine/dates/datepicker.tsx")), true],
  ['DatesProvider', '', lazy(() => import("../../fragments/mantine/dates/datesprovider.tsx")), true],
  ['DateTimePicker', '', lazy(() => import("../../fragments/mantine/dates/datetimepicker.tsx")), true],
  ['TimeInput', '', lazy(() => import("../../fragments/mantine/dates/timeinput.tsx")), true],
  ['YearPicker', '', lazy(() => import("../../fragments/mantine/dates/yearpicker.tsx")), true],
  ['DateInput', '', lazy(() => import("../../fragments/mantine/dates/dateinput.tsx")), true],
  ['Calendar', '', lazy(() => import("../../fragments/mantine/dates/calendar.tsx")), true],
  ['MonthPicker', 'Input', lazy(() => import("../../fragments/mantine/dates/monthpicker_input.tsx")), true],
  ['DatePicker', 'Input', lazy(() => import("../../fragments/mantine/dates/datepicker_input.tsx")), true],
  ['YearPicker', 'Input', lazy(() => import("../../fragments/mantine/dates/yearpicker_input.tsx")), true],
];
export function register() {
  registerModuleDeferred("mantine/dates", async () => {
    registerComponents(components, "mantine/dates");
  });
}