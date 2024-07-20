def checar_3_cifras(lis):
    lis2 = []
    for n in lis:
        if n in range(100, 1000):  # Recuerda que el segundo digito del range no es inclusivo
            lis2.append(True)
        else:
            lis2.append(False)
    return lis2


print(checar_3_cifras([100, 2, 3, 456, 322, 1, 7888, 33, 200]))


def todos_positivos(lis):
    for n in lis:
        if n < 0:
            return False
        else:
            pass
    return True




lista_numeros = [1, 1, -1, 1, 2, 8]
t = todos_positivos(lista_numeros)
print(t)
