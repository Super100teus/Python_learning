from pathlib import Path
import shutil
import os
import send2trash
print(os.getcwd())
'''archivo = open('aprendiendo_mover_archivos.txt', 'w')
archivo.write('Veamos si podemos mover esta mamada')
archivo.close()
print(os.listdir())'''  # El codigo anterior creo un archivo en el directorio en el que este modulo se encuentra

# shutil.move('aprendiendo_mover_archivos.txt',  # Movi el archivo a la segunda ruta
#            'C:\\Users\\BatMa\\OneDrive\\Escritorio\\Trabajos\\Curso_python\\carpeta_prueba')

"""shutil.rmtree()    este metodo elimina una carpeta que especifiques con todos los archivos,
es irreversible no es lo mas recomendable usarlo"""

# Este metodo lo envia a la papelera, no es tan riesgoso como shutil.rmtree()
# send2trash.send2trash('aprendiendo_mover_archivos.txt') da error esta linea por que ya se elimino el archivo
print(os.walk('C:\\Users\\BatMa\\OneDrive\\Escritorio\\Trabajos\\Curso_python\\Recetas'))  # Mostrara el lugar en
# memoria es un generator (yield)
ruta = Path('C:/Users/BatMa/OneDrive/Escritorio/Trabajos/Curso_python/Recetas')

for carpeta, subcarpeta, archivo in os.walk(ruta):
    print(f'En la carpeta ruta: {carpeta}')
    print('Las subcarpetas son:')
    for sub in subcarpeta:
        print(f'\t{sub}')
    print('Los archivos son:')
    for arc in archivo:
        print(f'\t{arc}')

