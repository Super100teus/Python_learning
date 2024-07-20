"""
Veremos como manipular ventanas emergentes y sus distintas herramientas
"""
import random

import pygame
from pygame import mixer

pygame.init()  # Inicializar pygame
ancho, alto = 1000, 571
pantalla = pygame.display.set_mode((ancho, alto))  # Fijo el tamaño de la pantalla, set_mode((ancho,alto)) en una tupla
# El modulo display es la forma en que vamos a ver lo que vayamos a invocar

# Titulo e icono
pygame.display.set_caption('Tu_vs_Trump')
icono = pygame.image.load('ovni.png')
pygame.display.set_icon(icono)
fondo = pygame.image.load('planetas.jpg')

# Agregar musica
mixer.music.load('The Legend of Zelda_ Ocarina of Time - Shop Theme Cover.mp3')
mixer.music.set_volume(.2)
mixer.music.play(-1)
sonido_proyectil = mixer.Sound('disparo.mp3')
sonido_colision = mixer.Sound('Golpe.mp3')

# Jugador
i_jugador = pygame.image.load('nave_espacial.png')
j_x = (ancho * 0.5) - 32
j_y = alto - 64
x = 0
y = 0

# Puntaje
puntaje = 0
fuente = pygame.font.Font('freesansbold.ttf', 32)
txt_x = 10
txt_y = 10

# Enemigo
i_enemigo = []
e_x = []
e_y = []
xe_cambio = []
ye_cambio = []
cantidad_enemigos = 8

# fuente final
fuente_final = pygame.font.Font('freesansbold.ttf', 30)

for e in range(cantidad_enemigos):
    i_enemigo.append(pygame.image.load('enemigo_trump.png'))
    e_x.append(random.randint(0, ancho - 32))
    e_y.append(random.randint(0, (alto - 350)))
    xe_cambio.append(.2)
    ye_cambio.append(50)


# Variables de proyectil
i_proyectil = pygame.image.load('misil_doble.png')
p_x = 0
p_y = j_y
xp_cambio = 0
yp_cambio = 3
proyectil_visible = False


def texto_final():
    texto = fuente_final.render(f'VALES VERGA', True, (255, 255, 255))
    pantalla.blit(texto, (400, 280))

# Funcion puntaje
def funcion_puntaje(pun_x, pun_y):
    texto = fuente.render(f'Puntaje: {puntaje}', True, (255, 255, 255))
    pantalla.blit(texto, (pun_x, pun_y))


# Funcion jugador
def juego(xj, yj):
    # Este metodo aplica los parametros que le des en pantalla
    pantalla.blit(i_jugador, (xj, yj))


# Funcion enemigo
def enemigos(x_e, y_e, ene):
    pantalla.blit(i_enemigo[ene], (x_e, y_e))


# Funcion proyectil
def proyectiles(x_e, y_e):
    global proyectil_visible
    proyectil_visible = True
    pantalla.blit(i_proyectil, (x_e + 20, y_e))


# Funcion colisiones
def colisiones(x1, x2, y1, y2):
    distancia = (((x1 - x2) ** 2) + ((y1 - y2) ** 2)) ** 0.5
    if distancia <= 24:
        return True
    else:
        return False


aux = True
while aux:
    # Imagen de fondo, (puede ser sistema de colores RGB)
    # pantalla.fill((18, 18, 40))
    pantalla.blit(fondo, (0, 0))
    for evento in pygame.event.get():
        # Terminar juego
        if evento.type == pygame.QUIT:
            aux = False
        if evento.type == pygame.KEYDOWN:

            # ** ** ** ** **  MOVIMIENTO HORIZONTAL  ** ** ** ** **
            if evento.key == pygame.K_LEFT:
                x = -2
            if evento.key == pygame.K_RIGHT:
                x = 2
            # ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** **

            # ** ** ** ** **  DISPARO  ** ** ** ** **
            if evento.key == pygame.K_SPACE:
                if not proyectil_visible:
                    p_y = j_y
                    p_x = j_x
                    proyectiles(p_x, p_y)
                    sonido_proyectil.play()
                '''else:
                    proyectil_visible = False'''

            # ** ** ** ** ** ** ** ** ** ** ** ** ***

            # ** ** ** ** ** MOVIMIENTO  VERTICAL ** ** ** ** **
            if evento.key == pygame.K_UP:
                y = -2
            if evento.key == pygame.K_DOWN:
                y = 2
            # ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** **

            # *** *** *** *** *** DETENER  INCREMENTO  DE  MOVIMIENTO *** *** *** *** ***
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                x = 0
            if evento.key == pygame.K_DOWN or evento.key == pygame.K_UP:
                y = 0
            # *** *** *** *** *** *** *** *** *** *** *** *** *** *** *** *** *** *** ***
    j_x += x
    j_y += y
    # ** ** ** ** ** ** VERIFICAR QUE EL JUGADOR NO SALGA DE LOS LIMITES ** ** ** ** ** **
    if j_x <= 0:
        j_x = 0
    if j_y <= 0:
        j_y = 0
    if j_x >= ancho - 64:
        j_x = ancho - 64
    if j_y >= alto - 64:
        j_y = alto - 64
    # ** ** ** ** *** *** *** ** *** ** *** ** ** ** * ** * * * * * ** ** ** ** * ** ** * **
    for e in range(cantidad_enemigos):



        e_x[e] += xe_cambio[e]
    # ** ** ** ** ** ** VERIFICAR QUE EL ENEMIGO NO SALGA DE LOS LIMITES ** ** ** ** ** **
        if e_x[e] <= 0:
            xe_cambio[e] = .8
            e_x[e] = 0
            e_y[e] += ye_cambio[e]
        if e_y[e] <= 0:
            e_y[e] = 0
            ye_cambio[e] = 50
        if e_x[e] >= ancho - 64:
            xe_cambio[e] = -0.8
            e_x[e] = ancho - 64
            e_y[e] += ye_cambio[e]
        if e_y[e] >= (alto * (3/4)):
            e_y[e] = (alto * (2/3))
            ye_cambio[e] = -50
            # ** ** * FIN DEL JUEGO *** ** * * * **
            for k in range(cantidad_enemigos):
                e_y[k] = 500
            texto_final()
            break
            # ** ** ** ** ** * *** * *** ** ** * **


    # ** ** ** ** *** *** *** ** *** ** *** ** ** ** * ** * * * * * ** ** ** ** * ** ** * **

    # ** ** ** ** ** ** MOVIMIENTO PROYECTIL ** ** ** ** ** **

        if p_y <= - 24:
            proyectil_visible = False
        if proyectil_visible:
            proyectiles(p_x, p_y)
            p_y += -yp_cambio
        coli = colisiones(p_x, e_x[e], p_y, e_y[e])
        if coli and proyectil_visible:
            sonido_colision.play()
            p_y = j_y
            proyectil_visible = False
            puntaje += 1
            e_x[e] = random.randint(0, ancho - 32)
            e_y[e] = random.randint(0, (alto - 350))

    # ** ** ** ** *** *** *** ** *** ** *** ** ** ** * ** * **

        enemigos(e_x[e], e_y[e], e)
    juego(j_x, j_y)
    funcion_puntaje(txt_x, txt_y)
    pygame.display.update()
