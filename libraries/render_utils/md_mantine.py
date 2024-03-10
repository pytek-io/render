import pathlib

import mistune
import render_html as html
import render_mantine.core as mantine
from mistune import AstRenderer, create_markdown
from mistune.directives import Directive
import render_mantine.code_highlight as code_highlight
from render_utils.common import load_module

from render.utils import decode_url, maybe_prefixed_content


def toc_plugin_patch(text, level, state):
    tid = "-".join(text.lower().split())
    state["toc_headings"].append(("#" + tid, text, level))
    return {"type": "theading", "text": text, "params": (level, tid)}


# patching mistune
mistune.directives.toc.record_toc_heading = toc_plugin_patch


def parse_link(link: str):
    href, download, target = link, None, None
    maybe_href = maybe_prefixed_content("internal:", href)
    if maybe_href:
        href = "#" + maybe_href
    else:
        download_address = maybe_prefixed_content("download:", href)
        if download_address:
            href, download = download_address, True
        else:
            target = "_blank"
    return href, download, target


class BaseDirective(Directive):
    directive_name: str

    def __call__(self, md):
        self.register_directive(md, self.directive_name)
        md.renderer.register(self.directive_name, lambda raw: self.render(**raw))


def remove_header_comment(code):
    return code[code.index('"""\n', 3) + 4 :] if code.startswith('"""') else code


class ExecBlock(BaseDirective):
    directive_name = "exec"

    def parse(self, block, m, state):
        options = dict(self.parse_options(m))
        return {
            "type": self.directive_name,
            "raw": {
                "module": m.group("value"),
                "prism": options.get("prism", "true") == "true",
                "load": options.get("load", "true") == "true",
            },
        }

    def render(self, module, prism, load):
        components = []
        if load:
            components.append(
                mantine.Paper(
                    mantine.Center(load_module(module)), withBorder=True, p="xl"
                )
            )
        if prism:
            file_path, _hash_argument = decode_url(module)
            if not file_path.endswith(".py"):
                file_path = file_path.replace(".", "/") + ".py"
            code = remove_header_comment(pathlib.Path(file_path).read_text())
            editor = code_highlight.CodeHighlight(
                code=code.replace("\n\n", "\n"), language="python", className="renderer-code"
            )
            components.append(editor)
        return mantine.Stack(
            components, 
            gap=15, 
            style={"marginBlockEnd": 16, "marginBlockStart": 16}
        )


EXTENSIONS = {"py": "python", "sh": "bash", "json": "json", "yaml": "yaml"}


class PrismBlock(BaseDirective):
    directive_name = "prism"

    def parse(self, block, m, state):
        options = dict(self.parse_options(m))
        file_path = m.group("value")
        return {
            "type": self.directive_name,
            "raw": {
                "file": file_path,
                "language": options.get("language")
                or EXTENSIONS.get(file_path.rsplit(".", 1)[-1], "text"),
            },
        }

    def render(self, file, language):
        return code_highlight.CodeHighlight(code=open(file).read(), language=language, mt=10, mb=10)


class MantineRenderer(AstRenderer):
    def heading(self, children, level):
        return mantine.Title(
            children[0],
            order=level,
            style={"marginBlockEnd": 16, "marginBlockStart": 28},
        )

    def thematic_break(self):
        return mantine.Divider()

    def block_quote(self, text):
        return mantine.Blockquote(text[0].children)

    def block_code(self, children, info=None):
        return mantine.Code(children)

    def newline(self):
        return

    def table(self, text):
        return mantine.Group(
            mantine.Paper(
                mantine.Table(text, highlightOnHover=True, withColumnBorders=True),
                withBorder=True,
            ),
            className="renderer-table",
            position="center",
            style={"paddingTop": 30},
        )

    def table_head(self, text):
        return html.thead(html.tr(text))

    def table_body(self, text):
        return html.tbody(text)

    def table_row(self, text):
        return html.tr(text)

    def table_cell(self, text, align=None, is_head=False):
        return html.th(text) if is_head else html.td(text)

    def paragraph(self, elements):
        return mantine.Text(elements, style={"fontSize": "14px"})

    def text(self, text):
        return text

    def block_text(self, text):
        return text

    def strong(self, text):
        return html.b(text[0])

    def emphasis(self, text):
        return html.em(text[0])

    def image(self, src, title, alt_text):
        return html.img(
            src=src,
            alt=alt_text,
            style={
                "display": "block",  # required for auto margins to work
                "marginLeft": "auto",
                "marginRight": "auto",
                "maxWidth": "100%",
                "maxHeight": "50vh",
                "marginTop": "16px",
                "marginBottom": "16px",
            },
        )

    def link(self, link, children=None, _title=None):
        href, _download, target = parse_link(link)
        return mantine.Anchor(
            children,
            href=href,
            target=target,
            underline=False,
            className="renderer-anchor",
        )

    def codespan(self, text):
        return mantine.Code(text, block=False, style={"fontSize": "inherit"})

    def list(self, children, ordered, level, start=None):
        return mantine.List(
            children,
            type="ordered" if ordered else "unordered",
            spacing=5,
            size="sm",
            withPadding=True,
            className="renderer-list",
        )

    def list_item(self, children, level):
        return mantine.List.Item(children)


def parse(content):
    # , Admonition(), GalleryBlock(), DirectiveToc()],
    return create_markdown(
        renderer=MantineRenderer(), plugins=[ExecBlock(), PrismBlock(), "table"]
    )(content)
