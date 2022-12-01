from ursina import *

class Hand(Entity):
    
    def __init__(self):
        super().__init__(
            parent = camera.ui,
            model = 'assets/arm',
            texture = load_texture('assets/arm_texture.png'),
            scale = .2,
            rotation = Vec3(150, -10, 0),
            position = Vec2(.4, -.6),
        )

    # cuando la mano está activa
    def activo(self):
        self.position = Vec2(.3, -.5)
    # cuando la mano está inactiva
    def inactivo(self):
        self.position = Vec2(.4, -.6)

    # hardware input
    def input(self, key):
        # ejecutamos la función activo si el botón izquierdo o derecho del mouse son presionados
        if key == 'left mouse down' or key == 'right mouse down':
            self.activo()
        else:
            self.inactivo()