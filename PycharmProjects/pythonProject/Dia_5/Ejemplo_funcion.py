precios_cafe = [('Capuccino', 45), ('Expresso', 30), ('Chocolate', 60)]
for c, p in precios_cafe:
    print(c)
# Quiero saber cual es tipo de cafe mas caro con una funcion


def cafe_caro(lis):
    cafe_mas_caro = ''
    precio_mayor = 0
    for cafe, precio in lis:
        if precio > precio_mayor:
            precio_mayor = precio
            cafe_mas_caro = cafe
        else:
            pass

    return (cafe_mas_caro, precio_mayor)


cafe, precio = cafe_caro(precios_cafe)
print(f' el cafe es {cafe} y  el precio es {precio}')


