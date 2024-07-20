"""
Vere las herramientas de el modulo collections
"""
from collections import Counter
from collections import defaultdict
from collections import namedtuple

mensaje = """***************** ***************** ***************** ***************** *****************
***************** *****************       Counter     ***************** *****************
***************** ***************** ***************** ***************** *****************\n"""
print(mensaje)

num = [2, 4, 8, 5, 2, 7, 7, 4, 9, 56, 32, 56]
print(Counter(num))  # Lo que Counter hace es basicamente contyar cuantas veces se repite cada valor dentro de la lista
frase = 'tres tristes tigres tragaban trigo en un trigal'
print(Counter(frase.split()))
print(Counter('Homelander'))
serie = Counter([1, 1, 1, 1, 1, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5])
print(serie.most_common())  # Verifica el valor mas comun, llena una lista con tuplas que contienen los datos
# Si pasas un numero como parametro muestra cuales son los x valores mas comunes
print(serie.most_common(2))
print(list(serie))  # Me da una lista con los valores unicos


mensaje = """\n***************** ***************** ***************** ***************** *****************
***************** *****************    defaultdict    ***************** *****************
***************** ***************** ***************** ***************** *****************\n"""
print(mensaje)

mi_dic = {'uno': 'verde', 'dos': 'azul', 'tres': 'estrella', 'cuatro': 'carmesi'}
print(mi_dic['tres'])
print(mi_dic)
mi_dic = defaultdict(lambda: 'nada')
print(mi_dic['c'])  # Al imprimir una clave que no existe en mi diccionario deberia dar error de no ser
# por defaultdict, ahora existe la clave c y se le asigno el valor de nada
print(mi_dic)

mensaje = """\n***************** ***************** ***************** ***************** *****************
***************** *****************     namedtuple    ***************** *****************
***************** ***************** ***************** ***************** *****************\n"""
print(mensaje)

mi_tupla = (1, 2, 45, 12, 18)
print(mi_tupla[2])
persona = namedtuple('Persona', ['nombre', 'altura', 'peso'])
atreus = persona('heim', '1.9', '80')
print(atreus.altura)  # Puedes nombrar cada posicion de la tupla

