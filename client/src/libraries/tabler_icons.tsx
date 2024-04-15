import { registerComponents, registerModuleDeferred } from "../app";


export function register() {
  const module_name = "tabler_icons";
  registerModuleDeferred(module_name, async () => {
    const tabler = (await import("@tabler/icons"));
    const components = [
      ["IconCheck", [], tabler.IconCheck, false],
      ["IconCookie", [], tabler.IconCookie, false],
      ["IconGauge", [], tabler.IconGauge, false],
      ["IconLock", [], tabler.IconLock, false],
      ["IconMessage2", [], tabler.IconMessage2, false],
      ["IconUser", [], tabler.IconUser, false],
      ["IconChevronDown", [], tabler.IconChevronDown, false],
      ["IconTimeline", [], tabler.IconTimeline, false],
      ["IconDeviceDesktop", [], tabler.IconDeviceDesktop, false],
      ["IconChartInfographic", [], tabler.IconChartInfographic, false],
      ["IconSettings", [], tabler.IconSettings, false],
      ["IconApps", [], tabler.IconApps, false],
      ["IconCloudComputing", [], tabler.IconCloudComputing, false],
      ["IconArrowLeft", [], tabler.IconArrowLeft, false],
      ["IconArrowRight", [], tabler.IconArrowRight, false],
      ["IconPuzzle2", [], tabler.IconPuzzle2, false],
      ["IconExternalLink", [], tabler.IconExternalLink, false],
    ];
    registerComponents(components, module_name, false);
  });
}
