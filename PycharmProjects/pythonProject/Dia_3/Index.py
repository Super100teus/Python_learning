mi_texto = "Esto es una prueba"
resultado = mi_texto[0]  # Me da el caracter dentro de la cadena que se encuentre en el indice especificado dentro de
# los corchetes
resultado2 = mi_texto.index("a")  # Puedo buscar un caracter nada mas o una cadena entera si buco una cadena entera me
# dara el indice en donde empieza
print(resultado, resultado2)
resultado2 = mi_texto.index("a", 11)  # Aqui empezara a buscar a partir del indice 11
print(resultado2, type(resultado2))
resultado3 = mi_texto.index("e", 11, 16)  # Aqui empezara a buscar a partir del indice 11 hasta antes del indice 16
print(resultado3)  # Si no encuentra el caracter en la cadena o rango especificado arrojara una ecepcion
resultado2 = mi_texto.rindex("a")  # Este metodo rindex busca de derecha a izquierda en vez de izquierda a derecha ,
# por lo que dara el primer caracter que encuentre de derecha a izquierda
print(resultado2)
