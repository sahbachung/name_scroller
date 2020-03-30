from tkinter import Button
from tkinter.colorchooser import askcolor


def hex2rgb(hex_string):
    assert hex_string[0] == "#"
    assert len(hex_string) in (4, 7)
    hex_string = hex_string.split("#")[1]
    rgb_tuple = (0, 0, 0)
    if len(hex_string) == 6:
        rgb_tuple = tuple((
            int(hex_string[h*2 : h*2 + 2], 16) for h in range(len(hex_string)//2)
        ))
    elif len(hex_string) == 3:
        rgb_tuple = tuple((int(hex_string[h], 16) for h in range(hex_string)))
    return rgb_tuple


def rgb2hex(rgb_tuple):
    assert len(rgb_tuple) == 3
    assert all(0 <= x <= 255 for x in rgb_tuple)
    hex_string = "#"
    for c in rgb_tuple:
        hex_string += hex(c).split("x")[1].upper()
    return hex_string


class ColorButton(Button):
    color_hex = "#000000"
    color_rgb = (0, 0, 0)

    def __init__(self, master, color=None):
        super().__init__(master=master, command=self.change_color, width=2)
        if type(color) in (tuple, list):
            self.set_rgb(color)
        elif type(color) is str:
            self.set_hex(color)
        else:
            self.set_hex("#000000")
        self.configure(bg=self.get_hex())

    def get_hex(self) -> str:
        return self.color_hex

    def get_rgb(self) -> tuple:
        return self.color_rgb

    def set_hex(self, hex_string: str) -> None:
        self.color_rgb = hex2rgb(hex_string)
        self.color_hex = hex_string
        self.configure(bg=self.get_hex())

    def set_rgb(self, rgb_tuple: tuple) -> None:
        self.color_hex = rgb2hex(rgb_tuple)
        self.color_rgb = rgb_tuple
        self.configure(bg=self.get_hex())

    def change_color(self) -> None:
        c = askcolor(self.get_hex())[1]
        print(c)
        if c:
            self.set_hex(c)
