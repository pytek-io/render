from render import Component, InputComponent


class Swiper(InputComponent):
    Module = "swiper"
    NewValuePath = "activeIndex"
    ChangeEventName = "onSlideChange"
    InputName = None
    ATTRIBUTES = ["navigation", "lazy", "style"]
    CALLBACKS = ["onSlideChange"]

    def __init__(
        self,
        children=None,
        navigation=None,
        lazy=None,
        key=None,
        style=None,
        controller=None,
        onChange=None,
    ):
        super().__init__(key, controller, onChange, None, None)
        self.children = children
        self.navigation = navigation
        self.lazy = lazy
        self.style = style


class SwiperSlide(Component):
    Module = "swiper"
    ATTRIBUTES = []

    def __init__(
        self,
        children=None,
        key=None,
    ):
        super().__init__(key=key)
        self.children = children
