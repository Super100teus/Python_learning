"""Proyecto en el que aplicare lo aprendido en el dia 9"""
from collections import *
import shutil
import os
import send2trash
from datetime import *
import math
import re
import time
import timeit
from pathlib import Path


def mi_funcion():
    ruta = 'C:/Users/BatMa/PycharmProjects/pythonProject/Dia_9/P_dia_9/Mi_Gran_Directorio'
    respuesta = """"""
    ruta_leer = ''
    abrir_arc = ''
    contenido = ''
    lis = []
    regex = r'(N[\S\D]{3}\-\d{5})'
    fecha_hoy = datetime.today()
    anio = fecha_hoy.year
    mes = fecha_hoy.month
    dia = fecha_hoy.day
    num_serie = 0
    arc_noms = ""
    serie_noms = ""
    nums_cont = 0
    for carpeta, subcarpeta, archivo in os.walk(ruta):
        print('Las subcarpetas son:')
        for sub in subcarpeta:
            print('\t{sub}')
        print('Los archivos son:')
        for arc in archivo:
            ruta_leer = f'{carpeta}/{arc}'
            abrir_arc = open(ruta_leer)
            contenido = abrir_arc.read()
            abrir_arc.close()
            p_encontrado = re.search(regex, contenido)
            if p_encontrado:
                arc_noms += f'  {arc}   {p_encontrado.group()}\n'
                serie_noms += f'{p_encontrado.group()}\n                '
                nums_cont += 1
            print('\t{arc}')
    lis.append(arc_noms)
    lis.append(serie_noms)
    lis.append(nums_cont)
    lis.append(f'{anio}/{mes}/{dia}')
    return lis


declaracion = '''
mi_funcion()
'''
setup = """
def mi_funcion():
    from datetime import datetime
    import os
    import re
    
    ruta = 'C:/Users/BatMa/PycharmProjects/pythonProject/Dia_9/P_dia_9/Mi_Gran_Directorio'
    ruta_leer = ''
    abrir_arc = ''
    contenido = ''
    lis = []
    regex = r'(N[\S\D]{3}\-\d{5})'
    fecha_hoy = datetime.today()
    anio = fecha_hoy.year
    mes = fecha_hoy.month
    dia = fecha_hoy.day
    num_serie = 0
    arc_noms = ""
    serie_noms = ""
    nums_cont = 0
    for carpeta, subcarpeta, archivo in os.walk(ruta):
        print('Las subcarpetas son:')
        for sub in subcarpeta:
            print('\t{sub}')
        print('Los archivos son:')
        for arc in archivo:
            ruta_leer = f'{carpeta}/{arc}'
            abrir_arc = open(ruta_leer)
            contenido = abrir_arc.read()
            abrir_arc.close()
            p_encontrado = re.search(regex, contenido)
            if p_encontrado:
                arc_noms += f'  {arc}   {p_encontrado.group()}'
                serie_noms += f'{p_encontrado.group()}                '
                nums_cont += 1
            print('\t{arc}')
    lis.append(arc_noms)
    lis.append(serie_noms)
    lis.append(nums_cont)
    lis.append(f'{anio}/{mes}/{dia}')
    return lis
"""

# El mayor error que tuve es en la sig linea se debia a que en el setup no importaba las librerias
# necesarias la tabulacion en el resultado no es la mejor pero aun asi se consigui la informacion
# necesaria, una posicion del arreglo que devuelve la funcion 'mi_funcion' es redundante pero asi
# lo dejare tambien solo lo dejare comentado para que se tome en cuenta
duracion = timeit.timeit(declaracion, setup, number=10)
t_redondeado = math.ceil(duracion)
lis = mi_funcion()
resultado_f = f"""   Fecha de busqueda: {lis[3]}
----------------------------------
    ARCHIVO     NRO. SERIE
    -------     ----------
{lis[0]}
    
    Numeros encontrados: {lis[2]}
    Duracion de la ejecucion: {t_redondeado} segundo/s
    """
print(resultado_f)

"""
Necesitamos el metodo read() para leer los archivos (es parte de open(archivo)), la iteracion con el metodo
walk() de os:
*****************************************************************************************
ruta = 'C:\\Users\\BatMa\\OneDrive\\Escritorio\\Trabajos\\Curso_python\\Recetas'

for carpeta, subcarpeta, archivo in os.walk(ruta):
    print(f'En la carpeta ruta: {carpeta}')
    print('Las subcarpetas son:')
    for sub in subcarpeta:
        print(f'\t{sub}')
    print('Los archivos son:')
    for arc in archivo:
        print(f'\t{arc}')
******************************************************************************************
despues con expresiones regulares podemos conseguir el grupo de captura del patron deseado en cada archivo
*************************************************************

texto2 = "En caso de emergencia llama al 345-456-9721"
regex2 = r'(\d){3}-(\d){3}-(\d){4}'
res = re.search(regex2, texto2)
print(res)
print(res.group())
*************************************************************
Finalmente utilizar el metodo today() para  obtener la fecha actual en todo momento,
tratar de hacerlo en formato dd/mm//yyyy
"""
