from abc import ABC

import skia

from components.drawable import Drawable


class Component(Drawable, ABC):
    def __init__(self, path: skia.Path, paint: skia.Paint):
        super(Component, self).__init__(path, paint)