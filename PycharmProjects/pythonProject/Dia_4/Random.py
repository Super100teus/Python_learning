from random import *
aleatorio = randint(1, 90)
doubles = round(uniform(1, 9), 3)  # Este metodo redondea el exceso de decimales al numero de decimales que quiera
ran1 = random()  # Aleatorio entre 0 y 1
colores = ['azul', 'verde', 'cafe', 'amarillo']
ran2 = choice(colores)
numeros = list(range(3, 79, 4))
shuffle(numeros)  # Mezcla aleatoriamente los valores de la lista, shuffle no puede ser usado con strings debido a que
# son inmutables
print(f'randint: {aleatorio} , uniform:{doubles} , random:{ran1} , choice:{ran2} , shuffle:{numeros}')
