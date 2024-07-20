import random
import re


def entrada(caracter, avance, vidas, palabra, lis):
    longitud = len('')
    avance_lis = list(avance)
    nuevo_avance = ''
    mensaje = ''
    for i, v in enumerate(palabra):
        v_minusculo = v.lower()
        v_mayusculo = v.upper()
        if caracter == v or caracter == v_minusculo or caracter == v_mayusculo :
            avance_lis[i] = v

    nuevo_avance = ''.join(avance_lis)
    mensaje =f'''\n\n\n\n\n\n\n_______________________________________T  U______A  V  A  N  C  E_______________________________________
    --------------------------------------------------------------------------------------------------------------------
    
                        V  I  D  A  S  :  {vidas}           P  A  L  A  B  R  A  :  {nuevo_avance}           P  A  L  A  B  R  A  S      U  S  A  D  A  S  : {lis}
    
    --------------------------------------------------------------------------------------------------------------------
\n\n\n\n\n\n\n'''
    print(mensaje)
    return nuevo_avance


def caracteres_individuales(palabra):
    palabra = palabra.lower()
    pal_mutable = palabra
    pal_nueva = ''
    pal_unica = ''
    for i in palabra:
        pal_nueva += min(pal_mutable)
        pal_mutable = pal_mutable.replace(min(pal_mutable), '', 1)
    for i in pal_nueva:
        if i not in pal_unica:
            pal_unica += i
    return len(pal_unica)


def comenzar():
    # choice() : Elige un elemento aleatorio de una secuencia, como una lista o una tupla.
    palabras = ['Leon', 'Black-Noar', 'Nolan Grayson', 'Harry potter 7', 'Maze Runner', 'El 7 machos', 'El origen',
                'Gen-V', 'The Boys', 'El planeta de los simios', 'Toyota tacoma', 'Japones', 'Estrella azul']
    palabra = random.choice(palabras)
    vidas = 6
    gana = caracteres_individuales(palabra)
    lis = []
    palabra_incognita = '_' * len(palabra)
    nueva_incognita = ''
    print(f'\n\nA continuacion comenzara el juego donde cada cierto momento en el juego veras la siguiente informacion:'
          f'\n\n                                     '
          f'                vidas : {vidas}                        palabra: {palabra_incognita}\n\n'
          f'Es el juego del ahorcado, como viste tienes 6 vidas las cuales iran decreciendo segun te equivoques,'
          f'buena suerte')
    while vidas != 0 and gana != 0:
        intento = '  '
        print("  D  E  B  U  G  G  E  A  N  D  O")
        while len(intento) != 1:
            intento = input('Ingresa el caracter .. ')
            if len(intento) == 1:
                verdad_o_no = validar_entrada(intento, palabra, lis)
                if verdad_o_no:
                    gana += -1
                    lis.append(intento.lower())
                    lis.append(intento.upper())
                    nueva_incognita = entrada(intento, palabra_incognita, vidas, palabra, lis)
                    palabra_incognita = nueva_incognita
                else:
                    print('____________________________Te equivocaste______________________________')
                    vidas += -1
                    lis.append(intento.lower())
                    lis.append(intento.upper())
                    nueva_incognita = entrada(intento, palabra_incognita, vidas, palabra, lis)
                    palabra_incognita = nueva_incognita


            else:
                print('Ingresaste mas de un caracter o cero caracteres , solo ingresa uno')

    if vidas == 0:
        print('Perdiste el juego')
    else:
        print('Ganaste puto perro ')


def validar_entrada(entrada, palabra, palabras_usadas):
    patron = re.compile("^[a-zA-Z0-9_\\-\\s]+$")
    if patron.match(entrada):
        if (entrada in palabra and entrada not in palabras_usadas) or (entrada in palabra.lower() and entrada not in palabras_usadas) or (entrada in palabra.upper() and entrada not in palabras_usadas):
            return True
        else:
            return False
    else:
        return False


comenzar()
