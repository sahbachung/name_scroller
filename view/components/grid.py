from tkinter import Frame, Label, Checkbutton
from model.cell import Cell

class CellButton(Checkbutton, Cell):
    ON = True
    OFF = False

    def __init__(self, y, x, val=True, command=None, master=None):
        super().__init__(master=master, command=command)
        Cell.__init__(self, x, y, val)
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

