from abc import ABC
import skia
from contextlib import contextmanager

class Drawable(ABC):
    def __init__(self, path: skia.Path, paint: skia.Paint):
        super(Drawable, self).__init__()
        self.path: skia.Path = path
        self.paint: skia.Paint = paint

    @contextmanager
    def draw(self, canvas: skia.Canvas):
        canvas.drawPath(self.path, self.paint)

    @property
    def paint(self) -> skia.Paint:
        return self._paint

    @paint.setter
    def paint(self, value: skia.Paint):
        self._paint = value

    @property
    def path(self) -> skia.Path:
        return self._path

    @path.setter
    def path(self, value: skia.Path):
        self._path = value