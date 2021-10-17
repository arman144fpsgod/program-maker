from ursina import *

app = Ursina()


def Cube():
    Entity(model="cube", color = color.red)
window.fullscreen = True

button = Button(text="Level 1")
button.on_click = Cube
button.tooltip = Tooltip("Start Level")

app.run()
