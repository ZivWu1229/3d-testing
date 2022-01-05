from ursina import *
from ursina import collider
from ursina import texture
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()
rotations = {'d':(0,0,0),'n':(90,0,0),'e':(0,0,90)}
obj = []

class Handing_items(Entity):
    def __init__(self):
        super().__init__(
            parent=camera.ui,
            model='cube',
            texture='planks',
            rotation=(22.5,45,45),
            position=(0.5,-0.5,0),
            scale=0.5
        )

class Floor(Button):
    def __init__(self, pos=(0,-10,0), side='d'):
        global rotations
        super().__init__(
            parent=scene,
            model='cube',
            scale=(5,1,5),
            rotation=rotations[side],
            position=pos,
            texture='planks',
            highlight_color=color.rgba(50,50,255,100),
            color=color.white,
            collider=Quad(scale=(1,1,1))
        )
    def on_click(self):
        pass

def update():
    if player.y < -10:
        player.position = (0,0,0)

obj.append(Floor())

handing_items = Handing_items()
player = FirstPersonController()

app.run()