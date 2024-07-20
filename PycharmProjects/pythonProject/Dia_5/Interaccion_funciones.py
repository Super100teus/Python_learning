from random import shuffle

# Lista inicial
palos = ['-', '--', '---', '----', '-----']


# Mezclar palitos
def mezcla(lista):
    shuffle(lista)
    return lista


# Pedirle intento
def intentalo():
    intento = ''
    while intento not in ['1', '2', '3', '4', '5']:
        intento = input('Introduce un numero entre 1 y 5 .. ')
    return int(intento)


# Comprobar intento
def comprobacion():
    lista = mezcla(palos)
    intento = intentalo()
    if lista[intento - 1] == '-':
        print(f'{lista[intento - 1]} te toca lavar los platos ')
    else:
        print(f'{lista[intento - 1]} te has salvado perro')


comprobacion()
