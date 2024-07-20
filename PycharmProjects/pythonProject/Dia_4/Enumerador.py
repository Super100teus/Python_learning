lista = ['a', 'b', 'c']
for i in enumerate(lista):  # Me escribe el indice seguido de su valor correspondiente , entre parentesis, el enumerate
    # lo que hace basicamente es enumerar cada iteracion del bucle, no es que consiga en si el indice
    print(i)
print('-----------------------')
for i, v in enumerate(lista):  # Hace lo mismo que el anterior ciclo pero sin parentesis
    print(i, v)
print('-----------------------')
for i, v in enumerate(range(13, 19)):
    print(i, v)
print('-----------------------')
mis_tuples = list(enumerate(lista))  # Crea una lista de tuplas
print(mis_tuples)
print(mis_tuples[1][1])
print('-----------------------')
mis_tuples2 = tuple(enumerate(lista))  # Crea una tupla de tuplas
print(mis_tuples2)
print(mis_tuples2[1][1])
print('-----------------------')
mis_tuples3 = dict(enumerate(lista))  # Crea un diccionario, con la enumeracion de enumerate como clave y el valor
# corresponde al valor de la lista
print(mis_tuples3)
print(mis_tuples[1])
