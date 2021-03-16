from abc import ABC
from typing import List, TypeVar, Callable, Generic
from enum import Enum


T = TypeVar("T", bound='EventType')
U = TypeVar("U", bound='Observable')


class Event(ABC):
    def __init__(self, source: U, event_type: T, *args, **kwargs):
        self.source = source
        self.event_type = event_type
        self.args = args
        for key, val in kwargs:
            self.__setattr__(key, val)

    @property
    def event_type(self) -> T:
        return self._event_type

    @event_type.setter
    def event_type(self, value: T):
        self._event_type = value

    @property
    def source(self) -> U:
        return self._source

    @source.setter
    def source(self, value: U):
        self._source = value

class EventType(Enum):
    def __init__(self):
        pass


class Observer(ABC):
    def __init__(self):
        pass

    def on_event(self, event: Event):
        raise NotImplementedError()


class Observable(ABC):
    def __init__(self):
        self.observers = []

    def add_observer(self, observer: Observer):
        if observer not in self.observers:
            self.observers.append(observer)

    def remove_observer(self, observer: Observer):
        self.observers.remove(observer)

    def notify(self, event: Event):
        for observer in self.observers:
            observer.on_event(event)

    @property
    def observers(self) -> List[Observer]:
        return self._observers

    @observers.setter
    def observers(self, value: List[Observer]):
        self._observers = value


B = TypeVar("B")


class Bindable(Generic[B], ABC):
    def __init__(self):
        super(Bindable, self).__init__()
        self.bound = []

    def bind(self, other: 'Bindable'):
        if self not in other.bound:
            other.bound.append(self)

    def unbind(self, other: 'Bindable'):
        if self in other.bound:
            other.bound.remove(self)
        if other in self.bound:
            self.bound.remove(other)

    def bind_bidirectional(self, other: 'Bindable'):
        if other not in self.bound:
            self.bound.append(other)
        if self not in other.bound:
            other.bind(self)

    def remote_change(self, new: B):
        raise NotImplementedError()

    def changed(self, new_value: B):
        for bound in self.bound:
            bound.remote_change(new_value)

    @property
    def bound(self) -> List['Bindable']:
        return self._bound

    @bound.setter
    def bound(self, value: List['Bindable']):
        self._bound = value


P = TypeVar("P", bound=property)


class ObservableProperty(Bindable[B], ABC):

    def __init__(self, value: B=None):
        super(ObservableProperty, self).__init__()
        self._value = value

    def __str__(self):
        return str(self.value)

    def remote_change(self, new: B):
        self._value = new

    @property
    def value(self) -> B:
        return self._value

    @value.setter
    def value(self, value: B):
        if self._value != value:
            self._value = value
            self.changed(self._value)


class BoolProperty(ObservableProperty[bool]):
    def __init__(self, initial: bool=None):
        super(BoolProperty, self).__init__(initial)


class ObjectProperty(Generic[B], ObservableProperty[B]):
    def __init__(self, value: B=None):
        super(ObjectProperty, self).__init__(value)