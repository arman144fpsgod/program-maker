from ursina import *

app = Ursina()




def Cube():
    Entity(model = "cube")
window.fullscreen = True

Text(text='Computer Island', scale = 5, color = color.gold, position = (-0.5, 0.4))
button1 = Button(text="Level 1", scale = 0.2, position = (-0.75, 0.15))
button1.on_click = Cube
button1.tooltip = Tooltip("Start Level")
button2 = Button(text="Level 2", scale = 0.2, position = (-0.5, 0.15))
button2.on_click = Cube
button2.tooltip = Tooltip("Start Level")
button3 = Button(text="Level 3", scale = 0.2, position = (-0.25, 0.15))
button3.on_click = Cube
button3.tooltip = Tooltip("Start Level")
button4 = Button(text="Level 4", scale = 0.2, position = (0.0, 0.15))
button4.on_click = Cube
button4.tooltip = Tooltip("Start Level")
button5 = Button(text="Level 5", scale = 0.2, position = (0.25, 0.15))
button5.on_click = Cube
button5.tooltip = Tooltip("Start Level")
button6 = Button(text="Level 6", scale = 0.2, position = (0.5, 0.15))
button6.on_click = Cube
button6.tooltip = Tooltip("Start Level")
button7 = Button(text="Level 7", scale = 0.2, position = (0.75, 0.15))
button7.on_click = Cube
button7.tooltip = Tooltip("Start Level")
button8 = Button(text="Level 8", scale = 0.2, position = (-0.75, -0.1))
button8.on_click = Cube
button8.tooltip = Tooltip("Start Level")
button9 = Button(text="Level 9", scale = 0.2, position = (-0.5, -0.1))
button9.on_click = Cube
button9.tooltip = Tooltip("Start Level")
button10 = Button(text="Level 10", scale = 0.2, position = (-0.25, -0.1))
button10.on_click = Cube
button10.tooltip = Tooltip("Start Level")


app.run()