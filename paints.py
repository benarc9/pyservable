from skia import Paint, Color4f, ColorBLACK, ColorYELLOW


class ColoredFill(Paint):
    def __init__(self, color: Color4f = Color4f(0, 0, 0, 255)):
        super().__init__(color)


class ColorStroke(Paint):
    def __init__(self, color: Color4f = ColorBLACK):
        super().__init__(color)
        self.setStyle(Paint.kStroke_Style)


class ColorFillStroke(Paint):
    def __init__(self, color: Color4f = ColorYELLOW):
        super().__init__()
        self.setStyle(Paint.kStrokeAndFill_Style)
