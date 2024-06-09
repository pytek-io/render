from render import Component, create_callback, Props


class Carousel(Component):
    Module = "mantine/carousel"
    JSXName = "Carousel"
    CALLBACKS = [
        "onKeyPress",
        "onClick",
        "getEmblaApi",
        "onNextSlide",
        "onPreviousSlide",
        "onSlideChange",
    ]
    ATTRIBUTES = [
        "style",
        "className",
        "id",
        "align",
        "component",
        "containScroll",
        "controlSize",
        "controlsOffset",
        "dragFree",
        "draggable",
        "h",
        "height",
        "href",
        "inViewThreshold",
        "includeGapInSize",
        "initialSlide",
        "loop",
        "m",
        "mb",
        "me",
        "ml",
        "mr",
        "ms",
        "mt",
        "mx",
        "my",
        "nextControlIcon",
        "nextControlProps",
        "orientation",
        "p",
        "pb",
        "pe",
        "pl",
        "plugins",
        "pr",
        "previousControlIcon",
        "previousControlProps",
        "ps",
        "pt",
        "px",
        "py",
        "skipSnaps",
        "slideGap",
        "slideSize",
        "slidesToScroll",
        "speed",
        "sx",
        "ta",
        "target",
        "title",
        "variant",
        "withControls",
        "withIndicators",
        "withKeyboardEvents",
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
        align=None,
        component=None,
        containScroll=None,
        controlSize=None,
        controlsOffset=None,
        dragFree=None,
        draggable=None,
        getEmblaApi=None,
        h=None,
        height=None,
        href=None,
        inViewThreshold=None,
        includeGapInSize=None,
        initialSlide=None,
        loop=None,
        m=None,
        mb=None,
        me=None,
        ml=None,
        mr=None,
        ms=None,
        mt=None,
        mx=None,
        my=None,
        nextControlIcon=None,
        nextControlProps=None,
        onNextSlide=None,
        onPreviousSlide=None,
        onSlideChange=None,
        orientation=None,
        p=None,
        pb=None,
        pe=None,
        pl=None,
        plugins=None,
        pr=None,
        previousControlIcon=None,
        previousControlProps=None,
        ps=None,
        pt=None,
        px=None,
        py=None,
        skipSnaps=None,
        slideGap=None,
        slideSize=None,
        slidesToScroll=None,
        speed=None,
        sx=None,
        ta=None,
        target=None,
        title=None,
        variant=None,
        withControls=None,
        withIndicators=None,
        withKeyboardEvents=None,
        controller=None,
    ):
        super().__init__(key, controller, children)
        self.style = style
        self.className = className
        self.id = id
        self.onKeyPress = create_callback(onKeyPress, "onKeyPress")
        self.onClick = create_callback(onClick, "onClick")
        self.align = align
        self.component = component
        self.containScroll = containScroll
        self.controlSize = controlSize
        self.controlsOffset = controlsOffset
        self.dragFree = dragFree
        self.draggable = draggable
        self.getEmblaApi = create_callback(getEmblaApi, "getEmblaApi")
        self.h = h
        self.height = height
        self.href = href
        self.inViewThreshold = inViewThreshold
        self.includeGapInSize = includeGapInSize
        self.initialSlide = initialSlide
        self.loop = loop
        self.m = m
        self.mb = mb
        self.me = me
        self.ml = ml
        self.mr = mr
        self.ms = ms
        self.mt = mt
        self.mx = mx
        self.my = my
        self.nextControlIcon = nextControlIcon
        self.nextControlProps = nextControlProps
        self.onNextSlide = create_callback(onNextSlide, "onNextSlide")
        self.onPreviousSlide = create_callback(onPreviousSlide, "onPreviousSlide")
        self.onSlideChange = create_callback(onSlideChange, "onSlideChange")
        self.orientation = orientation
        self.p = p
        self.pb = pb
        self.pe = pe
        self.pl = pl
        self.plugins = plugins
        self.pr = pr
        self.previousControlIcon = previousControlIcon
        self.previousControlProps = previousControlProps
        self.ps = ps
        self.pt = pt
        self.px = px
        self.py = py
        self.skipSnaps = skipSnaps
        self.slideGap = slideGap
        self.slideSize = slideSize
        self.slidesToScroll = slidesToScroll
        self.speed = speed
        self.sx = sx
        self.ta = ta
        self.target = target
        self.title = title
        self.variant = variant
        self.withControls = withControls
        self.withIndicators = withIndicators
        self.withKeyboardEvents = withKeyboardEvents
