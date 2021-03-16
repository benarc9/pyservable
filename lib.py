import skia


class Vector:
    def __init__(self, x:float=0, y:float=0):
        self.x = x
        self.y = y

    def __str__(self):
        return str("({}, {})".format(self.x, self.y))

    @property
    def x(self) -> float:
        return self._x

    @x.setter
    def x(self, value:float):
        self._x = value


    @property
    def y(self) -> float:
        return self._y

    @y.setter
    def y(self, value:float):
        self._y = value

    def to_point(self) -> skia.Point:
        return skia.Point(self.x, self.y)