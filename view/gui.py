from tkinter import Tk, Frame, Label


class App(Tk):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.main = Frame(self)


if __name__ == "__main__":
    app = Tk()
    app.mainloop()

