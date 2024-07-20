mi_lista = ['c', 'a', 'g']
mi_lista2 = ['e', 'b', 'g']
mi_lista3 = mi_lista+mi_lista2  # Aqui si se guarda en una nueva lista, no ocupa slides
del(mi_lista[0:1])
res = len(mi_lista)
res1 = mi_lista[0]
print(f"{res} y  eltipo es {type(mi_lista)} res1:{res1}")
print(mi_lista3)
mi_lista3[0] = "Alfa"
print(mi_lista3)
mi_lista3.append('h')
print(mi_lista3)
mi_lista3.pop(2)  # Lo que interpreta pop si lo dejamos sin parametros es que quieres eliminar el ultimo elemento
eliminado = mi_lista3.pop()
print(mi_lista3)
print(eliminado)
mi_lista3.sort()  # Ordena la lista en orden alfabetico, este tipo de metodo no se puede guardar en una variable
print(mi_lista3)
mi_lista3.reverse()  # reverse ordena en orden alfabetico inverso osea de z a la a
print(mi_lista3)
