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
        super().__init__(key, controller, children)
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
            "dependencies",
            "disabled",
            "extra",
            "feedbackIcons",
            "fields",
            "form",
            "getValueFromEvent",
            "getValueProps",
            "hasFeedback",
            "help",
            "hidden",
            "htmlFor",
            "initialValue",
            "initialValues",
            "label",
            "labelAlign",
            "labelCol",
            "labelWrap",
            "layout",
            "messageVariables",
            "name",
            "noStyle",
            "normalize",
            "preserve",
            "required",
            "requiredMark",
            "rules",
            "scrollToFirstError",
            "shouldUpdate",
            "size",
            "tooltip",
            "trigger",
            "validateDebounce",
            "validateFirst",
            "validateMessages",
            "validateStatus",
            "validateTrigger",
            "valuePropName",
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
            dependencies=None,
            disabled=None,
            extra=None,
            feedbackIcons=None,
            fields=None,
            form=None,
            getValueFromEvent=None,
            getValueProps=None,
            hasFeedback=None,
            help=None,
            hidden=None,
            htmlFor=None,
            initialValue=None,
            initialValues=None,
            label=None,
            labelAlign=None,
            labelCol=None,
            labelWrap=None,
            layout=None,
            messageVariables=None,
            name=None,
            noStyle=None,
            normalize=None,
            onFieldsChange=None,
            onFinish=None,
            onFinishFailed=None,
            onValuesChange=None,
            preserve=None,
            required=None,
            requiredMark=None,
            rules=None,
            scrollToFirstError=None,
            shouldUpdate=None,
            size=None,
            tooltip=None,
            trigger=None,
            validateDebounce=None,
            validateFirst=None,
            validateMessages=None,
            validateStatus=None,
            validateTrigger=None,
            valuePropName=None,
            variant=None,
            wrapperCol=None,
            controller=None,
        ):
            super().__init__(key, controller, children)
            self.style = style
            self.className = className
            self.id = id
            self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
            self.onClick = create_callback(onClick, "onClick")
            self.colon = colon
            self.component = component
            self.dependencies = dependencies
            self.disabled = disabled
            self.extra = extra
            self.feedbackIcons = feedbackIcons
            self.fields = fields
            self.form = form
            self.getValueFromEvent = getValueFromEvent
            self.getValueProps = getValueProps
            self.hasFeedback = hasFeedback
            self.help = help
            self.hidden = hidden
            self.htmlFor = htmlFor
            self.initialValue = initialValue
            self.initialValues = initialValues
            self.label = label
            self.labelAlign = labelAlign
            self.labelCol = labelCol
            self.labelWrap = labelWrap
            self.layout = layout
            self.messageVariables = messageVariables
            self.name = name
            self.noStyle = noStyle
            self.normalize = normalize
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
            self.required = required
            self.requiredMark = requiredMark
            self.rules = rules
            self.scrollToFirstError = scrollToFirstError
            self.shouldUpdate = shouldUpdate
            self.size = size
            self.tooltip = tooltip
            self.trigger = trigger
            self.validateDebounce = validateDebounce
            self.validateFirst = validateFirst
            self.validateMessages = validateMessages
            self.validateStatus = validateStatus
            self.validateTrigger = validateTrigger
            self.valuePropName = valuePropName
            self.variant = variant
            self.wrapperCol = wrapperCol

    class List(Component):
        Module = "antd"
        JSXName = "Form.List"
        CALLBACKS = [
            "onKeyPress",
            "onClick",
            "add",
            "move",
            "onFieldsChange",
            "onFinish",
            "onFinishFailed",
            "onValuesChange",
            "remove",
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
            "initialValue",
            "initialValues",
            "labelAlign",
            "labelCol",
            "labelWrap",
            "layout",
            "name",
            "preserve",
            "requiredMark",
            "rules",
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
            add=None,
            colon=None,
            component=None,
            disabled=None,
            feedbackIcons=None,
            fields=None,
            form=None,
            initialValue=None,
            initialValues=None,
            labelAlign=None,
            labelCol=None,
            labelWrap=None,
            layout=None,
            move=None,
            name=None,
            onFieldsChange=None,
            onFinish=None,
            onFinishFailed=None,
            onValuesChange=None,
            preserve=None,
            remove=None,
            requiredMark=None,
            rules=None,
            scrollToFirstError=None,
            size=None,
            validateMessages=None,
            validateTrigger=None,
            variant=None,
            wrapperCol=None,
            controller=None,
        ):
            super().__init__(key, controller, children)
            self.style = style
            self.className = className
            self.id = id
            self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
            self.onClick = create_callback(onClick, "onClick")
            self.add = create_callback(add, "add")
            self.colon = colon
            self.component = component
            self.disabled = disabled
            self.feedbackIcons = feedbackIcons
            self.fields = fields
            self.form = form
            self.initialValue = initialValue
            self.initialValues = initialValues
            self.labelAlign = labelAlign
            self.labelCol = labelCol
            self.labelWrap = labelWrap
            self.layout = layout
            self.move = create_callback(move, "move")
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
            self.remove = create_callback(remove, "remove")
            self.requiredMark = requiredMark
            self.rules = rules
            self.scrollToFirstError = scrollToFirstError
            self.size = size
            self.validateMessages = validateMessages
            self.validateTrigger = validateTrigger
            self.variant = variant
            self.wrapperCol = wrapperCol
