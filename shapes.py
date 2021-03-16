from typing import List
from lib import *
import abc


class Shape(abc.ABC):
    def __init__(self):
        pass

    @property
    def paint(self) -> skia.Paint:
        return self._paint

    @paint.setter
    def paint(self, value:skia.Paint):
        self._paint = value

    @property
    def path(self) -> skia.Path:
        return self._path

    @path.setter
    def path(self, value:skia.Path):
        self._path = value

    @abc.abstractmethod
    def draw(self, canvas):
        raise NotImplementedError("Draw method not implemented on shape")


class Triangle(Shape):
    def __init__(self, point1:Vector, point2:Vector, point3:Vector, color:skia.Color4f=skia.ColorYELLOW):
        super(Triangle, self).__init__()
        self.points = [point1.to_point(), point2.to_point(), point3.to_point()]
        self.path = skia.Path()
        self.path.addPoly(pts=[point1.to_point(), point2.to_point(), point3.to_point()], close=True)
        self.paint = skia.Paint(Color=color)

    @property
    def points(self) -> List[skia.Point]:
        return self._points

    @points.setter
    def points(self, value:List[skia.Point]):
        for point in value:
            print(point, "\n")
        self._points = value

    def draw(self, canvas):
        if canvas:
            canvas.drawPath(self.path, self.paint)


class Rect(Shape):
    def __init__(self, origin: Vector, size: Vector, color: skia.Color4f = skia.ColorBLUE):
        super(Rect, self).__init__()
        self.origin = origin
        self.size = size
        self.rect = skia.Rect(origin.x, origin.y, size.x, size.y)
        self.path = skia.Path()
        self.path.addRect(skia.Point(origin.x, origin.y),
                          skia.Point(origin.x, origin.y + size.y),
                          skia.Point())
        self.paint = skia.Paint(Color=color)

    def draw(self, canvas):
        canvas.drawRect(self.rect, self.paint)

    @property
    def origin(self):
        return self._origin

    @origin.setter
    def origin(self, value:Vector):
        self._origin = value

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value:Vector):
        self._size = value
        
    @property
    def rect(self):
        return self._rect

    @rect.setter
    def rect(self, value):
        self._rect = value