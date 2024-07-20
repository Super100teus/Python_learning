"""
Este modulo es para analizar que bloque de codigo es mas eficiente con
respecto al tiempo
"""

import time
import timeit

def p_for(num):
    lista = []
    for i in range(1, num + 1):
        lista.append(i)
    return lista


def p_while(num):
    lista = []
    cont = 1
    while cont <= num:
        lista.append(cont)
        cont += 1
    return lista


print(p_for(90))
print(p_while(90))
inicio = time.time()
p_for(7000)
final = time.time()
print(final - inicio)
inicio = time.time()
p_while(7000)
final = time.time()
print(final - inicio)

declaracion = """
p_for(10)
"""
mi_setup = """
def p_for(num):
    lista = []
    for i in range(1, num + 1):
        lista.append(i)
    return lista
"""
duracion = timeit.timeit(declaracion, mi_setup, number=1000)
print('\n*************** timeit ***************\n')
print(duracion)
declaracion2 = """
p_while(10)
"""
mi_setup2 = """
def p_while(num):
    lista = []
    cont = 1
    while cont <= num:
        lista.append(cont)
        cont += 1
    return lista
"""
declaracionn = '''
mi_funcion()
'''
setup = """
def mi_funcion():
    ruta = Path('C:/Users/BatMa/PycharmProjects/pythonProject/Dia_9/P_dia_9/Mi_Gran_Directorio')
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
        print(f'En la carpeta ruta: {carpeta}')
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
                arc_noms += f"{arc}\n"
                serie_noms += f"{p_encontrado.group()}\n"
                nums_cont += 1
            print('\t{arc}')
    lis.append(arc_noms)
    lis.append(serie_noms)
    lis.append(nums_cont)
    lis.append(f'{anio}/{mes}/{dia}')
    return lis
    """
duracion2 = timeit.timeit(declaracion2, mi_setup2, number=1000)
print(duracion2)
