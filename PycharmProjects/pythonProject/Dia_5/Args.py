# Acepta los argumentos que sea siempre y cuando haya un * antes del argumento , la paabra no
# necesariamente debe de ser args puede ser cualquier cosa que este precedida por el * aunque se recomienda args por
# legibilidad y buena costumbre de programacion
def suma(*args):
    total = 0
    for arg in args:
        total += arg
    return total


print(suma(1, 2, 3, 4, 5, 6, 7, 8, 8, 878, 8))
