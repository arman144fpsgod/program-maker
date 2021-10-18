from ursina import *

app = Ursina()

def Cube():
    Entity(model = "cube")


window.fullscreen = True


complete1 = 1
complete2 = 0
complete3 = 0
complete4 = 0
complete5 = 0
complete6 = 0
complete7 = 0
complete8 = 0
complete9 = 0
complete10 = 0


Text(text='Computer Island', scale = 5, color = color.gold, position = (-0.5, 0.4))
if complete1 == 0:
    button1 = Button(text="Level 1", scale=0.2, position=(-0.75, 0.15))
    button1.tooltip = Tooltip("Locked")
elif complete1 == 1:
    button1 = Button(text="Level 1", scale=0.2, position=(-0.75, 0.15))
    button1.on_click = Cube
    button1.tooltip = Tooltip("Start Level")
elif complete1 == 2:
    button1 = Button(text="Level 1", scale=0.2, position=(-0.75, 0.15))
    button1.on_click = Cube
    button1.tooltip = Tooltip("Review Level")
if complete2 == 0:
    button2 = Button(text="Level 2", scale=0.2, position=(-0.5, 0.15))
    button2.tooltip = Tooltip("Locked")
elif complete2 == 1:
    button2 = Button(text="Level 2", scale=0.2, position=(-0.5, 0.15))
    button2.on_click = Cube
    button2.tooltip = Tooltip("Start Level")
elif complete2 == 2:
    button2 = Button(text="Level 2", scale=0.2, position=(-0.5, 0.15))
    button2.on_click = Cube
    button2.tooltip = Tooltip("Review Level")
if complete3 == 0:
    button3 = Button(text="Level 3", scale=0.2, position=(-0.25, 0.15))
    button3.tooltip = Tooltip("Locked")
elif complete3 == 1:
    button3 = Button(text="Level 3", scale=0.2, position=(-0.25, 0.15))
    button3.on_click = Cube
    button3.tooltip = Tooltip("Start Level")
elif complete3 == 2:
    button3 = Button(text="Level 3", scale=0.2, position=(-0.25, 0.15))
    button3.on_click = Cube
    button3.tooltip = Tooltip("Review Level")
if complete4 == 0:
    button4 = Button(text="Level 4", scale=0.2, position=(0, 0.15))
    button4.tooltip = Tooltip("Locked")
elif complete4 == 1:
    button4 = Button(text="Level 4", scale=0.2, position=(0, 0.15))
    button4.on_click = Cube
    button4.tooltip = Tooltip("Start Level")
elif complete4 == 2:
    button4 = Button(text="Level 4", scale=0.2, position=(0, 0.15))
    button4.on_click = Cube
    button4.tooltip = Tooltip("Review Level")
if complete5 == 0:
    button5 = Button(text="Level 5", scale=0.2, position=(0.25, 0.15))
    button5.tooltip = Tooltip("Locked")
elif complete5 == 1:
    button5 = Button(text="Level 5", scale=0.2, position=(0.25, 0.15))
    button5.on_click = Cube
    button5.tooltip = Tooltip("Start Level")
elif complete5 == 2:
    button5 = Button(text="Level 5", scale=0.2, position=(0.25, 0.15))
    button5.on_click = Cube
    button5.tooltip = Tooltip("Review Level")
if complete6 == 0:
    button6 = Button(text="Level 6", scale=0.2, position=(0.5, 0.15))
    button6.tooltip = Tooltip("Locked")
elif complete6 == 1:
    button6 = Button(text="Level 6", scale=0.2, position=(0.5, 0.15))
    button6.on_click = Cube
    button6.tooltip = Tooltip("Start Level")
elif complete6 == 2:
    button6 = Button(text="Level 6", scale=0.2, position=(0.5, 0.15))
    button6.on_click = Cube
    button6.tooltip = Tooltip("Review Level")
if complete7 == 0:
    button7 = Button(text="Level 7", scale=0.2, position=(0.75, 0.15))
    button7.tooltip = Tooltip("Locked")
elif complete7 == 1:
    button7 = Button(text="Level 7", scale=0.2, position=(0.75, 0.15))
    button7.on_click = Cube
    button7.tooltip = Tooltip("Start Level")
elif complete7 == 2:
    button7 = Button(text="Level 7", scale=0.2, position=(0.75, 0.15))
    button7.on_click = Cube
    button7.tooltip = Tooltip("Review Level")
if complete8 == 0:
    button8 = Button(text="Level 8", scale=0.2, position=(-0.75, -0.1))
    button8.tooltip = Tooltip("Locked")
elif complete8 == 1:
    button8 = Button(text="Level 8", scale=0.2, position=(-0.75, -0.1))
    button8.on_click = Cube
    button8.tooltip = Tooltip("Start Level")
elif complete8 == 2:
    button8 = Button(text="Level 8", scale=0.2, position=(-0.75, -0.1))
    button8.on_click = Cube
    button8.tooltip = Tooltip("Review Level")
if complete9 == 0:
    button9 = Button(text="Level 9", scale=0.2, position=(-0.5, -0.1))
    button9.tooltip = Tooltip("Locked")
elif complete9 == 1:
    button9 = Button(text="Level 9", scale=0.2, position=(-0.5, -0.1))
    button9.on_click = Cube
    button9.tooltip = Tooltip("Start Level")
elif complete9 == 2:
    button9 = Button(text="Level 9", scale=0.2, position=(-0.5, -0.1))
    button9.on_click = Cube
    button9.tooltip = Tooltip("Review Level")
if complete10 == 0:
    button10 = Button(text="Level 10", scale=0.2, position=(-0.25, -0.1))
    button10.tooltip = Tooltip("Locked")
elif complete10 == 1:
    button10 = Button(text="Level 10", scale=0.2, position=(-0.25, -0.1))
    button10.on_click = Cube
    button10.tooltip = Tooltip("Start Level")
elif complete10 == 2:
    button10 = Button(text="Level 10", scale=0.2, position=(-0.25, -0.1))
    button10.on_click = Cube
    button10.tooltip = Tooltip("Review Level")

app.run()