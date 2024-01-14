import render_html as html

ERROR_STACK = ["This will be updated at runtime"]


def app(_):
    return html.div(html.p(line) for line in ERROR_STACK)
