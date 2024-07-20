nombre = ['Ana', 'Hugo', 'Valeria']
edades = [65, 29, 43, 55]
combinados = list(zip(nombre, edades))  # Este metodo convierte en una lista de tuplas de la manera anterior , las
# tuplas llegaran hasta la lista mas corta y lo demas lo ingnora correlo y fijate en el resultado de la linea de abajo
print(combinados)
ciudades = ['Lima', 'Mexico', 'Miami']
combinados = list(zip(nombre, edades, ciudades))  # Simplemente tenemos tuplas mas largos
print(combinados)
for nombre, edad, ciudad in combinados:
    print(f'{nombre} tiene {edad} años y vive en la ciudad de {ciudad}')
