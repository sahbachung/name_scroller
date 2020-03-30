from tkinter import Frame, Button
from components.colorbutton import ColorButton


class Column(Frame):
    grid_height = 8

    def __init__(self, master, cells=None):
        super().__init__(master=master)
        self.del_button = Button(master=self, text=" X ", command=(
            lambda: self.master.remove_col(index=self.master.get_index(self))
        ))
        self.grid_cells = []
        if cells:
            assert len(cells) == self.grid_height
            for c in cells:
                self.grid_cells.append(ColorButton(self, color=c))
        else:
            self.grid_cells = [ColorButton(self) for _ in range(self.grid_height)]
        self.del_button.pack()
        for c in self.grid_cells:
            c.pack()

    def get_rgb_array(self) -> list:
        cells = []
        for cell in self.grid_cells:
            cells.append(cell.get_rgb())
        return cells

    def load_rgb_array(self, cells: list) -> None:
        for i, cell in enumerate(cells):
            self.grid_cells[i].set_rgb(cell)

    def load_hex_array(self, cells: list) -> None:
        for i, cell in enumerate(cells):
            self.grid_cells[i].set_hex(cell)

    def get_selected(self) -> bool:
        return bool(self.selected)

