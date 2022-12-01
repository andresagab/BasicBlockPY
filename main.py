from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

# creamos nuestra aplicación con ursina
app = Ursina()

from Voxel import Voxel
from Sky import Sky
from Hand import Hand

# disabled windows elements
window.fps_counter.enable = False
window.exit_button.visible = False    

# definir el rango de visión
# 1 chunk = 16 x 256 x 166
chunkSize = 24
# generamos los bloques utilizando 2 ciclos, uno para el eje Z y otra para el eje X
# utilizamos la clase Voxel para crear nuestros cubos
for z in range(chunkSize):
    for x in range(chunkSize):
        voxel = Voxel(position = (x, 0, z))

# crear suelo
suelo = Entity(model = 'plane', collider = 'box', scale = chunkSize * chunkSize, color = color.orange)
suelo.position = Vec3(0, -100, 0)

# crear jugador
jugador = FirstPersonController()
# configurar salto del jugador
jugador.jump_up_duration = .7
# crear cielo
cielo = Sky()
# crear mano
mano = Hand()


# declaramos una variable para controlar la acción de correr
correr = False

# creamos una función que se ejecuta cada vez que recibimos una entrada de teclado
def input(key):
    # cuando presionamos el shift izquierdo
    if key == 'left shift':
        # hacemos el llamado a la variable global correr
        global correr
        correr = not correr
        if correr:
            jugador.speed = 10
        else:
            jugador.speed = 5

# función que se ejecuta con cada actualización de frame
def update():
    # reiniciar la posición del jugador
    if jugador.position.y <= suelo.position.y + 10:
        jugador.position = Vec3(1, 30, 1)

# ejectuar aplicación
app.run()

