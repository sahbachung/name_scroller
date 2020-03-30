from tkinter import Frame

from components.gridcolumn import Column


class Grid(Frame):

    def __init__(self, master, data=None):
        super().__init__(master=master)
        self.cols = []
        if data:
            for column in data:
                self.cols.append(Column(self, cells=column))
        else:
            self.cols = [Column(self) for _ in range(8)]
        for col in self.cols:
            col.pack(side="left")

    def add_col(self, data=None) -> None:
        if data:
            self.cols.append(Column(self, cells=data))
        else:
            self.cols.append(Column(self))
            self.cols[-1].pack(side="left")

    def remove_col(self, index=-1) -> None:
        self.cols[index].destroy()
        self.cols.remove(self.cols[index])

    def get_index(self, col: Column) -> int:
        return self.cols.index(col)

    def save(self) -> list:
        data = []
        for col in self.cols:
            data.append(col.get_rgb_array())
        return data

    def new(self):
        for col in self.cols:
            col.destroy()
        self.cols = [Column(self) for _ in range(8)]
