"""
En este modulo hare la parte logica de cada seccion de la supuesta farmacia
"""
from os import system


class MaquinaTurnos:
    def __init__(self, t_perfume, t_farmacia, t_cosmetico):
        self.t_cosmetico = t_cosmetico
        self.t_perfume = t_perfume
        self. t_farmacia = t_farmacia

    def perfumeria(self):
        self.t_perfume += 1
        yield f'P - {self.t_perfume}'

    def farmacia(self):
        self.t_farmacia += 1
        yield f'F - {self.t_farmacia}'

    def cosmeticos(self):
        self.t_cosmetico += 1
        yield f'C - {self.t_cosmetico}'


    def comentarios(self, funcion):
        def secundaria():
            system('cls')
            print(' \n\n                 Su turno es : ')
            print(f'\n                    {next(funcion())}\n')
            print('             gracias por la espera\n\n')

        return secundaria

    def verificacion(self, opcion):
        aux = 0
        if opcion == 1:
            aux = f'F - {self.t_farmacia}'
        elif opcion == 2:
            aux = f'C - {self.t_cosmetico}'
        elif opcion == 3:
            aux = f'P - {self.t_perfume}'

        def secundaria():
            system('cls')
            print(' \n\n       El turno actual en esta area es : ')
            print(f'\n                    {aux}\n')
            print('             gracias por la espera\n\n')

        return secundaria
