mi_set = {1, 2, 3, 4, (1, 2, 3), 5, 1, 2, 3, 5}  # Esto se puede declarar tambien como v = set([1,2,3]) son inmutables y
# unicos los valores no se repiten, los objetos set no son subscribibles osease no tienen indice, no podemos operar con
# indices
print(type(mi_set))
print(mi_set)  # Los valores repetidos son descartados sin dar advertencia, los sets no tienen elementos repetidos
s1 = {1, 2, 3}
s2 = {3, 4, 5}
s3 = s1.union(s2)
print(len(mi_set))
print(2 in mi_set)
print(s3)
s4 = {2, 1, 3}
s4.add(4)
print(s4)
s4.remove(3)  # Si el elemento a eliminar no esta dara error
s4.discard(5)  # Si el elemento a descartar no esta no sucede absolutamente nada
s4.pop()  # Habiamos visto que si pop se utilizaba sin parametros se eliminaba el ultimo elemento , pero en un set no
# hay un orden por lo que no hay un ultimo valor entonces pop elemina un elemento de manera aleatoria
print(s4)
s4.clear()  # Elimina todo lo que hay en nuestro set
print(s4)
