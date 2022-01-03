from ursina import *
from ursina import collider
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()
rotations = {'d':(0,0,0),'n':(90,0,0),'e':(0,0,90)}
obj = []

class Floor(Entity):
    def __init__(self, pos=(0,0,0), side='d'):
        super().__init__(
            parent=scene,
            model='plane',
            collision=True,
            collider='plane',
            scale=(10,1,10),
            rotation=self.rotation[side],
            position=pos
        )

obj = Floor()

player = FirstPersonController()

app.run()