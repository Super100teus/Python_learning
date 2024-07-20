# Conversion de tipos de datos implicita (el usuario no debe de hacer nada).
num1 = 20
num2 = 30.2
print(type(num1), type(num2))
num1 = num1+num2
print(type(num1), type(num2))

# Conversion de tipos de datos explicita (el usuario tiene que intervenir)
num3 = 5.9
print(num3, type(num3))
num4 = int(num3)
# La salida en el siguiente print dara un int eliminando los decimales de el valor que anteriormente era float
# (NO REDONDEA quiere decir que 2.9999 se convierte en 2 NO en 3)
print(num4, type(num4))
