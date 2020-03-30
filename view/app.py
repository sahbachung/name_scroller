from tkinter import Tk
from tkinter.filedialog import asksaveasfilename, askopenfilename

from json import load, dump

from components.gridframe import Grid
from components.gridcontrol import Control


class App(Tk):

    def __init__(self, *args, **kwargs):
        super().__init__()
        self.resizable(0, 0)
        self.current_fp = ""
        self.title("Color Sequencer")
        self.grid = Grid(self)
        self.control = Control(self, self.grid)
        self.control.pack(fill="y")
        self.grid.pack()

    def new(self) -> None:
        self.grid.forget()
        self.grid = Grid(self)
        self.grid.pack()

    def load(self):
        if self.current_fp is "":
            loc = askopenfilename(
                defaultextension=".json",
                filetypes=(
                    ("JSON files", "*.json"),
                    ("All Files", "*.*")))
        else:
            loc = askopenfilename(
                defaultextension=".json",
                filetypes=(
                    ("JSON files", "*.json"),
                    ("All Files", "*.*")),
                initialdir=self.current_fp)
        if loc is None or loc is "":
            return
        self.grid.destroy()
        with open(loc) as file:
            data = load(file)
            self.grid = Grid(self, data=data)
            self.grid.pack()

    def save(self) -> bool:
        if self.current_fp is "":
            return self.save_as()
        else:
            try:
                with open(self.current_fp, "x") as file:
                    dump(self.grid.save(), file)
            except FileExistsError:
                with open(self.current_fp, "w") as file:
                    dump(self.grid.save(), file)
            finally:
                return True

    def save_as(self) -> bool:
        if self.current_fp is "":
            loc = asksaveasfilename(
                defaultextension=".json",
                filetypes=(
                    ("json file", "*.json"),
                    ("All Files", "*.*")))
        else:
            loc = asksaveasfilename(
                defaultextension=".json",
                filetypes=(
                    ("json file", "*.json"),
                    ("All Files", "*.*")),
                initialfile=self.current_fp)
        if not loc:
            return False
        try:
            with open(loc, "x") as file:
                dump(self.grid.save(), file)
        except FileExistsError:
            with open(loc, "w") as file:
                dump(self.grid.save(), file)
        self.current_fp = loc
        return True


def main():
    app = App()
    app.mainloop()


if __name__ == "__main__":
    main()