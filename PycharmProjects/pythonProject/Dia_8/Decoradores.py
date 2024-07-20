"""
Lo que hace este modulo es ver la funcion de los decoradores de funciones que basicamente
lo que hacen es activar o desactivar acciones adicionales dentro de una funcion
"""


def cambiar_letras(tipo):

    def mayusculas(tex):
        print(tex.upper())

    def minusculas(tex):
        print(tex.lower())

    if tipo == 'may':
        return mayusculas
    elif tipo == 'min':
        return minusculas


# Todo en python es un objeto, por lo que hasta las funciones pueden ser asignadas a variables
mi_funcion = cambiar_letras('may')
mi_funcion('HomeLaNder')  # Le paso el parametro que la funcion necesita


def decora_saludo(funcion):
    def otra_fun(palabra, pl):
        print('hola')
        funcion(palabra, pl)
        print('adios')
    return otra_fun


@decora_saludo
def suma(num1, num2):
    num3 = num1 + num2
    print(f'La suma es {num3}')


def resta(num1, num2):
    num3 = num1 - num2
    print(f'La resta es {num3}')


operaciones = suma
operaciones(45, 98)  # Esta es una manera de aplicar la decoracion a la funcion aunque a mi parecer no la mejor
resta_decorada = decora_saludo(resta)  # Esta manera me parece mejor, misma funcion pero con acciones adicionales
resta_decorada(34, 881)
resta(665, 6756)

