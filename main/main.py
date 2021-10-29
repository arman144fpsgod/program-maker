from numpy import positive
from ursina import *
from ursina import texture

def main():
    app = Ursina()
    class Start_button(Button):
        def __init__(self,text2):
            super().__init__(
                parent = scene,
                model = "quad",
                texture = "Graphic/play-button.PNG",
                color = color.white66,
                scale = (2.5,2.5),
                position = Vec2(0,1.2),
                text= text2,
                #highlight_color = color.
            )
        def input(self, key):
            if self.hovered:
                if key == "left mouse down":
                    destroy(start_button)
                    destroy(menu_button)
                    destroy(setting_button)
                    destroy(start_text)
                    destroy(menu_text)
                    import mainv2
    class Menu_button(Button):
        def __init__(self,text3):
            super().__init__(
                parent = scene,
                model = "quad",
                texture = "Graphic/menu (1)",
                color = color.red,
                scale = (1,1),
                position = Vec2(-.9,-.7),
                text=text3
            )
    class Settings_button(Button):
        def __init__(self):
            super().__init__(
                parent = scene,
                model = "quad",
                color = color.white66,
                texture = "Graphic/settings",
                scale = (1,1),
                position = Vec2(.9,-.7)
            )
    #window.size = 300,150
    window._icon = "Graphic/island.png"
    start_text = Text(text = "lets start coding",scale = (1), position = Vec2(-.07,.15))
    start_button = Start_button(start_text)
    setting_button = Settings_button()
    menu_text = Text(text = "Menu",scale = (1), position = Vec2(-.05,-.07))
    menu_button = Menu_button(menu_text)
    app.run()
main()