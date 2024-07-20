lis = [None] * 5
for i in range(5):
    lis[i] = input('Escribe tu valor, toma en cuenta que el valor sera una string .. ')

print(f'El recorrido de la lista es {lis}')
elm = int(input('Cual es la posicion que quieres eliminar recuerda los indices en este caso van del 0 al 4 .. '))
del lis[elm:(elm+1)]
print(f'El recorrido con el valor eliminado es {lis}')

