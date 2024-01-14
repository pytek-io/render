import { registerComponent, registerModuleDeferred } from "../app";


export function register() {
    const module_name = "tabler_icons";
    registerModuleDeferred(module_name, async () => {
      const tabler = (await import("@tabler/icons"));
      registerComponent("IconCheck", tabler.IconCheck, module_name);
      registerComponent("IconCookie", tabler.IconCookie, module_name);
      registerComponent("IconGauge", tabler.IconGauge, module_name);
      registerComponent("IconLock", tabler.IconLock, module_name);
      registerComponent("IconMessage2", tabler.IconMessage2, module_name);
      registerComponent("IconUser", tabler.IconUser, module_name);
      registerComponent("IconChevronDown", tabler.IconChevronDown, module_name);
      registerComponent("IconTimeline", tabler.IconTimeline, module_name);
      registerComponent("IconDeviceDesktop", tabler.IconDeviceDesktop, module_name);
      registerComponent("IconChartInfographic", tabler.IconChartInfographic, module_name);
      registerComponent("IconSettings", tabler.IconSettings, module_name);
      registerComponent("IconApps", tabler.IconApps, module_name);
      registerComponent("IconCloudComputing", tabler.IconCloudComputing, module_name);
      registerComponent("IconArrowLeft", tabler.IconArrowLeft, module_name);
      registerComponent("IconArrowRight", tabler.IconArrowRight, module_name);
      registerComponent("IconPuzzle2", tabler.IconPuzzle2, module_name);
      registerComponent("IconExternalLink", tabler.IconExternalLink, module_name);
    });
  }
