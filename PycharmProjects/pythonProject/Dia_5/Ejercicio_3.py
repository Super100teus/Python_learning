def numero_cero(*args):
    numero_actual = 0
    numero_anterior = 0
    aux = 0
    for i in args:
        if aux == 0:
            numero_anterior = i
            aux = 1
        elif numero_anterior % 10 == 0 or numero_anterior == 0:
            if i == 0:
                return True
            else:
                numero_anterior = i
        else:
            numero_anterior = i
    return False


print(numero_cero(1, 11, 0, 10, 0, 90))
