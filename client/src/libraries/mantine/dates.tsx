import { registerComponents, registerModuleDeferred } from "../../app";
import { lazy } from "react";
const components = [
  ["MonthPicker", lazy(() => import("../../fragments/mantine/dates/monthpicker.tsx"))],
  ["MonthPicker.Input", lazy(() => import("../../fragments/mantine/dates/monthpicker_input.tsx"))],
  ["DatePicker", lazy(() => import("../../fragments/mantine/dates/datepicker.tsx"))],
  ["DatePicker.Input", lazy(() => import("../../fragments/mantine/dates/datepicker_input.tsx"))],
  ["DatesProvider", lazy(() => import("../../fragments/mantine/dates/datesprovider.tsx"))],
  ["DateTimePicker", lazy(() => import("../../fragments/mantine/dates/datetimepicker.tsx"))],
  ["TimeInput", lazy(() => import("../../fragments/mantine/dates/timeinput.tsx"))],
  ["YearPicker", lazy(() => import("../../fragments/mantine/dates/yearpicker.tsx"))],
  ["YearPicker.Input", lazy(() => import("../../fragments/mantine/dates/yearpicker_input.tsx"))],
  ["DateInput", lazy(() => import("../../fragments/mantine/dates/dateinput.tsx"))],
  ["Calendar", lazy(() => import("../../fragments/mantine/dates/calendar.tsx"))],
];
export function register() {
  registerModuleDeferred("mantine/dates", async () => {
    import('@mantine/dates/styles.css');
    registerComponents("mantine/dates", components, true);
  });
}