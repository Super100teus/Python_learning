def suma():
    n1 = float(input('Ingresa un numero .. '))
    n2 = float(input('Ingresa otro numero .. '))
    n3 = n1+n2
    print(n3)
    print('La suma fue ' + n3)
    print('Bien (:')



try:  # Codigo a ejecutar
    suma()

except TypeError:  # Codigo a ejecutar si hay un error en el try
    print('Error de tipos')

except ValueError:
    print('Ingresaste una letra')

else:  # Codigo a ejecutar si no hay un error en el try
    print('No hubo errores')

finally:  # Codigo a ejecutar despues del try halla errores o no
    print('Bien (:  2')


