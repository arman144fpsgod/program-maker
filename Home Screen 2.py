from ursina import *

app = Ursina()


def run_level(lx):
    Entity(model="quad", scale=100, color=color.dark_gray)
    Text(text=("This is", lx), position=(0, 0.2))
    button1 = Button(text="Finish", position=(0, -0.2), scale=0.1)
    button1.on_click = 1
    return button1.on_click


def home(lx, cx):
    positionx = 0
    positiony = 0
    level = 0
    if lx == 'Level 1':
        positionx = -0.75
        positiony = 0.15
    elif lx == 'Level 2':
        positionx = -0.5
        positiony = 0.15
    elif lx == 'Level 3':
        positionx = -0.25
        positiony = 0.15
    elif lx == 'Level 4':
        positionx = 0
        positiony = 0.15
    elif lx == 'Level 5':
        positionx = 0.25
        positiony = 0.15
    elif lx == 'Level 6':
        positionx = 0.5
        positiony = 0.15
    elif lx == 'Level 7':
        positionx = 0.75
        positiony = 0.15
    elif lx == 'Level 8':
        positionx = -0.75
        positiony = -0.1
    elif lx == 'Level 9':
        positionx = -0.5
        positiony = -0.1
    elif lx == 'Level 10':
        positionx = -0.5
        positiony = -0.1

    if cx == 0:
        button = Button(text=lx, scale=0.2, position=(positionx, positiony))
        button.on_click = 0
        button.tooltip = Tooltip("Locked")
    elif cx == 1:
        button = Button(text=lx, scale=0.2, position=(positionx, positiony))
        button.on_click = 1
        button.tooltip = Tooltip("Start Level")
    elif cx == 2:
        button = Button(text=lx, scale=0.2, position=(positionx, positiony))
        button.on_click = 2
        button.tooltip = Tooltip("Review Level")
    if button.on_click == None:
        return 0
    return button.on_click


l1 = "Level 1"
l2 = "Level 2"
l3 = "Level 3"
l4 = "Level 4"
l5 = "Level 5"
l6 = "Level 6"
l7 = "Level 7"
l8 = "Level 8"
l9 = "Level 9"
l10 = "Level 10"

c1 = 1
c2 = 0
c3 = 0
c4 = 0
c5 = 0
c6 = 0
c7 = 0
c8 = 0
c9 = 0
c10 = 0

run_level1 = 0
run_level2 = 0
run_level3 = 0
run_level4 = 0
run_level5 = 0
run_level6 = 0
run_level7 = 0
run_level8 = 0
run_level9 = 0
run_level10 = 0
window.fullscreen = True
x = Button(text="x", color=color.red, position=(0.80, 0.45), scale=0.05)
x.on_click = 1
a = 0
if x.on_click == 1:
    a = 1
while a == 0:
    Entity(model="quad", scale=100, color=color.dark_gray)
    x = Button(text="x", color=color.red, position=(0.80, 0.45), scale=0.05)
    x.on_click = 1
    a = 0
    if x.on_click == 1:
        a = x.on_click
    Text(text='Computer Island', scale=5, color=color.gold, position=(-0.5, 0.4))
    home_to_level1 = home(l1, c1)
    home_to_level2 = home(l2, c2)
    home_to_level3 = home(l3, c3)
    home_to_level4 = home(l4, c4)
    home_to_level5 = home(l5, c5)
    home_to_level6 = home(l6, c6)
    home_to_level7 = home(l7, c7)
    home_to_level8 = home(l8, c8)
    home_to_level9 = home(l9, c9)
    home_to_level10 = home(l10, c10)
    if home_to_level1 != 0:
        run_level1 = run_level(l1)
    elif home_to_level2 != 0:
        run_level2 = run_level(l2)
    elif home_to_level3 != 0:
        run_level3 = run_level(l3)
    elif home_to_level4 != 0:
        run_level4 = run_level(l4)
    elif home_to_level5 != 0:
        run_level5 = run_level(l5)
    elif home_to_level6 != 0:
        run_level6 = run_level(l6)
    elif home_to_level7 != 0:
        run_level7 = run_level(l7)
    elif home_to_level8 != 0:
        run_level8 = run_level(l8)
    elif home_to_level9 != 0:
        run_level9 = run_level(l9)
    elif home_to_level10 != 0:
        run_level10 = run_level(l10)
    if run_level1 == 1 and home_to_level1 == 1:
            c1 = 2
            c2 = 1
    elif run_level2 == 1 and home_to_level2 == 1:
        c2 = 2
        c3 = 1
    elif run_level3 == 1 and home_to_level3 == 1:
        c3 = 2
        c4 = 1
    elif run_level4 == 1 and home_to_level4 == 1:
        c4 = 2
        c5 = 1
    elif run_level5 == 1 and home_to_level5 == 1:
        c5 = 2
        c6 = 1
    elif run_level6 == 1 and home_to_level6 == 1:
        c6 = 2
        c7 = 1
    elif run_level7 == 1 and home_to_level7 == 1:
        c7 = 2
        c8 = 1
    elif run_level8 == 1 and home_to_level8 == 1:
        c8 = 2
        c9 = 1
    elif run_level9 == 1 and home_to_level9 == 1:
        c9 = 2
        c10 = 1
    elif run_level10 == 1 and home_to_level10 == 1:
        c10 = 2
    app.run()
