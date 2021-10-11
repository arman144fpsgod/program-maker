from ursina import *

app = Ursina()

window.windowed_size = 0.3
window.update_aspect_ratio()
window.late_init()

Entity(model='cube')
Entity(model='cube', position=(2,2,2))

app.run()