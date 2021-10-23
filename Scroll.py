from ursina import *
app = Ursina()
p = Button(model='quad', scale=(.4, .8), collider='box')
for i in range(8):
    Button(parent=p, scale_y=.05, text=f'giopwjoigjwr{i}', origin_y=.5, y=.5-(i*.05))

p.add_script(Scrollable())
app.run()
