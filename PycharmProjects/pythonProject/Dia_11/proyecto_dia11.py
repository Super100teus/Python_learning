"""
Haremos paso a paso  la recoleccion de todos los nombres de los libros que tengan
4 estrellas o mas dentro de una lista
"""
import bs4
import requests

# Crear url sin numero de pagina
url_base = 'http://books.toscrape.com/catalogue/page-{}.html'
'''for i in range(1, 11):
    print(url_base.format(i))

resultado = requests.get(url_base.format('1'))
sopa = bs4.BeautifulSoup(resultado.text, 'lxml')
libros = sopa.select('.product_pod')
ejemplo = libros[0].select('a')[1]['title']
print(ejemplo)'''
# Lista de titulos con 4 o 5 estrellas
titulos_rating_alto = []

# Iterar paginas
for n, pagina in enumerate(range(1, 51)):
    # Crear sopa en cada pagina
    url_pagina = url_base.format(pagina)
    resultado = requests.get(url_pagina)
    sopa = bs4.BeautifulSoup(resultado.text, 'lxml')

    # Seleccionar datos de libros
    libros = sopa.select('.product_pod')
    titulos_rating_alto.append(f'\n*********Pagina {n + 1}*********\n')
    # Iterar en los libros
    for libro in libros:
        # Verificar las 4 o 5 estrellas
        if len(libro.select('.star-rating.Four')) != 0 or len(libro.select('.star-rating.Five')) != 0:
            # Guardar titulo en variable
            titulo_libro = libro.select('a')[1]['title']
            titulos_rating_alto.append(titulo_libro)


for i in titulos_rating_alto:
    print(i)

