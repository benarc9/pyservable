import skia
from shapes import Shape


class Outline:
    def __init__(self, shape:Shape, width:float=2, color:skia.Color4f=skia.ColorBLACK):
        self.width = width
        self.paint = skia.Paint(Color = color,
                               Dither=True,
                               Style=skia.Paint.kStroke_Style,
                               StrokeWidth=width,
                               AntiAlias=True,
                                StrokeJoin=skia.Paint.kBevel_Join
                                )
        self.cap = skia.Paint.Cap()
        self.shape = shape
        self.path = shape.path
        
    @property
    def shape(self) -> Shape:
        return self._shape
    
    @shape.setter
    def shape(self, value:Shape):
        self._shape = value

    @property
    def path(self) -> skia.Path:
        return self._path

    @path.setter
    def path(self, value:skia.Path):
        self._path = value

    @property
    def paint(self) -> skia.Paint:
        return self._paint

    @paint.setter
    def paint(self, value:skia.Paint):
        self._paint = value

    @property
    def width(self) -> int:
        return self._width

    @width.setter
    def width(self, value:int):
        self._width = value