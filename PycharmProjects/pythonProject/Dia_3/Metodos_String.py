texto = "\"Los anillos de poder son gobernados por el unico\""
resultado = texto.upper()
resultado_1 = texto[2].upper()
resultado_2 = texto.lower()
resultado_3 = texto.split()  # En este caso toma los espacios vacios como separador pero puede tomar lo que sea que
resultado_4 = texto.split("o")  # ponga dentro del parentesis, y convierte en lista la variable
print(resultado, "\n" + resultado_1, "\n" + resultado_2, "\n")
print(resultado_3)
print(type(resultado_3))
print(resultado_4)
a = "Sauron"
b = "es"
c = "dicipulo"
d = "de"
e = "alguien"
f = "mas"
g = "poderoso"
h = " ".join([a, b, c, d, e, f, g])  # Junta las cadenas separadas por un espacio en este caso, solo acepta valores de
# listas por lo que tuve que crear una lista dentro del metodo join
print(h)
resultado_5 = texto.find("u")  # Es igual que el metodo index, con la excepcion de que si el o los carecteres deseados
# no se encuentran no dara un error sino retornra un '-1', comprueba en el siguiente print
print(resultado_5)
resultado_6 = texto.replace("el unico", "Sauron, discipulo de Melkor conocido como .. Morgoth")  # Reemplaza el primer parametro del argumento por el
# segundo parametro y asi la cadena texto queda modificada
print(resultado_6)

