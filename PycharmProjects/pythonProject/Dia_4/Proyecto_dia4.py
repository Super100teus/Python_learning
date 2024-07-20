from random import *
aleatorio = randint(1, 100)
intento, i = 0, 0
print('Intenta adivinar un numero entre 1 y 100 solo numeros enteros, tienes 8 intentos buena suerte')
while intento != aleatorio and i < 9:
    if i < 8:
        intento = int(input(f' Intento numero {i + 1} introduce tu numero ..  '))
        if intento < 1 or intento > 100:
            print(f'Numero no valido solo numeros entre 1 y 100 intenta otra vez')
        elif intento > aleatorio:
            print(f'El numero ingresado es MAYOR al numero ganador')
        elif intento < aleatorio:
            print(f'El numero ingresado es MENOR al numero ganador')
        else:
            print(f'Felicidades has ganado adivinando el numero ganador te tomo {i + 1} intentos')
    else:
        print('Has excedido la cantidad de intentos perdiste debes morir ahora')
    i += 1
