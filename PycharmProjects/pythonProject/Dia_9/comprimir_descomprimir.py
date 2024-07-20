"""Aprenderemos a usar zipfile, shutil   para comprimir y descomprimir archivos programaticamente"""
import zipfile
import shutil

'''# Este codigo comprime los 2 archivos especificados en una sola carpeta
mi_zip = zipfile.ZipFile('archivo_comprimido.zip', 'w')
mi_zip.write('C:\\Users\\BatMa\\OneDrive\\Escritorio\\Trabajos\\Lenguajes_y_Automatas\\diagrama_de_sintaxis.txt')
mi_zip.write('C:\\Users\\BatMa\\OneDrive\\Escritorio\\Trabajos\\Lenguajes_y_Automatas\\Muestra.txt')
mi_zip.close()'''

'''# El sig codigo descomprime los archivos\
zip_abierto = zipfile.ZipFile('archivo_comprimido.zip', 'r')
zip_abierto.extractall()'''


"""# Esta es la manera que mas comoda se hace para comprimir y descomprimir archivos
origen = 'C:\\Users\\BatMa\\OneDrive\\Escritorio\\Trabajos\\Lenguajes_y_Automatas'
destino = 'Todo comprimido'
shutil.make_archive(destino, 'zip', origen)"""
# En el segundo parametro puedo especificar otra ruta completa para guardar en otro lado
shutil.unpack_archive('proyecto+Dia+9.zip', 'P_dia_9', 'zip')


