import os
from pathlib import Path, PureWindowsPath
# Presta atencion en que el objeto Path de pathlib ayuda a trabajar con rutas y directorios
# independientes del sistema operativo
# Funciones no tienen parentesis funciones si? no estoy seguro alv
carpeta = Path('C:/Users/BatMa/OneDrive/Escritorio/Trabajos/Curso_python/otro_ejercicio.txt')  # De esta manera hacemos
# que las direcciones funcionen por igual en linux, Mac o Windows
print(carpeta.read_text())  # Me da lo que hay en el archivo de texto (.txt)
print(carpeta.name)  # Me da el nombre del archivo
print(carpeta.suffix)  # Me da la terminacion o sufijo, el tipo de archivo en realidad
print(carpeta.stem)  # Da el nombre del archivo sin su terminacion o sin su tipo de archivo
# Verifico la existencia del archivo
if carpeta.exists():
    print(' El archivo existe ')
else:
    print(' No existe ')

ruta_windows = PureWindowsPath(carpeta)
print(ruta_windows)  # Es el path del mismo archivo pero adptado a windows
