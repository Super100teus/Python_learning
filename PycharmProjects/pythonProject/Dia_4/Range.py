numeros = [1, 2, 33, 58, 90]
for u in range(4):  # Indice 0 hasta 3
    print(numeros[u])
    print('- ' + str(u))

print('\n_____________--------------_______________\n')

for u in range(1, 4):  # Variante de la utilizacion del rango en for, desde el indice 1 hasta el 3, el 3 si se incluye
    print(numeros[u])
    print('- ' + str(u))

print('\n_____________--------------_______________\n')

for u in range(1, 49, 7):  # Variante de la utilizacion del rango en for, el tercer parametro del range son los numeros
    # que avanza por iteracion
    print('- ' + str(u))

print('\n_____________--------------_______________\n')

lista = list(range(1, 590, 7))
print(lista)
