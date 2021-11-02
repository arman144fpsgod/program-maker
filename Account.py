from ursina import *
app = Ursina()


def account_enter():
    global lines, i, file1, lines1
    for j in range(0, len(lines)):
        if lines1[j][:-1] == lines[i][:-1]:
            return j


class login_button(Button):
    def __init__(self, position):
        super().__init__(
            parent=scene,
            model="quad",
            color=color.black,
            text="Add +",
            position=position,
            scale=2
        )

    def input(self, key):
        global Login_button
        if self.hovered:
            if key == "left mouse down":
                import Login
                if Login.flag == 1:
                    import Levels


class account(Button):
    def __init__(self, position, text):
        super().__init__(
            parent=scene,
            model="quad",
            color=color.gray,
            text=text,
            position=position,
            scale=2
        )

    def input(self, key):
        if self.hovered:
            if key == "left mouse down":
                file1 = open("Database1.txt", "r")
                lines1 = file1.readlines()
                file2 = open("Database3.txt", "w")
                file2.writelines(lines1[account_enter()][:-1])


file = open("Database5.txt", "r")
lines = file.readlines()
for i in range(3):
    if i < len(lines):
        if i == 0:
            Account = account((-3, 0), lines[i][:-1])
        elif i == 1:
            Account = account((0, 0), lines[i][:-1])
        elif i == 2:
            Account = account((3, 0), lines[i][:-1])
    else:
        if i == 0:
            Login_button = login_button((-3, 0))
        elif i == 1:
            Login_button = login_button((0, 0))
        elif i == 2:
            Login_button = login_button((3, 0))
lines, lines1 = ['0'], ['0']
app.run()
