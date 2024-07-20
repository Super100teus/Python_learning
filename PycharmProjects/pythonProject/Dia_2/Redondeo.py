val = 90/7
resultado = round(90/7)
print(round(val), resultado)
valor = 95.6666666666666666666666
print(round(valor, 2), type(valor))  # Aqui el tipo de valor sigue siendo float por que no modificamos la variable
valor = round(valor)
print(valor, type(valor))  # Aqui es un int por que ya se modifico la variable
