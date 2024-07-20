def suma(num1, num2, *args, **kwargs):
    print(f'num1: {num1} , num2:{num2}')
    for arg in args:
        print(f'arg: {arg}')
    for kwarg in kwargs:
        print(f'kwarg: {kwarg} ')
    print(type(kwargs))
    total = 0
    for c, v in kwargs.items():
        print(f'{c} = {v}')
        total += v
    return total


args = ['Homelander', 94, 'Setir']
kwargs = {"x" : 2, 'c' : 5, 'p' : 9}
# Puedo pasar los argumentos directamente en el metodo, pero siempre en orden es decir en el orden que los declare en
# este caso (num1,num2.*args,**kwargs) o hacerlo con lista y diccionario respectivamente
print(suma(23, 439, *args, **kwargs))


def describir_persona(nom, **kwargs):
    lis = []
    linea = f'Caracteristicas de {nom}:\n'
    for c, v in kwargs.items():
        linea += f'{c}: {v}\n'
    print(linea)
    return linea


describir_persona('m', cabello='cafe', edad ='22')
