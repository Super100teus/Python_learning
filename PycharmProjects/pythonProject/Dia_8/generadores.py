"""
La palabra yield lo que hace es retornar un valor de una funcion pero solo cuando se necesita
es decir solo cuando el programa necesite un valor de la lista que retorna pero solamente genera
ese valor los demas no son generados hasta que se ocupen, este metodo hace que el rendimiento de
espacio sea muy superior cuando se trabaja datos muy estensos y abarca mucho espacio de memoria
"""


def funcion():
    lis = []
    for i in range(1, 6):
        lis.append(i * 10)
    return lis


def generador():
    for i in range(1, 6):
        k = yield i * 10
        #yield i * 10


print(funcion())
print(generador())
g = generador()
print(next(g))  # Me da el siguiente numero en la iteracion
print(next(g))


def mi_generador():
    w = 1
    yield w
    w += 1
    yield w
    w += 5
    yield w


d = mi_generador()
print(next(d))
print(next(d))
print(next(d))


