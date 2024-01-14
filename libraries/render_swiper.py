from render import Component, InputComponent


class Swiper(InputComponent):
    Module = "swiper"
    NewValuePath = "activeIndex"
    ChangeEventName = "onSlideChange"
    InputName = None

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

    def __init__(
        self,
        children=None,
        desc=None,
    ):
        super().__init__(key=desc)
        self.children = children
