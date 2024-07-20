def orden_alfa(palabra):
    palabra = palabra.lower()
    pal_mutable = palabra
    pal_nueva = ''
    pal_unica = ''
    for i in palabra:
        pal_nueva += min(pal_mutable)
        pal_mutable = pal_mutable.replace(min(pal_mutable), '', 1)
    for i in pal_nueva:
        if i not in pal_unica:
            pal_unica += i
    return pal_unica


print(orden_alfa('Homelander'))

