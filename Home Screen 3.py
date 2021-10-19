from ursina import *

app = Ursina()


def complete(levels, level):
    if levels[level][1] == 1:
        levels[level][1] = 2
        if level < 9:
            levels[level+1][1] = 1
    return levels


def run(levels, level):
    Entity(model="quad", scale=100, color=color.dark_gray)
    Text(text=("This is", levels[level][0]), position=(0, 0.2), scale=2)
    finish = Button(text="Finish", position=(0, -0.2), scale=0.1)
    finish.on_click = Func(complete, levels, level)
    return finish.on_click


def home(levels):
    Entity(model="quad", scale=100, color=color.dark_gray)
    Text(text='Computer Island', scale=5, color=color.gold, position=(-0.5, 0.4))
    button1 = Button(text=levels[0][0], scale=0.2, position=(-0.75, 0.15))
    a = 1
    if levels[0][1] == 0:
        button1.tooltip = Tooltip("Locked")
    elif levels[0][1] == 1:
        button1.tooltip = Tooltip("Start Level")
        button1.on_click = Func(run, levels, 0)
        while button1.on_click == None:
            a += 1
        return button1.on_click
    elif levels[0][1] == 2:
        button1.tooltip = Tooltip("Review Level")
        button1.on_click = Func(run, levels, 0)
        return button1.on_click
    button2 = Button(text=levels[1][0], scale=0.2, position=(-0.5, 0.15))
    if levels[1][1] == 0:
        button2.tooltip = Tooltip("Locked")
    elif levels[1][1] == 1:
        button2.tooltip = Tooltip("Start Level")
        button2.on_click = Func(run, levels, 1)
        return button2.on_click
    elif levels[1][1] == 2:
        button2.tooltip = Tooltip("Review Level")
        button2.on_click = Func(run, levels, 1)
        return button2.on_click
    button3 = Button(text=levels[2][0], scale=0.2, position=(-0.25, 0.15))
    if levels[2][1] == 0:
        button3.tooltip = Tooltip("Locked")
    elif levels[2][1] == 1:
        button3.tooltip = Tooltip("Start Level")
        button3.on_click = Func(run, levels, 2)
        return button3.on_click
    elif levels[2][1] == 2:
        button3.tooltip = Tooltip("Review Level")
        button3.on_click = Func(run, levels, 2)
        return button3.on_click
    button4 = Button(text=levels[3][0], scale=0.2, position=(0, 0.15))
    if levels[3][1] == 0:
        button4.tooltip = Tooltip("Locked")
    elif levels[3][1] == 1:
        button4.tooltip = Tooltip("Start Level")
        button4.on_click = Func(run, levels, 3)
        return button1.on_click
    elif levels[3][1] == 2:
        button4.tooltip = Tooltip("Review Level")
        button4.on_click = Func(run, levels, 3)
        return button1.on_click
    button5 = Button(text=levels[4][0], scale=0.2, position=(0.25, 0.15))
    if levels[4][1] == 0:
        button5.tooltip = Tooltip("Locked")
    elif levels[4][1] == 1:
        button5.tooltip = Tooltip("Start Level")
        button5.on_click = Func(run, levels, 4)
        return button5.on_click
    elif levels[4][1] == 2:
        button5.tooltip = Tooltip("Review Level")
        button5.on_click = Func(run, levels, 4)
        return button5.on_click
    button6 = Button(text=levels[5][0], scale=0.2, position=(0.5, 0.15))
    if levels[5][1] == 0:
        button6.tooltip = Tooltip("Locked")
    elif levels[5][1] == 1:
        button6.tooltip = Tooltip("Start Level")
        button5.on_click = Func(run, levels, 5)
        return button5.on_click
    elif levels[5][1] == 2:
        button6.tooltip = Tooltip("Review Level")
        button6.on_click = Func(run, levels, 5)
        return button6.on_click
    button7 = Button(text=levels[6][0], scale=0.2, position=(-0.75, 0.15))
    if levels[6][1] == 0:
        button7.tooltip = Tooltip("Locked")
    elif levels[6][1] == 1:
        button7.tooltip = Tooltip("Start Level")
        button7.on_click = Func(run, levels, 6)
        return button7.on_click
    elif levels[6][1] == 2:
        button7.tooltip = Tooltip("Review Level")
        button7.on_click = Func(run, levels, 6)
        return button1.on_click
    button8 = Button(text=levels[7][0], scale=0.2, position=(-0.75, 0.15))
    if levels[7][1] == 0:
        button8.tooltip = Tooltip("Locked")
    elif levels[7][1] == 1:
        button8.tooltip = Tooltip("Start Level")
        button8.on_click = Func(run, levels, 7)
        return button8.on_click
    elif levels[7][1] == 2:
        button8.tooltip = Tooltip("Review Level")
        button8.on_click = Func(run, levels, 7)
        return button8.on_click
    button9 = Button(text=levels[8][0], scale=0.2, position=(-0.75, 0.15))
    if levels[8][1] == 0:
        button9.tooltip = Tooltip("Locked")
    elif levels[8][1] == 1:
        button9.tooltip = Tooltip("Start Level")
        button9.on_click = Func(run, levels, 8)
        return button9.on_click
    elif levels[8][1] == 2:
        button9.tooltip = Tooltip("Review Level")
        button9.on_click = Func(run, levels, 8)
        return button9.on_click
    button10 = Button(text=levels[9][0], scale=0.2, position=(-0.75, 0.15))
    if levels[9][1] == 0:
        button10.tooltip = Tooltip("Locked")
    elif levels[9][1] == 1:
        button10.tooltip = Tooltip("Start Level")
        button10.on_click = Func(run, levels, 9)
        return button10.on_click
    elif levels[9][1] == 2:
        button10.tooltip = Tooltip("Review Level")
        button10.on_click = Func(run, levels, 9)
        return button10.on_click


l1 = ["Level1", 1]
l2 = ["Level2", 0]
l3 = ["Level3", 0]
l4 = ["Level4", 0]
l5 = ["Level5", 0]
l6 = ["Level6", 0]
l7 = ["Level7", 0]
l8 = ["Level8", 0]
l9 = ["Level9", 0]
l10 = ["Level10", 0]
levels_list = [l1, l2, l3, l4, l5, l6, l7, l8, l9, l10]

while True:
    levels_list = home(levels_list)
    app.run()
