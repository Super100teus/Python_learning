import os
from pathlib import Path


ruta = os.getcwd()  # getcwd = get current working directory
print(ruta)
ruta = os.chdir('C:\\Users\\BatMa\\OneDrive\\Escritorio\\Trabajos\\Curso_python')
archivo = open('otro_ejercicio.txt')
print(archivo.read())
archivo.close()
# ruta = os.makedirs('C:\\Users\\BatMa\\OneDrive\\Escritorio\\Trabajos\\Curso_python\\carpeta_prueba') Esta linea la
# ejecute una vez por que intenta crear una carpeta nueva y ya que es creada da un error por que no puede crear una
# carpeta ya existente
ruta2 = os.chdir('C:\\Users\\BatMa\\OneDrive\\Escritorio\\Trabajos\\Curso_python\\carpeta_prueba')
# os.chdir = Change the current working directory to the specified path.
archivo = open('Nuevo22.txt', 'w')  # Una vez cambiado el directorio al especificado el archivo a continuacion se creara
# dentro de la ultima carpeta especificada por este metodo os.chdir()
archivo.write(' Creando un nuevo archivo y carpeta al mismo tiempo Creando un nuevo archivo y carpeta al mismo tiempo Creando un nuevo archivo y carpeta al mismo tiempo')
nombre = os.path.basename('C:\\Users\\BatMa\\OneDrive\\Escritorio\\Trabajos\\Curso_python\\carpeta_prueba\\Nuevo2.txt')
# La linea con el metodo os.path.basename() extrae el nombre de el archivo
print(nombre)
nombre = os.path.split('C:\\Users\\BatMa\\OneDrive\\Escritorio\\Trabajos\\Curso_python\\carpeta_prueba\\Nuevo2.txt')
# La linea con el metodo os.path.split() extrae el nombre de el archivo en una tupla junto a su direccionf
print(nombre)
archivo.close()
# os.rmdir('C:\\Users\\BatMa\\OneDrive\\Escritorio\\elimina')
# os.rmdir() = remove directory remueve la carpeta indicada


# **********************************************************************************************************************
# **********************************************************************************************************************
# **************************                                                              ******************************
# ************************** INGRESAR DIRECCIONES VALIDAS EN TODOS LOS SITEMAS OPERATIVOS ******************************
# **************************                                                              ******************************
# **********************************************************************************************************************
# **********************************************************************************************************************


carpeta = Path('C:/Users/BatMa/OneDrive/Escritorio/Trabajos/Curso_python')  # De esta manera hacemos que las direcciones
# funcionen por igual en linux, Mac o Windows
archivo_a_importar = carpeta / 'otro_ejercicio.txt'
mi_archivo = open(archivo_a_importar)
print(mi_archivo.read())
