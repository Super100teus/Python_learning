import matplotlib.pyplot as plt
import numpy as np

# Crea una secuencia de imágenes de ejemplo con colores diferentes
frames = []
colors = [(1, 0, 0), (0, 1, 0), (0, 0, 1), (1, 1, 0), (0, 1, 1)]
for color in colors:
    frame = np.zeros((100, 100, 3))  # Imagen en blanco de 100x100 píxeles , y el numero 3 representa los 3 canales de
    # color tipicos rgb
    frame[:, :, :] = color  # Establece el color en toda la imagen
    frames.append(frame)

# Configura la visualización
fig, ax = plt.subplots()
ax.set_aspect('equal')  # Este método se llama en el objeto de ejes para establecer la relación de aspecto del gráfico.
# En este caso, se establece en 'equal', lo que significa que se asegura de que la escala sea igual en ambas direcciones
ax.axis('off')  # Se hace esta linea para desactivar lineamientos y señalamientos en los graficos
plt.subplots_adjust(left=0.1, right=.9, top=.9, bottom=0.1)  # Ajusto los margenes (valores desde 0 a 0.9)

# Muestra las imágenes con transparencia
for i, frame in enumerate(frames):
    alpha = 0.5  # Nivel de transparencia
    ax.imshow(frame, alpha=alpha)
    plt.pause(1)  # Pausa para mostrar cada imagen

plt.show()