# Aqui pude haber utilizado las funciones max y min en la lista, puto pendejo se te fue el pedo
def devolver_distintos(num1, num2, num3):
    numeros = [num1, num2, num3]
    suma = 0
    mayor, enmedio, menor = numeros[0], numeros[1], numeros[2]  # 3, 5, 7
    if num1 != num2 and num2 != num3 and num1 != num3:
        for i in numeros:
            if mayor <= i:
                mayor = i
            if menor >= i:
                menor = i
        for i in numeros:
            if mayor > i > menor:
                enmedio = i
    elif num1 == num2:
        if num1 > num3:
            mayor, enmedio, menor = num1, num1, num3
        else:
            mayor, enmedio, menor = num3, num1, num1
    elif num1 == num3:
        if num1 > num2:
            mayor, enmedio, menor = num1, num1, num2
        else:
            mayor, enmedio, menor = num2, num1, num1
    elif num2 == num3:
        if num1 > num2:
            mayor, enmedio, menor = num1, num2, num2
        else:
            mayor, enmedio, menor = num2, num2, num1
    elif num1 == num2 == num3:
        mayor, enmedio, menor = num2, num2, num2

    suma = mayor + enmedio + menor
    if suma > 15:
        return mayor
    elif suma < 10:
        return menor
    else:
        return enmedio


print(devolver_distintos(5, 2, 9))
