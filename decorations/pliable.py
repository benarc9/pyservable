from abc import ABC
from typing import TypeVar, Generic
from contextlib import contextmanager

from components.component import Component
from decorations.decoration import Decoration

T = TypeVar("T", bound=Decoration)


class Pliable(Generic[T], ABC):
    def __init__(self, component: Component):
        super(Pliable, self).__init__()
        self.component = component

    @contextmanager
    def apply(self):
        raise NotImplementedError("")

    @property
    def component(self) -> Component:
        return self._component

    @component.setter
    def component(self, value: Component):
        self._component = value