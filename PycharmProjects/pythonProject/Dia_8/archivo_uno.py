"""
Este es un modulo que imprime  algo para ser calificado por pylint
basado en las reglas de PEP 8 este archivo se llamabaArchivo1.py
pero por la convencion snake_case debere llamarlo archivo_uno,
snake_case: En Python, es una práctica comúnnombrar los módulos,
variables y funciones utilizando la convención snake_case, que consiste
en palabras en minúsculas separadas por guiones bajos. Los nombres
de los módulos deben seguir esta convención. Puntaje de Pylint: 10/10
"""


def imprime_algo():
    """
    Crea una variable y la imprime
    :return: num
    """
    num = 22
    print(num)
    return num


imprime_algo()
