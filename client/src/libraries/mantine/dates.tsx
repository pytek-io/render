import { registerComponents, registerModuleDeferred } from "../../app";
import { lazy } from "react";
import '@mantine/core/styles.css';
import '@mantine/dates/styles.css';
const components = [
  ['MonthPicker', ['Input'], lazy(() => import("../../fragments/mantine/dates/monthpicker.tsx"))],
  ['DatePicker', ['Input'], lazy(() => import("../../fragments/mantine/dates/datepicker.tsx"))],
  ['DatesProvider', [], lazy(() => import("../../fragments/mantine/dates/datesprovider.tsx"))],
  ['DateTimePicker', [], lazy(() => import("../../fragments/mantine/dates/datetimepicker.tsx"))],
  ['TimeInput', [], lazy(() => import("../../fragments/mantine/dates/timeinput.tsx"))],
  ['YearPicker', ['Input'], lazy(() => import("../../fragments/mantine/dates/yearpicker.tsx"))],
  ['DateInput', [], lazy(() => import("../../fragments/mantine/dates/dateinput.tsx"))],
  ['Calendar', [], lazy(() => import("../../fragments/mantine/dates/calendar.tsx"))],
];
export function register() {
  registerModuleDeferred("mantine/dates", async () => {
    registerComponents(components, "mantine/dates", true);
  });
}