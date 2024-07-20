texto = "ABCDEFGHIJKLM"
fragmento = texto[2]  # Es igual a el indice 2
fragmento_1 = texto[2:5]  # Slice desde el indice 2 hasta uno antes del 5 osea 4
fragmento_2 = texto[2:]  # Slice desde el indice 2 hasta el final
fragmento_3 = texto[:7]  # Slice desde el principio hasta un indice antes del 7 osea 6
fragmento_4 = texto[3:11:3]  # Slice desde el indice 3 hasta uno antes del 11, de 3 en 3
fragmento_5 = texto[::3]
fragmento_6 = texto[::-1]
print(fragmento, "\n" + fragmento_1, "\n" + fragmento_2, "\n" + fragmento_3, "\n" + fragmento_4, "\n" + fragmento_5)
print(fragmento_6)
fragmento_7 = texto[-1:]  # Me da el ultimo caracter de la cadena
print(fragmento_7)
