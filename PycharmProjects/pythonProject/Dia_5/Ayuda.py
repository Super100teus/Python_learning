dic = {'1': 9, '2': 11, '3': 18}
a = dic.popitem()  # Retorna con la estructura LIFO (last in first out) la variable que retorna es la que se elimina
# Si poso el cursor sobre metodos o variables me salta informacion sobre ello , simantengo la tecla
# ctrl presionada sale informacion un poco diferente pero en escencia la misma
print(a)
print(dic)
e = "  op 'po' "
w = e.lstrip("  o")  # Este metodo elimina los caracteres del comienzo que se le especifique en los parametros , si no
# se especifica nada se eliminara por defecto todos los espacios en blanco del comienzo
print(w)
frutas = ["mango", "banana", "cereza", "ciruela", "pomelo"]
frutas.insert(3, 'naranja')
print(frutas)  # Inserta el elemento dado en el indice especificado
marcas_smartphones = {"Samsung", "Xiaomi", "Apple", "Huawei", "LG"}

marcas_tv = {"Sony", "Philips", "Samsung", "LG"}
con = marcas_tv.isdisjoint(marcas_smartphones)  # Esto dara True si el set no tiene elementos en comun con el otro

print(con)
