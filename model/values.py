from abc import ABC, abstractmethod
from enum import Enum


class RGB(Enum):

    RED = 0
    GREEN = 1
    BLUE = 2


class Value(ABC):

    @abstractmethod
    def set_val(self, *args, **kwargs): ...

    @abstractmethod
    def get_val(self): ...


class RGBValue(Value):

    def __init__(self, r=0, g=0, b=0):
        self._r = r
        self._g = g
        self._b = b

    def get_val(self):
        return self._r, self._g, self._b

    def set_val(self, r=-1, g=-1, b=-1):
        """If any of the values are less than zero the value will be unchanged"""
        try:
            self.set_colour(RGB.RED, r)
        except ValueError:
            pass
        try:
            self.set_colour(RGB.GREEN, g)
        except ValueError:
            pass
        try:
            self.set_colour(RGB.BLUE, b)
        except ValueError:
            pass

    def set_colour(self, color: RGB, value):
        if value < 0 or 255 < value:
            if value < 0:
                raise ValueError("%d <0 " % value)
            else:
                raise ValueError("255 < %d" % value)
        elif color is RGB.RED:
            self._r = value
        elif color is RGB.GREEN:
            self._g = value
        elif color is RGB.BLUE:
            self._b = value

    def __repr__(self):
        return str(self.get_val())


class OnOffValue(Value):

    def __init__(self, state, rgb_on_val: RGBValue = RGBValue(255, 255, 255), rgb_off_val: RGBValue = RGBValue()):
        self.state = state
        self.rgb_on = rgb_on_val
        self.rgb_off = rgb_off_val

    def set_val(self, state):
        self.state = state

    def get_val(self):
        return self.state

    def get_rgb(self) -> RGBValue:
        if self.state:
            return self.rgb_on
        else:
            return self.rgb_off





