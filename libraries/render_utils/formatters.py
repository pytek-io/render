from render import js_arrow

apply_to_value = js_arrow(
    "apply_value",
    "(method, {value}) => value != undefined ? method(value) : value",
)

transform_if_number = js_arrow(
    "transform_if_number",
    """(method, {value}) => typeof value == "number" ? method(value) : value""",
)

compose = js_arrow(
    "compose",
    "(method1, method2, value) => method2(method1(value))",
)

_replace_value_with = js_arrow(
    "blank_if_zero",
    "(method, value_to_replace, replace_value, value) => value_to_replace ? replace_value : method(value)",
)


def replace_value(method, value=0, replace_value=""):
    return _replace_value_with(method, value, replace_value)


filesize = js_arrow("filesize", "value => window.filesize(value)")

pythonTimeStampToJSDate = js_arrow(
    "pythonTimeStampFormatter", "value => new Date(value * 1000)"
)

timeStampToJSDate = js_arrow("pythonTimeStampFormatter", "value => new Date(value)")

durationFormatter = js_arrow(
    "durationFormatter",
    """value => {
    var seconds = value / 1000;
    var result = ""
    var interval = Math.floor(seconds / 31536000);
    if (interval > 1) {
      result = interval + " years";
      seconds = seconds - interval * 31536000;
    }
    interval = Math.floor(seconds / 2592000);
    if (interval > 1) {
      result = `${result}, ${interval} months`;
      seconds = seconds - interval * 2592000;
    }
    interval = Math.floor(seconds / 86400);
    if (interval > 1) {
      result = `${result}, ${interval} days`;
      seconds = seconds - interval * 86400;
    }
    interval = Math.floor(seconds / 3600);
    if (interval > 1) {
      result = `${result}, ${interval} hours`;
      seconds = seconds - interval * 3600;
    }
    interval = Math.floor(seconds / 60);
    if (interval > 1) {
      result = `${result}, ${interval} minutes`;
      seconds = seconds - interval * 60;
    }
    if (interval > 1) { 
      result = `${result}, ${interval} seconds`;
    }
    return result;
  }""",
)

toLocaleTimeString = js_arrow(
    "toLocaleTimeString", "value => value.toLocaleTimeString()"
)
toLocaleDateString = js_arrow(
    "toLocaleDateString", "value => value.toLocaleDateString()"
)
toLocaleString = js_arrow("toLocaleString", "value => value.toLocaleString()")
boolToString = js_arrow("boolToString", "value => `${value}`")
numeral = js_arrow("numeral.format", "value => window.numeral(value).format()")
percentage = js_arrow("numeral.format", "value => value * 100")
amount_formatter = js_arrow(
    "amount_formatter",
    '({value}) => `${value.value}`.replace(/\\B(?=(\\d{3})+(?!\\d))/g, ",")',
)
percent_formatter = js_arrow(
    "percent_formatter", "value => `${(value * 100.0).toFixed(2)}%`"
)
percent_formatter_col = transform_if_number(percent_formatter)
round_value = js_arrow("round_value", "(nb_digits, value) => value.toFixed(nb_digits)")
round_value_to_2_digits = round_value(2)
round_value_to_2_digits_col = transform_if_number(round_value_to_2_digits)
maximumSignificantDigits = js_arrow(
    "maximumSignificantDigits",
    "(nb_digits, value) => new Intl.NumberFormat('en-IN', { maximumSignificantDigits: nb_digits}).format(value)",
)
hexadecimalFormatter = js_arrow(
    "hexadecimalFormatter", "value => value.toString(16)"
)
colorCellNumber = js_arrow(
    "colorCellNumber", "({value}) => ({color: value > 0.0 ? 'green' : 'red'})"
)
get_attribute = js_arrow("get_attribute", "(attribute, object) => object[attribute]")
constant = js_arrow("constant", "(value, _) => value")