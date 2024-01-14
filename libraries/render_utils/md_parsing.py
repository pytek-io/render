import ast
import os
from itertools import count
from sys import prefix

from mistletoe import Document, block_token, span_token
from render_antd import Table, Tabs, Typography
from render_html import a, blockquote, br, div, em, img, li, ul
from render_prism import PrismCodeFormatter
from render_utils.common import load_module

from render.utils import decode_url, maybe_prefixed_content


LANGUAGES = {"py": "python", "md": "markdown", "css": "css"}
STYLE_START = "<style>"
STYLE_END = "</style>"
INTRINSIC_TYPES = {
    "string": "str",
    "boolean": "bool",
    "undefined": "None",
    "number": "int",  # or float?
    "null": "None",
}
COMPONENT_COUNTER = count()


def monaco_language_from_extension(file_name):
    extension = file_name.rsplit(".", 1)[-1]
    return LANGUAGES.get(extension, "python")


def find_python_file_path(command):
    command = command.replace(".", os.sep)
    for end in (".py", os.sep + "__init__.py"):
        if os.path.exists(command + end):
            command += end
            break
    return command


def extract_file_path_and_language(command):
    language = monaco_language_from_extension(command)
    if language == "python" and not command.endswith(".py"):
        command = find_python_file_path(command)
    return command, language


def code_box_demo(module_path, language=None):
    file_path, _hash_argument = decode_url(module_path)
    actual_file_path, language = extract_file_path_and_language(file_path)
    language = language or monaco_language_from_extension(file_path)
    return PrismCodeFormatter(code=open(actual_file_path).read(), language=language)


def end_of_doc_string_module(code):
    body = ast.parse(code).body
    return body[0].lineno if body and isinstance(body[0], ast.Expr) else 0


def code_module_box_demo(module_path):
    file_path, _hash_argument = decode_url(module_path)
    if not file_path.endswith(".py"):
        file_path = file_path.replace(".", "/") + ".py"
    code = open(file_path).read()
    code = "\n".join(list(code.split("\n"))[end_of_doc_string_module(code) :])
    return PrismCodeFormatter(code, language="python")


def enclose(left, content, right=None):
    return f"{left}{content}{right or left}"


def parse_argument_type(argument_type):
    argument_type = normalize_react_component_name(argument_type)
    python_type = INTRINSIC_TYPES.get(argument_type, None)
    if python_type:
        return python_type
    if "|" in argument_type:
        return enclose(
            "[",
            ", ".join(enclose('"', value.strip()) for value in argument_type.split("|")),
            "]",
        )
    elif argument_type.startswith("function"):
        return "Callable[[], None]"
    return argument_type


def replace_weird_escaped_pipes(description):
    return description.replace(" \\| ", " ") if description else ""


def normalize_react_component_name(name):
    if not name:
        return "null"
    return ("React." if "React" in name and not name.startswith("React.") else "") + name


def substring_index(text, substring, start):
    result = text.find(substring, start)
    return result if result != -1 else None


def extract_style_definitions(text):
    start, styles, content = 0, "", ""
    while True:
        next_style_start = substring_index(text, STYLE_START, start)
        if not next_style_start:
            break
        next_style_end = substring_index(text, STYLE_END, next_style_start)
        if not next_style_end:
            break
        styles += text[next_style_start + len(STYLE_START) : next_style_end]
        content += text[start:next_style_start]
        start = next_style_end + len(STYLE_END)
    content += text[start:]
    return styles, content


def render_heading(token: block_token.Heading):
    return Typography.Title(render_children(token), level=token.level)


def render_setext_heading(token: block_token.SetextHeading):
    return div(render_children(token), style={"paddingBottom": 30})


def render_ignore(token):
    pass


def render_thematic_break(token):
    return br()


def render_link(token: span_token.Link):
    href, download, target = token.target, None, None
    maybe_href = maybe_prefixed_content("internal:", href)
    if maybe_href:
        href = "#" + maybe_href
    else:
        download_address = maybe_prefixed_content("download:", href)
        if download_address:
            href, download = download_address, True
        else:
            target = "_blank"
    return a(
        token.title or render_children(token),
        href=href,
        download=download,
        target=target,
        key=href,
    )


def render_image(token: span_token.Image):
    return img(
        src=token.src,
        alt=token.children[0].content if token.children else None,
        className="markdown-inline-image",
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


def render_autolink(token: span_token.AutoLink):
    assert token.children[0].content
    return a(token.children[0].content, target=token.target)


def render_raw_text(token: span_token.RawText):
    return token.content


def render_line_break(_token: span_token.LineBreak):
    return br()


current_tabs = []


def render_code_fence(token: block_token.CodeFence):
    code_or_file_path = render_as_text(token)
    # removing trailing empty line as it usually takes up space unnecessarily
    if code_or_file_path.endswith("\n"):
        code_or_file_path = code_or_file_path[:-1]
    language = token.language
    if language == "read_file":
        return code_box_demo(code_or_file_path)
    if language == "read_module":
        return code_module_box_demo(code_or_file_path)
    if language.startswith("tab"):
        global current_tabs
        tag, tab = [x.strip() for x in language.split(":")]
        assert tab, "not tab name found, you should probably remove some space around :"
        assert tag != "tab_start" or not current_tabs
        current_tabs.append(
            Tabs.TabPane(
                PrismCodeFormatter(language="text", code=code_or_file_path, theme="github"),
                tab=tab,
                key=tab,
            )
        )
        if tag == "tab_end":
            current_tabs, tabs = [], current_tabs
            return Tabs(tabs)
        else:
            return None
    if language.startswith("load_module"):
        return div(
            load_module(code_or_file_path),
            style=None
            if language.endswith("no_frame")
            else {
                "borderColor": "#848689",
                "borderStyle": "dashed",
                "borderWidth": "thin",
                "padding": "10px",
                "margin": "16px 0",
            },
        )
    return PrismCodeFormatter(language=token.language, code=code_or_file_path, theme="github")


def generic_container_renderer(component):
    """This will generate component with unique keys"""

    def result(token):
        return component(render_children(token), key=next(COMPONENT_COUNTER))

    return result


TYPES = ["success", "secondary", "warning", "danger"]
ATTRIBUTES = ["disabled", "mark", "keyboard", "underline", "delete"]


def ant_text(**kwargs):
    def result(text, key=None):
        return Typography.Text(text, key=key, **kwargs)

    return result


def paragraph_formatter(text, key):
    return Typography.Paragraph(text, key=key)


def extended_typography(text, key):
    maybe_type = next(
        (prefix for prefix in TYPES + ATTRIBUTES if text[0].startswith(f":{prefix}:")),
        None,
    )
    if maybe_type:
        kwargs = {"type": maybe_type} if prefix in TYPES else {maybe_type: True}
        return Typography.Text([text[0][len(maybe_type) + 2 :]] + text[1:], key=key, **kwargs)
    return Typography.Text(text, key=key, code=True)


containers = {
    block_token.ListItem: li,
    block_token.List: ul,
    span_token.InlineCode: extended_typography,
    block_token.Paragraph: paragraph_formatter,
    span_token.Strong: ant_text(strong=True),
    block_token.Quote: blockquote,
    span_token.Emphasis: em,
}


def render_as_text(token):
    for name in ["target", "content"]:
        attribute = getattr(token, name, None)
        if attribute is not None:
            return attribute
    return "".join(map(render_as_text, token.children))


class BaseRenderer:
    def __init__(self) -> None:
        self.component_counter = count(100)  # starting at 100 to avoid clashes
        self.renderers = {
            token_type: generic_container_renderer(component_type)
            for token_type, component_type in containers.items()
        }
        self.renderers.update(
            {
                block_token.Table: self.render_table,
                block_token.SetextHeading: render_setext_heading,
                block_token.Heading: render_heading,
                block_token.ThematicBreak: render_thematic_break,
                span_token.RawText: render_raw_text,
                span_token.LineBreak: render_line_break,
                block_token.CodeFence: render_code_fence,
                block_token.BlockCode: render_code_fence,
                span_token.Link: render_link,
                span_token.Image: render_image,
                block_token.span_token.AutoLink: render_autolink,
                span_token.EscapeSequence: render_ignore,
            }
        )

    def render(self, token):
        method = getattr(self, f"render_{type(token).__name__}", None)
        if method:
            return method(token)
        if type(token) in containers:
            return self.render_container(token)
        return self.renderers[type(token)](token)

    def render_container(self, token):
        return containers[type(token)](
            self.render_children(token), key=next(self.component_counter)
        )

    def render_children(self, token):
        return [self.render(child) for child in token.children]

    def render_table(self, token: block_token.Table):
        columns, dataSource = self.parse_table(token)
        for i, row in enumerate(dataSource):
            if "key" not in row:
                row["key"] = str(i)
        return Table(columns=columns, dataSource=dataSource, pagination=False)

    def parse_table(self, token: block_token.Table):
        titles = [render_as_text(header) for header in token.header.children]
        columns = [{"title": title, "dataIndex": title} for title in titles]
        dataSource = [
            {name: self.render_children(element) for name, element in zip(titles, row.children)}
            for row in token.children
        ]
        return columns, dataSource


def render_node(token):
    return BaseRenderer().render(token)


arguments_name = ["description", "argument_type", "default_value"]
expected_titles = ["Description", "Type", "Default"]


def render_fail(token: span_token.EscapeSequence):
    raise Exception(token.children[0].content)


def render_children(node):
    renderer = BaseRenderer()
    return list(filter(None, (renderer.render(child) for child in node.children)))


def parse_md_doc(source):
    return render_children(Document(source))
