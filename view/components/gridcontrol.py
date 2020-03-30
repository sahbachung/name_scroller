from tkinter import Frame, Button

from components.gridframe import Grid


class Control(Frame):

    def __init__(self, master, target: Grid):
        super().__init__(master=master, pady=10, padx=2, bd=2, relief="sunken")
        self.target = target
        self.add_button = Button(master=self, text="Add", command=self.target.add_col)
        self.load_button = Button(master=self, text="Load", command=self.master.load)
        self.save_button = Button(master=self, text="Save", command=self.master.save)
        self.save_as_button = Button(master=self, text="Save As", command=self.master.save_as)
        self.new_button = Button(master=self, text="New", command=self.master.new)
        self.add_button.pack(side="left")
        self.new_button.pack(side="left")
        self.load_button.pack(side="left")
        self.save_button.pack(side="left")
        self.save_as_button.pack(side="left")
