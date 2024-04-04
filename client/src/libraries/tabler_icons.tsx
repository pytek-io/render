import { registerComponents, registerModuleDeferred } from "../app";


export function register() {
  const module_name = "tabler_icons";
  registerModuleDeferred(module_name, async () => {
    const tabler = (await import("@tabler/icons"));
    const components = [
      ["IconCheck", [], tabler.IconCheck],
      ["IconCookie", [], tabler.IconCookie],
      ["IconGauge", [], tabler.IconGauge],
      ["IconLock", [], tabler.IconLock],
      ["IconMessage2", [], tabler.IconMessage2],
      ["IconUser", [], tabler.IconUser],
      ["IconChevronDown", [], tabler.IconChevronDown],
      ["IconTimeline", [], tabler.IconTimeline],
      ["IconDeviceDesktop", [], tabler.IconDeviceDesktop],
      ["IconChartInfographic", [], tabler.IconChartInfographic],
      ["IconSettings", [], tabler.IconSettings],
      ["IconApps", [], tabler.IconApps],
      ["IconCloudComputing", [], tabler.IconCloudComputing],
      ["IconArrowLeft", [], tabler.IconArrowLeft],
      ["IconArrowRight", [], tabler.IconArrowRight],
      ["IconPuzzle2", [], tabler.IconPuzzle2],
      ["IconExternalLink", [], tabler.IconExternalLink],
    ];
    registerComponents(components, module_name, false);
  });
}
