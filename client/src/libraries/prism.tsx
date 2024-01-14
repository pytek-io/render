import { registerComponent, registerModuleDeferred } from "../app";
const R = require("ramda");

const themeNames = [
  "dracula",
  "duotoneDark",
  "duotoneLight",
  "github",
  "nightOwl",
  "nightOwlLight",
  "oceanicNext",
  "okaidia",
  "palenight",
  "shadesOfPurple",
  "shadesOfPurple",
  "synthwave84",
  "ultramin",
  "vsDark",
  "vsLight",
];

export function register() {
  registerModuleDeferred("prism", async () => {
    const [prism_react, styled_components, themesDefintions] =
      await Promise.all([
        import("prism-react-renderer"),
        import("styled-components"),
        Promise.all(
          themeNames.map(
            (name) => import(`prism-react-renderer/themes/${name}`)
          )
        ),
      ]);
    const styled = styled_components.default;
    const themes = R.zipObj(themeNames, themesDefintions);
    const Highlight = prism_react.default;
    const defaultProps = prism_react.defaultProps;
    const Pre = styled.pre`
      text-align: left;
      margin: 1em 0;
      padding: 0.5em;
      overflow: scroll;
    `;

    const Line = styled.div`
      display: table-row;
    `;

    const LineNo = styled.span`
      display: table-cell;
      text-align: right;
      padding-right: 1em;
      user-select: none;
      opacity: 0.5;
    `;

    const LineContent = styled.span`
      display: table-cell;
    `;
    const wrapper = ({ code, language, theme, lineNumbers, style }) => {
      let actual_theme = null;
      if (theme) {
        actual_theme = themes[theme].default;
      }
      return (
        <Highlight
          {...defaultProps}
          code={code}
          language={language}
          theme={actual_theme}
        >
          {({
            className,
            default_style,
            tokens,
            getLineProps,
            getTokenProps,
          }) => {
            const actual_style = { ...default_style, ...style };
            return (
              <pre className={className} style={actual_style}>
                {tokens.map((line, i) => (
                  <Line key={i} {...getLineProps({ line, key: i })}>
                    {lineNumbers ? <LineNo>{i + 1}</LineNo> : null}
                    <LineContent>
                      {line.map((token, key) => (
                        <span key={key} {...getTokenProps({ token, key })} />
                      ))}
                    </LineContent>
                  </Line>
                ))}
              </pre>
            );
          }}
        </Highlight>
      );
    };
    registerComponent("PrismCodeFormatter", wrapper, "prism");
  });
}
