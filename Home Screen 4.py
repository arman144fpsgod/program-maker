from ursina import *
app = Ursina()


def lock_check(level, button, level2, level3):
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
    global levels, button1, button2, button3, button4, button5, button6, button7, button8, button9, button10, text
    text = Text(text='Computer Island', scale=5, color=color.gold, position=(-0.5, 0.4))
    button1 = Button(text=levels[0][0], scale=0.2, position=(-0.75, 0.15))
    lock_check(levels[0][1], button1, levels[0][0], 0)
    button2 = Button(text=levels[1][0], scale=0.2, position=(-0.5, 0.15))
    lock_check(levels[1][1], button2, levels[1][0], 1)
    button3 = Button(text=levels[2][0], scale=0.2, position=(-0.25, 0.15))
    lock_check(levels[2][1], button3, levels[2][0], 2)
    button4 = Button(text=levels[3][0], scale=0.2, position=(0, 0.15))
    lock_check(levels[3][1], button4, levels[3][0], 3)
    button5 = Button(text=levels[4][0], scale=0.2, position=(0.25, 0.15))
    lock_check(levels[4][1], button5, levels[4][0], 4)
    button6 = Button(text=levels[5][0], scale=0.2, position=(0.5, 0.15))
    lock_check(levels[5][1], button6, levels[5][0], 5)
    button7 = Button(text=levels[6][0], scale=0.2, position=(0.75, 0.15))
    lock_check(levels[6][1], button7, levels[6][0], 6)
    button8 = Button(text=levels[7][0], scale=0.2, position=(-0.75, -0.1))
    lock_check(levels[7][1], button8, levels[7][0], 7)
    button9 = Button(text=levels[8][0], scale=0.2, position=(-0.5, -0.1))
    lock_check(levels[8][1], button9, levels[8][0], 8)
    button10 = Button(text=levels[9][0], scale=0.2, position=(-0.25, -0.1))
    lock_check(levels[9][1], button10, levels[9][0], 9)


window.fullscreen = True
button1, button2, button3, button4, button5, button6, button7, button8, button9, button10, finish, text, text2 =\
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
levels = [["Level 1", 1], ["Level 2", 0], ["Level 3", 0], ["Level 4", 0], ["Level 5", 0], ["Level 6", 0],\
          ["Level 7", 0], ["Level 8", 0], ["Level 9", 0], ["Level 10", 0]]
home()
app.run()
