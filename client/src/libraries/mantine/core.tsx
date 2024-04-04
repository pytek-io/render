import { registerComponents, registerModuleDeferred } from "../../app";
import { lazy } from "react";
import '@mantine/core/styles.css';
const components = [
  ['ColorInput', [], lazy(() => import("../../fragments/mantine/core/colorinput.tsx"))],
  ['Code', [], lazy(() => import("../../fragments/mantine/core/code.tsx"))],
  ['RangeSlider', [], lazy(() => import("../../fragments/mantine/core/rangeslider.tsx"))],
  ['Overlay', [], lazy(() => import("../../fragments/mantine/core/overlay.tsx"))],
  ['Autocomplete', [], lazy(() => import("../../fragments/mantine/core/autocomplete.tsx"))],
  ['Modal', ['sProvider'], lazy(() => import("../../fragments/mantine/core/modal.tsx"))],
  ['Switch', ['Group'], lazy(() => import("../../fragments/mantine/core/switch.tsx"))],
  ['HoverCard', ['Dropdown', 'Target'], lazy(() => import("../../fragments/mantine/core/hovercard.tsx"))],
  ['ComboboxDropdown', ['Target'], lazy(() => import("../../fragments/mantine/core/comboboxdropdown.tsx"))],
  ['Stack', [], lazy(() => import("../../fragments/mantine/core/stack.tsx"))],
  ['NavLink', [], lazy(() => import("../../fragments/mantine/core/navlink.tsx"))],
  ['Anchor', [], lazy(() => import("../../fragments/mantine/core/anchor.tsx"))],
  ['Drawer', [], lazy(() => import("../../fragments/mantine/core/drawer.tsx"))],
  ['Space', [], lazy(() => import("../../fragments/mantine/core/space.tsx"))],
  ['NumberInput', [], lazy(() => import("../../fragments/mantine/core/numberinput.tsx"))],
  ['Divider', [], lazy(() => import("../../fragments/mantine/core/divider.tsx"))],
  ['Collapse', [], lazy(() => import("../../fragments/mantine/core/collapse.tsx"))],
  ['Alert', [], lazy(() => import("../../fragments/mantine/core/alert.tsx"))],
  ['PillsInput', ['Field'], lazy(() => import("../../fragments/mantine/core/pillsinput.tsx"))],
  ['LoadingOverlay', [], lazy(() => import("../../fragments/mantine/core/loadingoverlay.tsx"))],
  ['ColorSwatch', [], lazy(() => import("../../fragments/mantine/core/colorswatch.tsx"))],
  ['FileInput', [], lazy(() => import("../../fragments/mantine/core/fileinput.tsx"))],
  ['VisuallyHidden', [], lazy(() => import("../../fragments/mantine/core/visuallyhidden.tsx"))],
  ['CopyButton', [], lazy(() => import("../../fragments/mantine/core/copybutton.tsx"))],
  ['Paper', [], lazy(() => import("../../fragments/mantine/core/paper.tsx"))],
  ['Slider', [], lazy(() => import("../../fragments/mantine/core/slider.tsx"))],
  ['Input', ['Description', 'Error', 'Label', 'Wrapper'], lazy(() => import("../../fragments/mantine/core/input.tsx"))],
  ['Tooltip', [], lazy(() => import("../../fragments/mantine/core/tooltip.tsx"))],
  ['Blockquote', [], lazy(() => import("../../fragments/mantine/core/blockquote.tsx"))],
  ['ThemeIcon', [], lazy(() => import("../../fragments/mantine/core/themeicon.tsx"))],
  ['Rating', [], lazy(() => import("../../fragments/mantine/core/rating.tsx"))],
  ['Fieldset', [], lazy(() => import("../../fragments/mantine/core/fieldset.tsx"))],
  ['TypographyStylesProvider', [], lazy(() => import("../../fragments/mantine/core/typographystylesprovider.tsx"))],
  ['Chip', ['Group'], lazy(() => import("../../fragments/mantine/core/chip.tsx"))],
  ['SimpleGrid', [], lazy(() => import("../../fragments/mantine/core/simplegrid.tsx"))],
  ['Loader', [], lazy(() => import("../../fragments/mantine/core/loader.tsx"))],
  ['RingProgress', [], lazy(() => import("../../fragments/mantine/core/ringprogress.tsx"))],
  ['Table', [], lazy(() => import("../../fragments/mantine/core/table.tsx"))],
  ['Indicator', [], lazy(() => import("../../fragments/mantine/core/indicator.tsx"))],
  ['Popover', ['Dropdown', 'Target'], lazy(() => import("../../fragments/mantine/core/popover.tsx"))],
  ['Flex', [], lazy(() => import("../../fragments/mantine/core/flex.tsx"))],
  ['Title', [], lazy(() => import("../../fragments/mantine/core/title.tsx"))],
  ['Progress', ['Root', 'Section'], lazy(() => import("../../fragments/mantine/core/progress.tsx"))],
  ['Avatar', [], lazy(() => import("../../fragments/mantine/core/avatar.tsx"))],
  ['Pill', ['Group', 'sInput'], lazy(() => import("../../fragments/mantine/core/pill.tsx"))],
  ['AspectRatio', [], lazy(() => import("../../fragments/mantine/core/aspectratio.tsx"))],
  ['Stepper', ['Step'], lazy(() => import("../../fragments/mantine/core/stepper.tsx"))],
  ['Tabs', ['List', 'Panel', 'Tab'], lazy(() => import("../../fragments/mantine/core/tabs.tsx"))],
  ['Skeleton', [], lazy(() => import("../../fragments/mantine/core/skeleton.tsx"))],
  ['Accordion', ['Chevron', 'Control', 'Item', 'Panel'], lazy(() => import("../../fragments/mantine/core/accordion.tsx"))],
  ['Textarea', [], lazy(() => import("../../fragments/mantine/core/textarea.tsx"))],
  ['List', ['Item'], lazy(() => import("../../fragments/mantine/core/list.tsx"))],
  ['MultiSelect', [], lazy(() => import("../../fragments/mantine/core/multiselect.tsx"))],
  ['TagsInput', [], lazy(() => import("../../fragments/mantine/core/tagsinput.tsx"))],
  ['Notification', ['s'], lazy(() => import("../../fragments/mantine/core/notification.tsx"))],
  ['Radio', ['Group'], lazy(() => import("../../fragments/mantine/core/radio.tsx"))],
  ['MantineProvider', [], lazy(() => import("../../fragments/mantine/core/mantineprovider.tsx"))],
  ['AppShell', ['Aside', 'Footer', 'Header', 'Main', 'Navbar', 'Section'], lazy(() => import("../../fragments/mantine/core/appshell.tsx"))],
  ['Spoiler', [], lazy(() => import("../../fragments/mantine/core/spoiler.tsx"))],
  ['NativeSelect', [], lazy(() => import("../../fragments/mantine/core/nativeselect.tsx"))],
  ['Checkbox', ['Group'], lazy(() => import("../../fragments/mantine/core/checkbox.tsx"))],
  ['Dialog', [], lazy(() => import("../../fragments/mantine/core/dialog.tsx"))],
  ['Container', [], lazy(() => import("../../fragments/mantine/core/container.tsx"))],
  ['FileButton', [], lazy(() => import("../../fragments/mantine/core/filebutton.tsx"))],
  ['Button', ['Group'], lazy(() => import("../../fragments/mantine/core/button.tsx"))],
  ['Burger', [], lazy(() => import("../../fragments/mantine/core/burger.tsx"))],
  ['Menu', ['Divider', 'Dropdown', 'Item', 'Label', 'Target'], lazy(() => import("../../fragments/mantine/core/menu.tsx"))],
  ['Breadcrumbs', [], lazy(() => import("../../fragments/mantine/core/breadcrumbs.tsx"))],
  ['Grid', ['Col'], lazy(() => import("../../fragments/mantine/core/grid.tsx"))],
  ['Timeline', ['Item'], lazy(() => import("../../fragments/mantine/core/timeline.tsx"))],
  ['Card', ['Section'], lazy(() => import("../../fragments/mantine/core/card.tsx"))],
  ['Affix', [], lazy(() => import("../../fragments/mantine/core/affix.tsx"))],
  ['BackgroundImage', [], lazy(() => import("../../fragments/mantine/core/backgroundimage.tsx"))],
  ['Portal', [], lazy(() => import("../../fragments/mantine/core/portal.tsx"))],
  ['Badge', [], lazy(() => import("../../fragments/mantine/core/badge.tsx"))],
  ['SegmentedControl', [], lazy(() => import("../../fragments/mantine/core/segmentedcontrol.tsx"))],
  ['ColorPicker', [], lazy(() => import("../../fragments/mantine/core/colorpicker.tsx"))],
  ['Text', [], lazy(() => import("../../fragments/mantine/core/text.tsx"))],
  ['Image', [], lazy(() => import("../../fragments/mantine/core/image.tsx"))],
  ['Center', [], lazy(() => import("../../fragments/mantine/core/center.tsx"))],
  ['Select', [], lazy(() => import("../../fragments/mantine/core/select.tsx"))],
  ['TextInput', [], lazy(() => import("../../fragments/mantine/core/textinput.tsx"))],
  ['ActionIcon', ['Group'], lazy(() => import("../../fragments/mantine/core/actionicon.tsx"))],
  ['PasswordInput', [], lazy(() => import("../../fragments/mantine/core/passwordinput.tsx"))],
  ['Transition', [], lazy(() => import("../../fragments/mantine/core/transition.tsx"))],
  ['Mark', [], lazy(() => import("../../fragments/mantine/core/mark.tsx"))],
  ['FocusTrap', ['InitialFocus'], lazy(() => import("../../fragments/mantine/core/focustrap.tsx"))],
  ['CloseButton', [], lazy(() => import("../../fragments/mantine/core/closebutton.tsx"))],
  ['Group', [], lazy(() => import("../../fragments/mantine/core/group.tsx"))],
  ['PinInput', [], lazy(() => import("../../fragments/mantine/core/pininput.tsx"))],
  ['ComboboxOption', ['s'], lazy(() => import("../../fragments/mantine/core/comboboxoption.tsx"))],
  ['Kbd', [], lazy(() => import("../../fragments/mantine/core/kbd.tsx"))],
  ['NumberFormatter', [], lazy(() => import("../../fragments/mantine/core/numberformatter.tsx"))],
  ['Combobox', ['Chevron', 'Dropdown', 'Empty', 'EventsTarget', 'Footer', 'Group', 'Header', 'Option', 'Search', 'Target'], lazy(() => import("../../fragments/mantine/core/combobox.tsx"))],
  ['JsonInput', [], lazy(() => import("../../fragments/mantine/core/jsoninput.tsx"))],
  ['ScrollArea', [], lazy(() => import("../../fragments/mantine/core/scrollarea.tsx"))],
  ['Highlight', [], lazy(() => import("../../fragments/mantine/core/highlight.tsx"))],
  ['Pagination', ['Control', 'Dots', 'First', 'Items', 'Last', 'Next', 'Previous', 'Root'], lazy(() => import("../../fragments/mantine/core/pagination.tsx"))],
  ['UnstyledButton', [], lazy(() => import("../../fragments/mantine/core/unstyledbutton.tsx"))],
];
export function register() {
  registerModuleDeferred("mantine/core", async () => {
    registerComponents(components, "mantine/core", true);
  });
}