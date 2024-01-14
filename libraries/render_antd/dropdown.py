from render import Component, create_callback


class Dropdown(Component):
    Module = "ant"
    JSXName = "Dropdown"

    def __init__(
        self,
        children=None,
        key=None,
        style=None,
        className=None,
        id=None,
        onKeyPress=None,
        onClick=None,
        arrow=None,
        autoAdjustOverflow=None,
        autoFocus=None,
        destroyPopupOnHide=None,
        disabled=None,
        dropdownRender=None,
        getPopupContainer=None,
        menu=None,
        onOpenChange=None,
        open=None,
        overlayClassName=None,
        overlayStyle=None,
        placement=None,
        trigger=None,
        controller=None,
    ):
        super().__init__(key, controller)
        self.children = children
        self.style = style
        self.className = className
        self.id = id
        self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
        self.onClick = create_callback(onClick, "onClick")
        self.arrow = arrow
        self.autoAdjustOverflow = autoAdjustOverflow
        self.autoFocus = autoFocus
        self.destroyPopupOnHide = destroyPopupOnHide
        self.disabled = disabled
        self.dropdownRender = dropdownRender
        self.getPopupContainer = getPopupContainer
        self.menu = menu
        self.onOpenChange = create_callback(
            onOpenChange, "onOpenChange", [[0], [1, "source"]]
        )
        self.open = open
        self.overlayClassName = overlayClassName
        self.overlayStyle = overlayStyle
        self.placement = placement
        self.trigger = trigger


class DropdownButton(Component):
    Module = "ant"
    JSXName = "Dropdown.Button"

    def __init__(
        self,
        children=None,
        key=None,
        style=None,
        className=None,
        id=None,
        onKeyPress=None,
        onClick=None,
        arrow=None,
        autoAdjustOverflow=None,
        autoFocus=None,
        buttonsRender=None,
        danger=None,
        destroyPopupOnHide=None,
        disabled=None,
        dropdownRender=None,
        getPopupContainer=None,
        icon=None,
        loading=None,
        menu=None,
        onOpenChange=None,
        open=None,
        overlayClassName=None,
        overlayStyle=None,
        placement=None,
        size=None,
        trigger=None,
        type=None,
        controller=None,
    ):
        super().__init__(key, controller)
        self.children = children
        self.style = style
        self.className = className
        self.id = id
        self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
        self.onClick = create_callback(onClick, "onClick", [])
        self.arrow = arrow
        self.autoAdjustOverflow = autoAdjustOverflow
        self.autoFocus = autoFocus
        self.buttonsRender = buttonsRender
        self.danger = danger
        self.destroyPopupOnHide = destroyPopupOnHide
        self.disabled = disabled
        self.dropdownRender = dropdownRender
        self.getPopupContainer = getPopupContainer
        self.icon = icon
        self.loading = loading
        self.menu = menu
        self.onOpenChange = create_callback(
            onOpenChange, "onOpenChange", [[0], [1, "source"]]
        )
        self.open = open
        self.overlayClassName = overlayClassName
        self.overlayStyle = overlayStyle
        self.placement = placement
        self.size = size
        self.trigger = trigger
        self.type = type
