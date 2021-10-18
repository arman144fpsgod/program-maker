from ursina import *

app = Ursina()


def ignore():
    Entity(model="quad", scale=100, color=color.dark_gray)


def home(complete1, complete2, complete3, complete4, complete5, complete6, complete7, complete8, complete9, complete10):
    Text(text='Computer Island', scale=5, color=color.gold, position=(-0.5, 0.4))
    if complete1 == 0:
        button1 = Button(text="Level 1", scale=0.2, position=(-0.75, 0.15))
        button1.tooltip = Tooltip("Locked")
    elif complete1 == 1:
        button1 = Button(text="Level 1", scale=0.2, position=(-0.75, 0.15))
        button1.on_click = level1(complete1, complete2)
        button1.tooltip = Tooltip("Start Level")
    elif complete1 == 2:
        button1 = Button(text="Level 1", scale=0.2, position=(-0.75, 0.15))
        button1.on_click = level2
        button1.on_click = level1(complete1, complete2)
        button1.tooltip = Tooltip("Review Level")
    if complete2 == 0:
        button2 = Button(text="Level 2", scale=0.2, position=(-0.5, 0.15))
        button2.tooltip = Tooltip("Locked")
    elif complete2 == 1:
        button2 = Button(text="Level 2", scale=0.2, position=(-0.5, 0.15))
        button1.on_click = level2(complete2, complete3)
        button2.tooltip = Tooltip("Start Level")
    elif complete2 == 2:
        button2 = Button(text="Level 2", scale=0.2, position=(-0.5, 0.15))
        button1.on_click = level2(complete2, complete3)
        button2.tooltip = Tooltip("Review Level")
    if complete3 == 0:
        button3 = Button(text="Level 3", scale=0.2, position=(-0.25, 0.15))
        button3.tooltip = Tooltip("Locked")
    elif complete3 == 1:
        button3 = Button(text="Level 3", scale=0.2, position=(-0.25, 0.15))
        button1.on_click = level3(complete3, complete4)
        button3.tooltip = Tooltip("Start Level")
    elif complete3 == 2:
        button3 = Button(text="Level 3", scale=0.2, position=(-0.25, 0.15))
        button1.on_click = level3(complete3, complete4)
        button3.tooltip = Tooltip("Review Level")
    if complete4 == 0:
        button4 = Button(text="Level 4", scale=0.2, position=(0, 0.15))
        button4.tooltip = Tooltip("Locked")
    elif complete4 == 1:
        button4 = Button(text="Level 4", scale=0.2, position=(0, 0.15))
        button1.on_click = level4(complete4, complete5)
        button4.tooltip = Tooltip("Start Level")
    elif complete4 == 2:
        button4 = Button(text="Level 4", scale=0.2, position=(0, 0.15))
        button1.on_click = level4(complete4, complete5)
        button4.tooltip = Tooltip("Review Level")
    if complete5 == 0:
        button5 = Button(text="Level 5", scale=0.2, position=(0.25, 0.15))
        button5.tooltip = Tooltip("Locked")
    elif complete5 == 1:
        button5 = Button(text="Level 5", scale=0.2, position=(0.25, 0.15))
        button1.on_click = level5(complete5, complete6)
        button5.tooltip = Tooltip("Start Level")
    elif complete5 == 2:
        button5 = Button(text="Level 5", scale=0.2, position=(0.25, 0.15))
        button1.on_click = level5(complete5, complete6)
        button5.tooltip = Tooltip("Review Level")
    if complete6 == 0:
        button6 = Button(text="Level 6", scale=0.2, position=(0.5, 0.15))
        button6.tooltip = Tooltip("Locked")
    elif complete6 == 1:
        button6 = Button(text="Level 6", scale=0.2, position=(0.5, 0.15))
        button1.on_click = level6(complete6, complete7)
        button6.tooltip = Tooltip("Start Level")
    elif complete6 == 2:
        button6 = Button(text="Level 6", scale=0.2, position=(0.5, 0.15))
        button1.on_click = level6(complete6, complete7)
        button6.tooltip = Tooltip("Review Level")
    if complete7 == 0:
        button7 = Button(text="Level 7", scale=0.2, position=(0.75, 0.15))
        button7.tooltip = Tooltip("Locked")
    elif complete7 == 1:
        button7 = Button(text="Level 7", scale=0.2, position=(0.75, 0.15))
        button1.on_click = level7(complete7, complete8)
        button7.tooltip = Tooltip("Start Level")
    elif complete7 == 2:
        button7 = Button(text="Level 7", scale=0.2, position=(0.75, 0.15))
        button1.on_click = level7(complete7, complete8)
        button7.tooltip = Tooltip("Review Level")
    if complete8 == 0:
        button8 = Button(text="Level 8", scale=0.2, position=(-0.75, -0.1))
        button8.tooltip = Tooltip("Locked")
    elif complete8 == 1:
        button8 = Button(text="Level 8", scale=0.2, position=(-0.75, -0.1))
        button1.on_click = level8(complete8, complete9)
        button8.tooltip = Tooltip("Start Level")
    elif complete8 == 2:
        button8 = Button(text="Level 8", scale=0.2, position=(-0.75, -0.1))
        button1.on_click = level8(complete8, complete9)
        button8.tooltip = Tooltip("Review Level")
    if complete9 == 0:
        button9 = Button(text="Level 9", scale=0.2, position=(-0.5, -0.1))
        button9.tooltip = Tooltip("Locked")
    elif complete9 == 1:
        button9 = Button(text="Level 9", scale=0.2, position=(-0.5, -0.1))
        button1.on_click = level9(complete9, complete10)
        button9.tooltip = Tooltip("Start Level")
    elif complete9 == 2:
        button9 = Button(text="Level 9", scale=0.2, position=(-0.5, -0.1))
        button1.on_click = level9(complete9, complete10)
        button9.tooltip = Tooltip("Review Level")
    if complete10 == 0:
        button10 = Button(text="Level 10", scale=0.2, position=(-0.25, -0.1))
        button10.tooltip = Tooltip("Locked")
    elif complete10 == 1:
        button10 = Button(text="Level 10", scale=0.2, position=(-0.25, -0.1))
        button1.on_click = level10(complete10)
        button10.tooltip = Tooltip("Start Level")
    elif complete10 == 2:
        button10 = Button(text="Level 10", scale=0.2, position=(-0.25, -0.1))
        button1.on_click = level10(complete10)
        button10.tooltip = Tooltip("Review Level")


def completed1(complete1, complete2):
    complete1 = 2
    complete2 = 1


def completed2(complete2, complete3):
    complete2 = 2
    complete3 = 1


def completed3(complete3, complete4):
    complete3 = 2
    complete4 = 1


def completed4(complete4, complete5):
    complete4 = 2
    complete4 = 1


def completed5(complete5, complete6):
    complete5 = 2
    complete6 = 1


def completed6(complete6, complete7):
    complete6 = 2
    complete7 = 1


def completed7(complete7, complete8):
    complete7 = 2
    complete8 = 1


def completed8(complete8, complete9):
    complete8 = 2
    complete9 = 1


def completed9(complete9, complete10):
    complete9 = 2
    complete10 = 1


def completed10(complete10):
    complete10 = 2


def level1(complete1, complete2):
    Entity(model="quad", scale=100, color = color.dark_gray)
    Text(text='This is Level 1', scale=2, color=color.black, position=(-0.5, 0.2))
    complete = Button(text="Complete", scale=0.3, position=(0, -0.3))
    complete.on_click = completed1(complete1, complete2)


def level2(complete2, complete3):
    ignore = Entity(model="quad", scale=100, color = color.dark_gray)
    Text(text='This is Level 2', scale=2, color=color.black, position=(-0.5, 0.2))
    complete = Button(text="Complete", scale=0.3, position=(0, -0.3))
    complete.on_click = completed2(complete2, complete3)
    complete.on_click = ignore
    complete.on_click = home(complete1, complete2, complete3, complete4, complete5, complete6, complete7, complete8, complete9, complete10)


def level3(complete3, complete4):
    ignore = Entity(model="quad", scale=100, color = color.dark_gray)
    Text(text='This is Level 3', scale=2, color=color.black, position=(-0.5, 0.2))
    complete = Button(text="Complete", scale=0.3, position=(0, -0.3))
    complete.on_click = completed3(complete3, complete4)
    complete.on_click = ignore
    complete.on_click = home(complete1, complete2, complete3, complete4, complete5, complete6, complete7, complete8, complete9, complete10)


def level4(complete4, complete5):
    ignore = Entity(model="quad", scale=100, color = color.dark_gray)
    Text(text='This is Level 4', scale=2, color=color.black, position=(-0.5, 0.2))
    complete = Button(text="Complete", scale=0.3, position=(0, -0.3))
    complete.on_click = completed4(complete4, complete5)
    complete.on_click = ignore
    complete.on_click = home(complete1, complete2, complete3, complete4, complete5, complete6, complete7, complete8, complete9, complete10)


def level5(complete5, complete6):
    ignore = Entity(model="quad", scale=100, color = color.dark_gray)
    Text(text='This is Level 5', scale=2, color=color.black, position=(-0.5, 0.2))
    complete = Button(text="Complete", scale=0.3, position=(0, -0.3))
    complete.on_click = completed5(complete5, complete6)
    complete.on_click = ignore
    complete.on_click = home(complete1, complete2, complete3, complete4, complete5, complete6, complete7, complete8, complete9, complete10)


def level6(complete6, complete7):
    ignore = Entity(model="quad", scale=100, color = color.dark_gray)
    Text(text='This is Level 6', scale=2, color=color.black, position=(-0.5, 0.2))
    complete = Button(text="Complete", scale=0.3, position=(0, -0.3))
    complete.on_click = completed6(complete6, complete7)
    complete.on_click = ignore
    complete.on_click = home(complete1, complete2, complete3, complete4, complete5, complete6, complete7, complete8, complete9, complete10)


def level7(complete7, complete8):
    ignore = Entity(model="quad", scale=100, color = color.dark_gray)
    Text(text='This is Level 7', scale=2, color=color.black, position=(-0.5, 0.2))
    complete = Button(text="Complete", scale=0.3, position=(0, -0.3))
    complete.on_click = completed7(complete7, complete8)
    complete.on_click = ignore
    complete.on_click = home(complete1, complete2, complete3, complete4, complete5, complete6, complete7, complete8, complete9, complete10)


def level8(complete8, complete9):
    ignore = Entity(model="quad", scale=100, color = color.dark_gray)
    Text(text='This is Level 8', scale=2, color=color.black, position=(-0.5, 0.2))
    complete = Button(text="Complete", scale=0.3, position=(0, -0.3))
    complete.on_click = completed8(complete8, complete9)
    complete.on_click = ignore
    complete.on_click = home(complete1, complete2, complete3, complete4, complete5, complete6, complete7, complete8, complete9, complete10)


def level9(complete9, complete10):
    ignore = Entity(model="quad", scale=100, color = color.dark_gray)
    Text(text='This is Level 9', scale=2, color=color.black, position=(-0.5, 0.2))
    complete = Button(text="Complete", scale=0.3, position=(0, -0.3))
    complete.on_click = completed9(complete9, complete10)
    complete.on_click = ignore
    complete.on_click = home(complete1, complete2, complete3, complete4, complete5, complete6, complete7, complete8, complete9, complete10)


def level10(complete10):
    ignore = Entity(model="quad", scale=100, color = color.dark_gray)
    Text(text='This is Level 10', scale=2, color=color.black, position=(-0.5, 0.2))
    complete = Button(text="Complete", scale=0.3, position=(0, -0.3))
    complete.on_click = completed10(complete10)
    complete.on_click = ignore
    complete.on_click = home(complete1, complete2, complete3, complete4, complete5, complete6, complete7, complete8, complete9, complete10)


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

home(complete1, complete2, complete3, complete4, complete5, complete6, complete7, complete8, complete9, complete10)


app.run()
