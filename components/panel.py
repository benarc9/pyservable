import skia

from components.component import Component
from lib import Vector


class Panel(Component):
    def __init__(self, origin: Vector, size: Vector, bg_color: skia.Color4f):
        self.size = size
        self.origin = origin
        self.path = skia.Path()
        self.rect = skia.Rect(origin.x,
                         origin.y + size.y,
                         origin.x + size.x,
                         origin.y)
        self.path.addRect(self.rect)
        super(Panel, self).__init__(self.path, skia.Paint(bg_color))

    @property
    def origin(self) -> Vector:
        return self._origin

    @origin.setter
    def origin(self, value: Vector):
        self._origin = value

    @property
    def size(self) -> Vector:
        return self._size

    @size.setter
    def size(self, value: Vector):
        self._size = value

    @property
    def rect(self) -> skia.Rect:
        return self._rect

    @rect.setter
    def rect(self, value: skia.Rect):
        self._rect = value

    @property
    def path(self) -> skia.Path:
        return self._path

    @path.setter
    def path(self, value: skia.Path):
        self._path = value

