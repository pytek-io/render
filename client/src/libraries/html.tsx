import { registerComponent } from "../app";

export function register() {
  const tags = [
    "ul",
    "ol",
    "li",
    "p",
    "i",
    "a",
    "b",
    "u",
    "br",
    "h1",
    "h2",
    "h3",
    "h4",
    "h5",
    "h6",
    "hr",
    "th",
    "td",
    "tr",
    "div",
    "pre",
    "iframe",
    "img",
    "svg",
    "code",
    "circle",
    "html",
    "body",
    "span",
    "head",
    "path",
    "label",
    "Link",
    "thead",
    "tbody",
    "style",
    "header",
    "strong",
    "article",
    "em",
    "section",
    "blockquote",
  ];
  for (const tag of tags) {
    registerComponent(tag, "", tag, "html", false);
  }

  // rmk: we should factor out this code...
  function inline_svg(args) {
    const image = args["children"];
    return (
      <div>
        <img src={`data:image/svg+xml;utf8,${encodeURIComponent(image)}`} />
      </div>
    );
  }
  registerComponent("inline_svg", "", inline_svg, "html");

  function inline_png(args) {
    const image = args["children"];
    return (
      <div>
        <img src={`data:image/png;base64,${encodeURIComponent(image)}`} />
      </div>
    );
  }
  registerComponent("inline_png", "", inline_png, "html");
}
