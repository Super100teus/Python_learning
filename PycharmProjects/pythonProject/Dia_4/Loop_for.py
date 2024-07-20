lista = ["amara", "biscocho", "carlo", "dinamarca", "estupido"]

for palabra in lista:
    indice_letra = lista.index(palabra)  # Este metodo me permite saber el indice del valor dentro del arreglo
    print(f"_______________________ La palabra es: {palabra} en la posicion {indice_letra} ___________________________")
    if palabra.startswith('a'):  # Este metodo verifica si el primer caracter sea el especificado, tiene otro metodo que
        # en su lugar verifica el ultimo caracter y se llama endwith
        print(f'La palabra {palabra} empieza con a')
    else:
        print(f'La palabra {palabra} no comienza con a')

pal = 'Sauron'
print('-----')
for p in pal:  # Recuerda que las strings se comportan parecido a las listas y se pueden iterar
    print(p)
print('-----')
for pp in 'Texicano':
    print(pp)
print('-----')
numeros = [[1, 2], [3, 4], [5, 6]]
for num in numeros:  # Aqui tambien se puede poner directo como en la string y funciona
    print(num)
print('-----')
for num, b in numeros:  # Aqui tambien se puede poner directo como en la string y funciona
    print(num)
    print(b)
print('-----')
dic = {'clave1': 'Tulkas', 'clave2': 'Hijo de Zeus', 'clave3': 'Viltrumita hiperdotado'}
for cl in dic:
    print(cl)
print('-----')
for cl in dic.items():  # Añado las claves completas del diccionario, aqui tambien se puede usar como en el for de los
    # numeros doble variable declarada en ciclo la primera imprime la clave y la segunda el valor del diccionario
    print(cl)
print('-----')
for cl in dic.values():  # Añado los puros valores del diccionario
    print(cl)
