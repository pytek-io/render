from render import Component, create_callback, Props


class Form(Component):
    Module = "antd"
    JSXName = "Form"
    CALLBACKS = [
        "onKeyPress",
        "onClick",
        "onFieldsChange",
        "onFinish",
        "onFinishFailed",
        "onValuesChange",
    ]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
        "colon",
        "component",
        "disabled",
        "feedbackIcons",
        "fields",
        "form",
        "initialValues",
        "labelAlign",
        "labelCol",
        "labelWrap",
        "layout",
        "name",
        "preserve",
        "requiredMark",
        "scrollToFirstError",
        "size",
        "validateMessages",
        "validateTrigger",
        "variant",
        "wrapperCol",
    ]

    def __init__(
        self,
        children=None,
        key=None,
        style=None,
        className=None,
        id=None,
        onKeyPress=None,
        onClick=None,
        colon=None,
        component=None,
        disabled=None,
        feedbackIcons=None,
        fields=None,
        form=None,
        initialValues=None,
        labelAlign=None,
        labelCol=None,
        labelWrap=None,
        layout=None,
        name=None,
        onFieldsChange=None,
        onFinish=None,
        onFinishFailed=None,
        onValuesChange=None,
        preserve=None,
        requiredMark=None,
        scrollToFirstError=None,
        size=None,
        validateMessages=None,
        validateTrigger=None,
        variant=None,
        wrapperCol=None,
        controller=None,
    ):
        super().__init__(key, controller)
        self.children = children
        self.style = style
        self.className = className
        self.id = id
        self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
        self.onClick = create_callback(onClick, "onClick")
        self.colon = colon
        self.component = component
        self.disabled = disabled
        self.feedbackIcons = feedbackIcons
        self.fields = fields
        self.form = form
        self.initialValues = initialValues
        self.labelAlign = labelAlign
        self.labelCol = labelCol
        self.labelWrap = labelWrap
        self.layout = layout
        self.name = name
        self.onFieldsChange = create_callback(
            onFieldsChange, "onFieldsChange", [[0], [1]]
        )
        self.onFinish = create_callback(onFinish, "onFinish", [[0]])
        self.onFinishFailed = create_callback(
            onFinishFailed,
            "onFinishFailed",
            [[0, "values"], [0, "errorFields"], [0, "outOfDate"]],
        )
        self.onValuesChange = create_callback(
            onValuesChange, "onValuesChange", [[0], [1]]
        )
        self.preserve = preserve
        self.requiredMark = requiredMark
        self.scrollToFirstError = scrollToFirstError
        self.size = size
        self.validateMessages = validateMessages
        self.validateTrigger = validateTrigger
        self.variant = variant
        self.wrapperCol = wrapperCol

    class Item(Component):
        Module = "antd"
        JSXName = "Form.Item"
        CALLBACKS = ["onKeyPress", "onClick"]
        ATTRIBUTES = [
            "style",
            "className",
            "id",
            "colon",
            "dependencies",
            "extra",
            "getValueFromEvent",
            "getValueProps",
            "hasFeedback",
            "help",
            "hidden",
            "htmlFor",
            "initialValue",
            "label",
            "labelAlign",
            "labelCol",
            "messageVariables",
            "name",
            "noStyle",
            "normalize",
            "preserve",
            "required",
            "rules",
            "shouldUpdate",
            "tooltip",
            "trigger",
            "validateDebounce",
            "validateFirst",
            "validateStatus",
            "validateTrigger",
            "valuePropName",
            "wrapperCol",
        ]

        def __init__(
            self,
            children=None,
            key=None,
            style=None,
            className=None,
            id=None,
            onKeyPress=None,
            onClick=None,
            colon=None,
            dependencies=None,
            extra=None,
            getValueFromEvent=None,
            getValueProps=None,
            hasFeedback=None,
            help=None,
            hidden=None,
            htmlFor=None,
            initialValue=None,
            label=None,
            labelAlign=None,
            labelCol=None,
            messageVariables=None,
            name=None,
            noStyle=None,
            normalize=None,
            preserve=None,
            required=None,
            rules=None,
            shouldUpdate=None,
            tooltip=None,
            trigger=None,
            validateDebounce=None,
            validateFirst=None,
            validateStatus=None,
            validateTrigger=None,
            valuePropName=None,
            wrapperCol=None,
            controller=None,
        ):
            super().__init__(key, controller)
            self.children = children
            self.style = style
            self.className = className
            self.id = id
            self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
            self.onClick = create_callback(onClick, "onClick")
            self.colon = colon
            self.dependencies = dependencies
            self.extra = extra
            self.getValueFromEvent = getValueFromEvent
            self.getValueProps = getValueProps
            self.hasFeedback = hasFeedback
            self.help = help
            self.hidden = hidden
            self.htmlFor = htmlFor
            self.initialValue = initialValue
            self.label = label
            self.labelAlign = labelAlign
            self.labelCol = labelCol
            self.messageVariables = messageVariables
            self.name = name
            self.noStyle = noStyle
            self.normalize = normalize
            self.preserve = preserve
            self.required = required
            self.rules = rules
            self.shouldUpdate = shouldUpdate
            self.tooltip = tooltip
            self.trigger = trigger
            self.validateDebounce = validateDebounce
            self.validateFirst = validateFirst
            self.validateStatus = validateStatus
            self.validateTrigger = validateTrigger
            self.valuePropName = valuePropName
            self.wrapperCol = wrapperCol

    class List(Component):
        Module = "antd"
        JSXName = "Form.List"
        CALLBACKS = ["onKeyPress", "onClick", "add", "move", "remove"]
        ATTRIBUTES = ["style", "className", "id", "initialValue", "name", "rules"]

        def __init__(
            self,
            children=None,
            key=None,
            style=None,
            className=None,
            id=None,
            onKeyPress=None,
            onClick=None,
            add=None,
            initialValue=None,
            move=None,
            name=None,
            remove=None,
            rules=None,
            controller=None,
        ):
            super().__init__(key, controller)
            self.children = children
            self.style = style
            self.className = className
            self.id = id
            self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
            self.onClick = create_callback(onClick, "onClick")
            self.add = create_callback(add, "add")
            self.initialValue = initialValue
            self.move = create_callback(move, "move")
            self.name = name
            self.remove = create_callback(remove, "remove")
            self.rules = rules
