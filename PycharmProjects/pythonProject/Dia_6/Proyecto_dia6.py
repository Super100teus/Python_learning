import os
import shutil
from pathlib import Path
from os import system


def menu_iniciar():
    ruta = Path('C:/Users/BatMa/OneDrive/Escritorio/Trabajos/Curso_python/Recetas')
    op = 0
    while op != 6:
        try:
            menu = '''_____MENU DE OPCIONES_____
                                 1 . - Leer receta
                                 2 . - Crear receta
                                 3 . - Crear categoria
                                 4 . - Eliminar receta
                                 5 . - Eliminar categoria
                                 6 . - Finalizar programa'''
            print(menu)
            op = int(input('Ingresa una opcion .. '))
            match op:
                case 1:
                    system('cls')
                    lista = generar_lista(ruta)
                    print(f'\n\n\n{lectura(lista)}\n\n\n')
                case 2:
                    system('cls')
                    lista = generar_lista(ruta)
                    crea_receta(ruta, lista)
                case 3:
                    system('cls')
                    crea_categoria(ruta)
                case 4:
                    system('cls')
                    lista = generar_lista(ruta)
                    elimina_receta(ruta, lista)
                case 5:
                    system('cls')
                    lista = generar_lista(ruta)
                    elimina_categoria(ruta, lista)
                case 6:
                    system('cls')
                    print('Fin del codigo')
        except ValueError:
            print('Intenta ingresando valores numericos entre 1-6')


def elimina_categoria(direccion, lis):
    elegir_carpeta, cont_clases = 0, 0
    aux = []
    ruta = direccion
    ruta_eliminatoria, retorno, receta_eliminar = '', '', ''
    while elegir_carpeta not in range(1, cont_clases+1):
        try:
            print('Las categorias son las siguientes :')
            for i, v in enumerate(lis):
                print(f'{i + 1} . - {v[0]}')
                cont_clases += 1
            print('0 . - Volver al menu principal')
            elegir_carpeta = int(input('Ingresa el numero de la categoria que quieres eliminar .. : '))
            if 1 <= elegir_carpeta <= cont_clases:
                ruta_eliminatoria = ruta / f'{lis[elegir_carpeta - 1][0]}'
                shutil.rmtree(ruta_eliminatoria)
                print('\n\n Categoria eliminada!!! \n\n')
            elif elegir_carpeta == 0:
                return ''
            else:
                elegir_carpeta = 0
                print(f'Intenta el rango de valores 1-{cont_clases}')
        except ValueError:
            print('\n\nIntenta con un valor numerico\n\n')
            elegir_carpeta = 0


def elimina_receta(direccion, lis):
    elegir_carpeta, elegir_receta, cont_clases = 0, 0, 0
    aux = []
    ruta = direccion
    ruta_eliminatoria, retorno, receta_eliminar = '', '', ''
    while elegir_carpeta not in range(1, cont_clases+1):
        print('Las categorias son las siguientes :')
        for i, v in enumerate(lis):
            print(f'{i + 1} . - {v[0]}')
            cont_clases += 1
        print('0 . - Volver al menu principal')
        print(f'contador : {cont_clases}')
        elegir_carpeta = int(input('Ingresa el numero de la categoria a la que quieres acceder .. : '))
        if 1 <= elegir_carpeta <= cont_clases :
            ruta_eliminatoria = ruta / f'{lis[elegir_carpeta-1][0]}'
            for i in range(len(lis[elegir_carpeta-1]) - 1):
                print(f'Receta {i + 1} : {lis[elegir_carpeta-1][i + 1]}')
                aux.append(lis[elegir_carpeta-1][i + 1])
            print('Volver 0 : Volver al menu principal')
            while elegir_receta not in range(1, (len(aux)) + 1):
                elegir_receta = int(input('Elige el numero de la receta que deseas eliminar .. : '))
                if 1 <= elegir_receta <= len(aux):
                    receta_eliminar = aux[elegir_receta-1]
                    ruta_eliminatoria = ruta_eliminatoria / f'{receta_eliminar}.txt'
                    os.remove(ruta_eliminatoria)
                    print('\n\n Receta eliminada!!! \n\n')
                elif elegir_receta == 0:
                    return ''
                else:
                    print(f'Ingresa valor dentro del rango 1-{len(aux)}')
        elif elegir_carpeta == 0:
            return ''
        else:
            print(f'Ingresa valores en el rango de 1-{cont_clases}')


def crea_categoria(direccion):
    elegir_categoria, categoria_cont = 0, 0
    categ_nom, crear_categ, si_o_no, ruta_actual = '', '', '', ''
    system('cls')
    si_o_no = input('Deseas crear una nueva categoria? (si/no) .. ')
    if si_o_no == 'si':
        categ_nom = input('Introduce el nombre de la nueva categoria : ')
        ruta_actual = os.chdir(direccion)
        crear_categ = os.makedirs(direccion / categ_nom)
    else:
        return ''


def crea_receta(direccion, lis):
    elegir_categoria, cont_clases = 0, 0
    receta_nom, categoria, nueva_ruta, archivo, contenido, si_o_no, aux = '', '', '', '', '', 'si', ''
    print('Las categorias son las siguientes :')
    for i, v in enumerate(lis):
        print(f'{i + 1} . - {v[0]}')
        cont_clases += 1
    print('0 . - Volver al menu principal')
    while elegir_categoria not in range(1, cont_clases+1):
        print(cont_clases)
        elegir_categoria = int(input('Ingresa el numero de la categoria a la que quieres acceder .. : '))
        if 1 <= elegir_categoria <= cont_clases:
            receta_nom = input('Ingrece el nombre de la receta que escribira .. ')
            categoria = lis[elegir_categoria-1][0]  # Guardo nombre de la caegoria a la que se le añadira una nueva receta
            nueva_ruta = os.chdir(direccion / categoria)  # Cambio la ruta en la que python trabaja a esta
            archivo = open(f'{receta_nom}.txt', 'w')
            while si_o_no == 'si':
                aux = input('Ingrese la linea de su receta a continuacion .. ')
                contenido += f'{aux}\n'
                si_o_no = input('Escribir otra linea (si/no) .. ')
                si_o_no = si_o_no.lower()
            archivo.write(contenido)
            archivo.close()
            print('\n\n Receta creada!!!!\n\n')

        elif elegir_categoria == 0:
            return ''
        else:
            print(f'Numero no valido in tenta con uno de entre el sig. rango: 1-{cont_clases}')


def lectura(lis):
    elegir_carpeta, elegir_receta, cont_clases = 0, 0, 0
    aux = []
    ruta = Path('C:/Users/BatMa/OneDrive/Escritorio/Trabajos/Curso_python/Recetas')
    archivo_a_importar, retorno = '', ''
    print('Las categorias son las siguientes :')
    for i, v in enumerate(lis):
        print(f'{i+1} . - {v[0]}')
        cont_clases = i
    print('0 . - Volver al menu principal')
    while elegir_carpeta != range(1, cont_clases):
        elegir_carpeta = int(input('Ingresa el numero de la categoria a la que quieres acceder .. : '))
        if 1 <= elegir_carpeta <= cont_clases + 1:
            elegir_carpeta = elegir_carpeta - 1
            archivo_a_importar = ruta / f'{lis[elegir_carpeta][0]}'
            for i in range(len(lis[elegir_carpeta]) - 1):
                print(f'Receta {i + 1} : {lis[elegir_carpeta][i + 1]}')
                aux.append(lis[elegir_carpeta][i + 1])
            print('Volver 0 : Volver al menu principal')
            while elegir_receta != range(1, (len(aux))+1):
                elegir_receta = int(input('Elige el numero de la receta que deseas leer .. : '))
                if 1 <= elegir_receta <= len(aux):
                    elegir_receta = elegir_receta - 1
                    print(aux[elegir_receta])
                    archivo_a_importar = archivo_a_importar / f'{aux[elegir_receta]}.txt'
                    mi_archivo = open(archivo_a_importar)
                    retorno = mi_archivo.read()
                    mi_archivo.close()
                    return retorno
                elif elegir_receta == 0:
                    return ''
                else:
                    print('Numero no valido intenta de nuevo, lee bien las opciones')
        elif elegir_carpeta == 0:
            return ''
        else:
            system('cls')
            print(f'Debes ingresar un numero entre 1 y {cont_clases+1} ')


def generar_lista(dirct):
    folders = []
    aux = []
    nueva_dir = ''
    for categoria in Path(dirct).glob('*/'):
        aux = []
        nueva_dir = f'{dirct}/{categoria.stem}'
        aux.append(categoria.stem)
        for u in Path(nueva_dir).glob('*.txt'):
            aux.append(u.stem)
        folders.append(aux)
    return folders


menu_iniciar()
