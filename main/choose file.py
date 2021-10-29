from ursina import *
import tkinter as tk
from tkinter import filedialog

class Choose_file(Button):
        def __init__(self):
            super().__init__(
                parent = scene,
                model = "quad",
                color = color.gray,
                scale = (2,2),
                position = Vec2(0,0),
                text = "Choose file"
            )
        def input(self,key):
            if self.hovered:
                if key == "left mouse down":
                    def UploadAction(event=None):
                        filename = filedialog.askopenfilename()
                        print('Selected:', filename)
                    root = tk.Tk()
                    button = tk.Button(root, text='Open', command=UploadAction)
                    button.pack()
                    root.mainloop()

choose_file = Choose_file()