import { registerComponent, registerModuleDeferred } from "../app";

export function register() {
  registerModuleDeferred("monaco", async () => {
    const Editor = (await import("@monaco-editor/react")).default;
    class RelaxedTypeScriptEditor extends React.Component {
      render() {
        return (
          <Editor
            language="typescript"
            // https://stackoverflow.com/questions/47017753/monaco-editor-dynamically-resizable
            // automaticLayout={true}
            {...this.props}
          />
        );
      }
    }
    registerComponent("Editor", "", Editor, "monaco");
    registerComponent(
      "RelaxedTypeScriptEditor", "",
      RelaxedTypeScriptEditor,
      "monaco"
    );
  });
}
