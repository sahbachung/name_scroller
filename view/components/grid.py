from tkinter import Frame, Label, Checkbutton
from model.cell import Cell
from abc import ABC, abstractmethod

from model.sequence import Sequence


class CellButton(Checkbutton, Cell):
    ON = True
    OFF = False

    def __init__(self, y, x, val=True, command=None, master=None):
        super().__init__(master=master, command=command)
        Cell.__init__(self, x, y)
        self._x = x
        self._y = y
        self["onvalue"] = CellButton.ON
        self["offvalue"] = CellButton.OFF
        if val:
            self.select()
        else:
            self.deselect()

    def get_pos(self):
        return self._x, self._y

    def pack(self):
        self.pack()


class Grid(ABC):

    def __init__(self, initial_sequence: Sequence):
        self.grid = initial_sequence

    @abstractmethod
    def add_column(self, index: int): ...

    @abstractmethod
    def remove_column(self, index: int) -> bool: ...


class GridFrame(Frame, Grid):

    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)