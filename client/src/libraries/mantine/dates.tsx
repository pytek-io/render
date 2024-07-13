/* AUTO GENERATED FILE - DO NOT EDIT! */

import { registerComponent, registerModuleDeferred, registerMethod } from "../../app";
import { lazy } from "react";
import '@mantine/core/styles.css';
import '@mantine/dates/styles.css';
export function register() {
  registerModuleDeferred("mantine/dates", async () => {
    registerComponent('MonthPicker', '', lazy(() => import("../../fragments/mantine/dates/monthpicker.tsx")), 'mantine/dates', true)
    registerComponent('DatePicker', '', lazy(() => import("../../fragments/mantine/dates/datepicker.tsx")), 'mantine/dates', true)
    registerComponent('DatesProvider', '', lazy(() => import("../../fragments/mantine/dates/datesprovider.tsx")), 'mantine/dates', true)
    registerComponent('DateTimePicker', '', lazy(() => import("../../fragments/mantine/dates/datetimepicker.tsx")), 'mantine/dates', true)
    registerComponent('TimeInput', '', lazy(() => import("../../fragments/mantine/dates/timeinput.tsx")), 'mantine/dates', true)
    registerComponent('YearPicker', '', lazy(() => import("../../fragments/mantine/dates/yearpicker.tsx")), 'mantine/dates', true)
    registerComponent('DateInput', '', lazy(() => import("../../fragments/mantine/dates/dateinput.tsx")), 'mantine/dates', true)
    registerComponent('Calendar', '', lazy(() => import("../../fragments/mantine/dates/calendar.tsx")), 'mantine/dates', true)
    registerComponent('MonthPicker', 'Input', lazy(() => import("../../fragments/mantine/dates/monthpicker_input.tsx")), 'mantine/dates', true)
    registerComponent('DatePicker', 'Input', lazy(() => import("../../fragments/mantine/dates/datepicker_input.tsx")), 'mantine/dates', true)
    registerComponent('YearPicker', 'Input', lazy(() => import("../../fragments/mantine/dates/yearpicker_input.tsx")), 'mantine/dates', true)
  });
}