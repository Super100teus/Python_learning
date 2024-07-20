archivo = open('dia6_prueba.txt')  # No ocupo poner mas datos de direccion por que el archivo se encuentra en la misma
# carpeta que este archivo de python
print(archivo)  # Me muestra otros datos
print(archivo.readline().rstrip())  # Debo imprimir esto primero por que al usar estos metodos leen hasta un punto y
# guardan hasta ahi y la siguiente invocacion leera lo que se le indique desde el ultimo punto guardado con el metodo
# rstrip() se elimina el salto de linea para que en consola se vea mejor
print(archivo.readline())
print(archivo.read())  # Me muestra el archivo
archivo.close()  # Resguardar el espacio de memoria , buena practica
archivo = open('dia6_prueba.txt')
for linea in archivo:
    print(f'Aqui dice: {linea}')
archivo.close()
archivo = open('dia6_prueba.txt')
print(archivo.readlines())  # Esto crea una lista de las lineas
archivo.close()
