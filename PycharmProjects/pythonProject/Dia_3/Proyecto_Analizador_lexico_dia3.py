# Se ingresa una cadena de texto grande y luego en otra variable (recomendablemente una lista) se ingresaran las letras
# a buscar y se haran las siguientes 5 acciones:
# -Cuantas veces aparecen cada una de las letras elegidas
# -Cuantas palabras hay en todo el texto (podriamos convertir la cadena en una lista)
# -Dira cual es la primera letra del texto y cual es la ultima
# -Mostraremos el texto o la cadena principal al reves, se invertira toda la cadena
# -Averiguar si la palabra 'python' se encuentra enn la cadena
cadena1 = """Tulkas es el Vala más fuerte y hábil en el combate y por ello es llamado Astaldo el Valiente. Fue el último 
de los Valar en llegar a Arda pues hizo su entrada en el año 1500 de las Edades de las Lámparas cuando aún se libraba la 
Primera de las Batallas de los Poderes y dicen los Sabios que su fuerte risa y su profunda cólera atemorizaron a Melkor,
que huyó de Arda, y desde entonces se dice que sintió un gran odio por Tulkas el Fuerte. Y es que Tulkas siempre ríe, 
tanto en el juego como en la guerra, en incluso dicen que se rió en la cara de Melkor durante las guerras de los Valar 
antes del despertar de los Elfos."""
cadena = cadena1.lower()
lis = ['', '', '']
lis[0] = input('Ingrese la primera letra .. ')
lis[1] = input('Ingrese la segunda letra .. ')
lis[2] = input('Ingrese la tercera letra .. ')
lis.append(cadena.count(lis[0]))
lis.append(cadena.count(lis[1]))
lis.append(cadena.count(lis[2]))
print(f'La cadena {lis[0]} aparece {lis[3]} veces, la cadena {lis[1]} aparece {lis[4]} veces y la cadena {lis[2]} aparece {lis[5]} veces')
print(f'Las palabras totales en la cadena son {len(cadena.split())}')
print(f'La primera letra del texto es {cadena[0]} y  la ultima es {cadena[-1]}')
print(f'La cadena invertida es \n {cadena[::-1]}')
py = {True: 'La palabra python se encuentra el la cadena', False: 'La palabra python NO se encuentra en la cadena'}
clave_dic = 'python' in cadena
print(py[clave_dic])
