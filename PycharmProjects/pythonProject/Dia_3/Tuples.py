mi_tuple = (1, 2, 3, 4)  # Las tuplas son inmutables
print(type(mi_tuple))
t = (12, 23.1, 'hola', ('u', 6, 73.3))
print(t[-1][1])
t = list(t)
print(type(t))
t = tuple(t)
print(type(t))
tt = (1, 2, 3)
x, y, z = tt  # Esto funciona con listas tambien
print(x, y, z)
ttt = (1, 2, 3, 1)
print(ttt.count(1))  # Este metodo cuenta cuantas veces aparece un valor especificado (el parametro es el valor)
# dentro de la tupla
print(ttt.index(1))
# Aqui consultaras el indice de el valor que especifiques estos ultimos 2 metodos se pueden usar en listas

