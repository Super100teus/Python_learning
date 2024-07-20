import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Crea una figura 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')  # Está creando un conjunto de ejes en un diseño de cuadrícula de 1 fila por
# 1 columna, y el tercer número (1) indica que estamos trabajando en el primer conjunto de ejes
# projection 3d es un argumento que esta configurando ejes 3d
# Define las coordenadas de la figura 3D (por ejemplo, un cubo)
vertices = np.array([[0, 0, 0],
                     [1, 0, 0],
                     [1, 1, 0],
                     [0, 1, 0],
                     [0, 0, 1],
                     [1, 0, 1],
                     [1, 1, 1],
                     [0, 1, 1]])

# Define las aristas del cubo
aristas = [[0, 1], [1, 2], [2, 3], [3, 0], # Aqui se define que  vertices se une con cual, si se modifica algo aqui notara que los cubos dejan de ser cubos
           [4, 5], [5, 6], [6, 7], [7, 4],
           [0, 4], [1, 5], [2, 6], [3, 7]]

# Dibuja las aristas del cubo
for arista in aristas:
    ax.plot(*vertices[arista, :].T, color='b')

# Aplica una traslación
traslacion = np.array([5, 5, 5]) # punto de vision y rango de movimiento en el plano cartesiano
vertices_traslacion = vertices + traslacion

# Dibuja las aristas del cubo trasladado
for arista in aristas:
    ax.plot(*vertices_traslacion[arista, :].T, color='r')

# Aplica una rotación (por ejemplo, rotación en el eje Z)
angulo_rotacion = np.pi / 4
matriz_rotacion = np.array([[np.cos(angulo_rotacion), -np.sin(angulo_rotacion), 0],
                            [np.sin(angulo_rotacion), np.cos(angulo_rotacion), 0],
                            [0, 0, 1]])
vertices_rotacion = np.dot(vertices_traslacion, matriz_rotacion)

# Dibuja las aristas del cubo trasladado y rotado
for arista in aristas:
    ax.plot(*vertices_rotacion[arista, :].T, color='g')

# Ajusta los límites del gráfico
ax.set_xlim([0, 7])
ax.set_ylim([0, 7])
ax.set_zlim([0, 7])

# Muestra el gráfico
plt.show() # Se mueve con el raton
