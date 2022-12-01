from ursina import *
import random

# creamos un diccionario de texturas
texturas = {
    # cesped
    'cesped' :
    {
        'textura': load_texture('assets/grass_block.png'),
        'sonido': Audio('assets/grass', loop = False, autoplay = False),
    },
    # piedra
    'piedra': {
        'textura': load_texture('assets/stone_block.png'),
        'sonido': Audio('assets/stone', loop = False, autoplay = False),
    },
    # ladrillo
    'ladrillo': {
        'textura': load_texture('assets/brick_block.png'),
        'sonido': Audio('assets/brick', loop = False, autoplay = False),
    },
    # tierra
    'tierra': {
        'textura': load_texture('assets/dirt_block.png'),
        'sonido': Audio('assets/dirt', loop = False, autoplay = False),
    },
}

# sonido al destruir un bloque
punchSound = Audio('assets/punch_sound', loop = False, autoplay = False)

# creamos una variable para determinar el bloque que estamos utilizando
bloque = 'cesped'

# creamos una clase denominada Voxel
class Voxel(Button):

    # constructor, se ejecuta cada vez que utilizamos esta clase
    def __init__(self, textura = texturas['cesped']['textura'], position = (0, 0, 0)):
        super().__init__(
            parent = scene,
            position = position,
            model = 'assets/block', # sphere, quad, plane
            origin_y = .5,
            texture = textura,
            color = color.color(0, 0, random.uniform(.9, 1)),
            scale = .5
        )

    # cuando hay un entrada de hardware
    def input(self, key):
        # use global vars
        global bloque
        # validamos si el bloque actual está siendo seleccionado
        if self.hovered:

            # agregar bloque al presionar el botón izquierdo del mouse
            if key == 'left mouse down':
                voxel = Voxel(texturas[bloque]['textura'], position = self.position + mouse.normal)
                texturas[bloque]['sonido'].play()

            # destruir bloque al presionar el botón derecho del mouse
            if key == 'right mouse down':
                punchSound.play()
                destroy(self)

        # keypad
        if key == '1':
            bloque = 'cesped'
        if key == '2':
            bloque = 'piedra'
        if key == '3':
            bloque = 'ladrillo'
        if key == '4':
            bloque = 'tierra'