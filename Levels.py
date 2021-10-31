from ursina import *
app = Ursina()


def start():
    global levels, levelbutton, alllevels, level, back_button
    destroy(button0, 0)
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
    destroy(button11, 0)
    destroy(button12, 0)
    destroy(button13, 0)
    destroy(button14, 0)
    destroy(button15, 0)
    destroy(button16, 0)
    destroy(button17, 0)
    destroy(button18, 0)
    destroy(button19, 0)
    destroy(button20, 0)
    destroy(levelbutton, 0)
    destroy(alllevels, 0)
    destroy(back_button, 0)
    destroy(text, 0)

    for i in range(0, 21):
        if i == level:
            levels[i][1] = 1
            for j in range(1, (i + 1)):
                levels[i - j][1] = 2
    leveltext = levels[level][0]
    levelbutton = Button(text=leveltext, scale=0.5, position=(0, 0))
    lock_check(levels[level][1], levelbutton, levels[level][0], level)
    alllevels = Button(text="|||", scale=0.1, position=(-0.7, 0.4))
    alllevels.fit_to_text(radius=.1)
    alllevels.on_click = Func(home)


def lock_check(level1, button, level2, level3):
    if level1 == 0:
        button.tooltip = Tooltip("Locked")
        return None
    elif level1 == 1:
        button.tooltip = Tooltip("Start Level")
    elif level1 == 2:
        button.tooltip = Tooltip("Review Level")
    button.on_click = Func(run, level2, level3)


def complete(level1):
    if levels[level1][1] == 1:
        levels[level1][1] = 2
        if level1 < 19:
            levels[level1+1][1] = 1
    file = open("Database4.txt", "r")
    lines = file.readlines()
    level = int(lines[num][:-1])
    destroy(finish, 0)
    destroy(text2, 0)
    start()


def run(level1, level2):
    global finish, text2
    destroy(button0, 0)
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
    destroy(button11, 0)
    destroy(button12, 0)
    destroy(button13, 0)
    destroy(button14, 0)
    destroy(button15, 0)
    destroy(button16, 0)
    destroy(button17, 0)
    destroy(button18, 0)
    destroy(button19, 0)
    destroy(button20, 0)
    destroy(levelbutton, 0)
    destroy(alllevels, 0)
    destroy(back_button, 0)
    destroy(text, 0)
    text2 = Text(text=level1, scale=3, color=color.red, position=(-0.12, 0.2))
    finish = Button(text="Finish", position=(0, -0.2), scale=0.2)
    finish.on_click = Func(complete, level2)


def home():
    global button0, button1, button2, button3, button4, button5, button6, button7, button8, button9, button10,\
        button11, button12, button13, button14, button15, button16, button17, button18, button19, button20, text
    destroy(alllevels, 0)
    destroy(levelbutton, 0)
    back_button = Button(text="<-", scale=0.1, position=(-0.7, 0.4))
    back_button.fit_to_text(radius=.1)
    back_button.on_click = Func(start)
    text = Text(text='Computer Island', scale=5, color=color.gold, position=(-0.5, 0.4))
    button0 = Button(text=levels[0][0], scale=0.2, position=(-0.75, 0.15))
    lock_check(levels[0][1], button0, levels[0][0], 0)
    button1 = Button(text=levels[1][0], scale=0.2, position=(-0.5, 0.15))
    lock_check(levels[1][1], button1, levels[1][0], 1)
    button2 = Button(text=levels[2][0], scale=0.2, position=(-0.25, 0.15))
    lock_check(levels[2][1], button2, levels[2][0], 2)
    button3 = Button(text=levels[3][0], scale=0.2, position=(0, 0.15))
    lock_check(levels[3][1], button3, levels[3][0], 3)
    button4 = Button(text=levels[4][0], scale=0.2, position=(0.25, 0.15))
    lock_check(levels[4][1], button4, levels[4][0], 4)
    button5 = Button(text=levels[5][0], scale=0.2, position=(0.5, 0.15))
    lock_check(levels[5][1], button5, levels[5][0], 5)
    button6 = Button(text=levels[6][0], scale=0.2, position=(0.75, 0.15))
    lock_check(levels[6][1], button6, levels[6][0], 6)
    button7 = Button(text=levels[7][0], scale=0.2, position=(-0.75, -0.1))
    lock_check(levels[7][1], button7, levels[7][0], 7)
    button8 = Button(text=levels[8][0], scale=0.2, position=(-0.5, -0.1))
    lock_check(levels[8][1], button8, levels[8][0], 8)
    button9 = Button(text=levels[9][0], scale=0.2, position=(-0.25, -0.1))
    lock_check(levels[9][1], button9, levels[9][0], 9)
    button10 = Button(text=levels[10][0], scale=0.2, position=(0, -0.1))
    lock_check(levels[10][1], button10, levels[10][0], 10)
    button11 = Button(text=levels[11][0], scale=0.2, position=(0.25, -0.1))
    lock_check(levels[11][1], button11, levels[11][0], 11)
    button12 = Button(text=levels[12][0], scale=0.2, position=(0.5, -0.1))
    lock_check(levels[12][1], button12, levels[12][0], 12)
    button13 = Button(text=levels[13][0], scale=0.2, position=(0.75, -0.1))
    lock_check(levels[13][1], button13, levels[13][0], 13)
    button14 = Button(text=levels[14][0], scale=0.2, position=(-0.75, -0.35))
    lock_check(levels[14][1], button14, levels[14][0], 14)
    button15 = Button(text=levels[15][0], scale=0.2, position=(-0.5, -0.35))
    lock_check(levels[15][1], button15, levels[15][0], 15)
    button16 = Button(text=levels[16][0], scale=0.2, position=(-0.25, -0.35))
    lock_check(levels[16][1], button16, levels[16][0], 16)
    button17 = Button(text=levels[17][0], scale=0.2, position=(0, -0.35))
    lock_check(levels[17][1], button17, levels[17][0], 17)
    button18 = Button(text=levels[18][0], scale=0.2, position=(0.5, -0.35))
    lock_check(levels[18][1], button18, levels[18][0], 18)
    button19 = Button(text=levels[19][0], scale=0.2, position=(0.25, -0.35))
    lock_check(levels[19][1], button19, levels[19][0], 19)
    button20 = Button(text=levels[20][0], scale=0.2, position=(0.75, -0.35))
    lock_check(levels[20][1], button19, levels[20][0], 20)


window.fullscreen = True
button0, button1, button2, button3, button4, button5, button6, button7, button8, button9, button10, button11, button12,\
button13, button14, button15, button16, button17, button18, button19, button20, levelbutton, alllevels, finish, text,\
text2, levels, back_button = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
file = open("Database3.txt", "r")
num = int(file.read())
file = open("Database4.txt", "r")
lines = file.readlines()
level = int(lines[num][:-1])
levels = [["Level 0", 0], ["Level 1", 0], ["Level 2", 0], ["Level 3", 0], ["Level 4", 0], ["Level 5", 0],\
            ["Level 6", 0], ["Level 7", 0], ["Level 8", 0], ["Level 9", 0], ["Level 10", 0], ["Level 11", 0],\
            ["Level 12", 0], ["Level 13", 0], ["Level 14", 0], ["Level 15", 0], ["Level 16", 0], ["Level 17", 0],\
            ["Level 18", 0], ["Level 19", 0], ["Level 20", 0]]
start()
app.run()
