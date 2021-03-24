from abc import ABC
from typing import TypeVar, Generic

import skia

from components.component import Component
from decorations.pliable import Pliable

T = TypeVar("T", bound=Component)


class Decoration(Generic[T], Pliable[T], ABC):
    def __init__(self, component: T,
                 color: skia.Color4f=skia.ColorGRAY,
                 stroke_width:int=4,
                 join_style: skia.Paint.Join=skia.Paint.kRound_Join,
                 cap_style: skia.Paint.Cap=skia.Paint.kRound_Cap):
        self.paint = skia.Paint()
        self.paint.setColor(color)
        self.paint.setStrokeCap(cap_style),
        self.paint.setStyle(skia.Paint.kStroke_Style),
        self.paint.setStrokeJoin(join_style),
        self.paint.setStrokeWidth(stroke_width)
        super(Decoration, self).__init__(component.path, self.paint)

    def apply(self, canvas: skia.Canvas):
        if skia.Canvas is not None:
            canvas.drawPath(self.component.path, self.paint)