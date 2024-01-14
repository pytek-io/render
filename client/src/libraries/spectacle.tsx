import { registerModule, registerMethod, registerModuleDeferred } from "../app";

export function register() {
  registerModuleDeferred("spectacle", async () => {
    const module = await import("spectacle");
    const { FlexBox, Box, FullScreen, Progress } = module
    const template = () => (
      <FlexBox
        justifyContent="space-between"
        position="absolute"
        bottom={0}
        width={1}
      >
        <Box padding="0 1em">
          <FullScreen />
        </Box>
        <Box padding="1em">
          <Progress />
        </Box>
      </FlexBox>
    );
    registerMethod("presentation_template", template);
    registerModule("spectacle", module);
  });
}
