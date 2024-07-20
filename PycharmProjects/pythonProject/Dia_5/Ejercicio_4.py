def contar_primos(num):
    primos = 0
    lis = []
    cont = 0
    for i in range(num+1):
        cont = 0
        if i != 0 and i != 1:
            for u in range(i + 1):
                if u != 0 and u != 1:
                    if i % u == 0:
                        cont += 1
        if cont == 1:
            primos += 1
            lis.append(i)
    return f' Hay {primos} en el rango de {num}, y son los siguientes:\n {lis}'


print(contar_primos(300))



