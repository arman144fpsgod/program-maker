from ursina import *
app = Ursina()


def lock_ckeck(level, button, level2, level3):
    if level == 0:
        button.tooltip = Tooltip("Locked")
        return None
    elif level == 1:
        button.tooltip = Tooltip("Start Level")
    elif level == 2:
        button.tooltip = Tooltip("Review Level")
    button.on_click = Func(run, level2, level3)


def complete(level):
    if levels[level][1] == 1:
        levels[level][1] = 2
        if level < 9:
            levels[level+1][1] = 1
    destroy(finish, 0)
    destroy(text2, 0)
    home()


def run(level, level2):
    global finish
    global text2
    destroy(button1, 0)
    destroy(button2, 0)
    destroy(button3, 0)
    destroy(button4, 0)
    destroy(button5, 0)
    destroy(button6, 0)
    destroy(button7, 0)
    destroy(button8, 0)
    destroy(button9, 0)
    destroy(button10, 0)
    destroy(text, 0)
    text2 = Text(text=level, scale=3, color=color.red, position=(-0.12, 0.2))
    finish = Button(text="Finish", position=(0, -0.2), scale=0.2)
    finish.on_click = Func(complete, level2)


def home():
    global levels
    global button1
    global button2
    global button3
    global button4
    global button5
    global button6
    global button7
    global button8
    global button9
    global button10
    global text
    text = Text(text='Computer Island', scale=5, color=color.gold, position=(-0.5, 0.4))
    button1 = Button(text=levels[0][0], scale=0.2, position=(-0.75, 0.15))
    lock_ckeck(levels[0][1], button1, levels[0][0], 0)
    button2 = Button(text=levels[1][0], scale=0.2, position=(-0.5, 0.15))
    lock_ckeck(levels[1][1], button2, levels[1][0], 1)
    button3 = Button(text=levels[2][0], scale=0.2, position=(-0.25, 0.15))
    lock_ckeck(levels[2][1], button3, levels[2][0], 2)
    button4 = Button(text=levels[3][0], scale=0.2, position=(0, 0.15))
    lock_ckeck(levels[3][1], button4, levels[3][0], 3)
    button5 = Button(text=levels[4][0], scale=0.2, position=(0.25, 0.15))
    lock_ckeck(levels[4][1], button5, levels[4][0], 4)
    button6 = Button(text=levels[5][0], scale=0.2, position=(0.5, 0.15))
    lock_ckeck(levels[5][1], button6, levels[5][0], 5)
    button7 = Button(text=levels[6][0], scale=0.2, position=(0.75, 0.15))
    lock_ckeck(levels[6][1], button7, levels[6][0], 6)
    button8 = Button(text=levels[7][0], scale=0.2, position=(-0.75, -0.1))
    lock_ckeck(levels[7][1], button8, levels[7][0], 7)
    button9 = Button(text=levels[8][0], scale=0.2, position=(-0.5, -0.1))
    lock_ckeck(levels[8][1], button9, levels[8][0], 8)
    button10 = Button(text=levels[9][0], scale=0.2, position=(-0.25, -0.1))
    lock_ckeck(levels[9][1], button10, levels[9][0], 9)


button1 = 0
button2 = 0
button3 = 0
button4 = 0
button5 = 0
button6 = 0
button7 = 0
button8 = 0
button9 = 0
button10 = 0
finish = 0
text = 0
text2 = 0
l1 = ["Level 1", 1]
l2 = ["Level 2", 0]
l3 = ["Level 3", 0]
l4 = ["Level 4", 0]
l5 = ["Level 5", 0]
l6 = ["Level 6", 0]
l7 = ["Level 7", 0]
l8 = ["Level 8", 0]
l9 = ["Level 9", 0]
l10 = ["Level 10", 0]
levels = [l1, l2, l3, l4, l5, l6, l7, l8, l9, l10]
home()
app.run()
