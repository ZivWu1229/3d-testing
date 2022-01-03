from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()
rotations = {'d':(0,0,0),'n':(90,0,0),'e':(0,0,90)}
obj = []

class Floor(Entity):
    def __init__(self, pos=(0,0,0), side='d'):
        global rotations
        super().__init__(
            parent=scene,
            model='plane',
            scale=(5,1,5),
            rotation=rotations[side],
            position=pos,
            texture='planks'
        )

obj = Floor()

player = FirstPersonController()

app.run()