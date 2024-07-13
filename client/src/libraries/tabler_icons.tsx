import { registerComponent, registerModuleDeferred } from "../app";


export function register() {
  const module_name = "tabler_icons";
  registerModuleDeferred(module_name, async () => {
    const tabler = (await import("@tabler/icons"));
    registerComponent("IconCheck", "", tabler.IconCheck, module_name, false)
    registerComponent("IconCookie", "", tabler.IconCookie, module_name, false)
    registerComponent("IconGauge", "", tabler.IconGauge, module_name, false)
    registerComponent("IconLock", "", tabler.IconLock, module_name, false)
    registerComponent("IconMessage2", "", tabler.IconMessage2, module_name, false)
    registerComponent("IconUser", "", tabler.IconUser, module_name, false)
    registerComponent("IconChevronDown", "", tabler.IconChevronDown, module_name, false)
    registerComponent("IconTimeline", "", tabler.IconTimeline, module_name, false)
    registerComponent("IconDeviceDesktop", "", tabler.IconDeviceDesktop, module_name, false)
    registerComponent("IconChartInfographic", "", tabler.IconChartInfographic, module_name, false)
    registerComponent("IconSettings", "", tabler.IconSettings, module_name, false)
    registerComponent("IconApps", "", tabler.IconApps, module_name, false)
    registerComponent("IconCloudComputing", "", tabler.IconCloudComputing, module_name, false)
    registerComponent("IconArrowLeft", "", tabler.IconArrowLeft, module_name, false)
    registerComponent("IconArrowRight", "", tabler.IconArrowRight, module_name, false)
    registerComponent("IconPuzzle2", "", tabler.IconPuzzle2, module_name, false)
    registerComponent("IconExternalLink", "", tabler.IconExternalLink, module_name, false)
  });
}
