from tkinter import Tk, Frame, Label
from model.values import RGBValue
from controller.engine import SequenceEngine


def rgb_to_hex(data):
    """Takes an RGB value as a tuple and returns a hex string"""
    h = "#"
    if type(data) == RGBValue:
        data = data.get_val()
    for c in data:
        h += hex(c).split("0x")[-1].upper()
        if c < 16:
            h = h[0:len(h)-1] + "0" + h[-1]
    return h


class SenseHat:
    """Dummy Sense hat for displaying in the terminal"""
    def set_pixels(self, data):
        print(data)

    def set_pixel(self, x, y, color):
        print("(X:%d, Y:%d): %s" % (x, y, rgb_to_hex(color)))

    def clear(self):
        print("\n"*20)


class SenseHatGUI(Tk):

    def __init__(self):
        super().__init__()
        self.frame = Frame(master=self)
        self.array = [
            Label(master=self.frame, height=2, width=4, bg="#000") for _ in range(64)
        ]
        self._start()

    def _start(self):
        self.frame.pack()
        for c in range(8):
            for r in range(8):
                self.array[r*8+c].grid(row=r, column=c)

    def set_pixels(self, data):
        for cell, color in zip(self.array, data):
            cell["bg"] = rgb_to_hex(color)

    def set_pixel(self, x, y, color):
        self.array[y*8+x]["bg"]=rgb_to_hex(color)

    def clear(self):
        for cell in self.array:
            cell["bg"] = "#000"


def main():
    hat = SenseHatGUI()
    engine = SequenceEngine()
    engine.load("../model/default.json")


    def update(hat, engine):
        hat.set_pixels(engine.get_next().to_array())
        hat.after(100, update, hat, engine)
    hat.after(100, update, hat, engine)
    hat.mainloop()


if __name__ == "__main__":
    main()