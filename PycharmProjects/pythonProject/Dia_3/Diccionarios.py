diccionario = {'c1': 'valor1', 'c2': 'valor2'}
cliente = {'Nombre': 'Mateus', 'Apellido': 'Guzman', 'Peso': 88, 'Talla': 1.89, 'Nacimiento': '2001-01-28'}
consulta = cliente['Nacimiento']
print(consulta)
print(diccionario)
res = diccionario['c2']
print(res)
dic = {'c1': 45, 'c2': [12, 34, 56], 'c3': {'s1': 100, 's2': 200}}
print(dic['c2'][2])
dic2 = {'c1': ['a', 'b', 'c'], 'c2': ['d', 'e', 'f']}
prueba = (dic2['c2'][1]).upper()
print(prueba)
dic2['c3'] = 'valor nuevo'  # Esta forma se puede usar para crear nuevas claves o valores en un diccionario asi como
# tambien para sobrescribir valores ya existentes
print(dic2)
print(dic2.keys())
print(dic2.values())
print(dic2.items())
