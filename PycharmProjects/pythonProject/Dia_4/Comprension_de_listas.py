palabra = 'Python'
lista = []
for letra in palabra:
    lista.append(letra)
print(lista)
lis = [le for le in palabra]  # Es otra forma de de hacer lo mismo que lo anterior pero mas rapido
print(lis)
lis2 = [n for n in range(0, 22) if 7 < n < 18]  # Es otra forma de de hacerlo pero mas rapido, en caso de querer poner
# la condicion con un else se debe poner toda la condicion despues de la primera variable dentro de la lista
print(lis2)
lis3 = [n if 7 < n < 18 else 'no' for n in range(0, 22)]
print(lis3)
pies = [10, 12, 13, 67, 34]
metros = [m * .3048 for m in pies]
print(metros)
