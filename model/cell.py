from abc import ABC, abstractmethod


class Cell(ABC):

    def __init__(self, x, y):
        self._coords = (x, y)

    def get_pos(self):
        return self._coords

    def set_pos(self, pos):
        self._coords = pos

    pos = property(fget=get_pos, fset=set_pos)