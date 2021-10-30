from ursina import *
app = Ursina()
music = Audio('My-Audio.ogg',autoplay = False,loop = True)
music.play()
app.run()