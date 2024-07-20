"""
Tiene que ver con un poco de html y css ya que al extraer datos de la web nuestros
comandos en python tendran que interactuar con comandos en html y css
"""
import bs4
import requests

# *************************************************************************************************************
# ************************ PRACTICA PARA OBTENER COMPONENTES ESPECIALMENTE PARRAFOS ***************************
# *************************************************************************************************************

'''resultado = requests.get('https://escueladirecta-blog.blogspot.com/2023/05/configurando-la-impresion-perfecta-de.html')
# print(resultado.text)
sopa = bs4.BeautifulSoup(resultado.text, 'lxml')
# print(sopa)
separador = '\n\n******************************************************************\n\n\n\n'
# Seleccionamos una etiqueta , solo se necesita saber su nombre
print(f'{separador}{len(sopa.select("p"))}')
# Podemos escoger un indice ya que este metodo devuelve una lista
print(f'{separador}{sopa.select("p")[2]}')
# Para librarse de las etiquetas y obtener solo el texto
print(f'{separador}{sopa.select("p")[2].getText()}')
elemento_especial = sopa.select('#post-body-6767435857594978736 p')
print(f'{separador}{elemento_especial}')
print(f'{separador}{elemento_especial[6]}{separador}')
for p in elemento_especial:
    print(p.getText())'''

# *************************************************************************************************************
# *************************************************************************************************************


# *************************************************************************************************************
# ******************************** PRACTICA PARA OBTENER COMPONENTES DE IMAGEN ********************************
# *************************************************************************************************************

img_practica = requests.get('https://www.esquire.com/es/ciencia/a40555746/tesla-inventor-biografia/')
sopa2 = bs4.BeautifulSoup(img_practica.text, 'lxml')
separador = '\n\n******************************************************************\n\n\n\n'
'''class="css-0 exi4f7p0" esa era la clase que me salia debido a que si el código fuente tiene class="css-0 exi4f7p0",
eso indica que el elemento HTML tiene dos clases asignadas: "css-0" y "exi4f7p0". En HTML y CSS, puedes asignar
múltiples clases a un elemento separándolas por espacios dentro del atributo class. Solo busque en ambas clases
hasta que encontre las imagenes de nicola tesla en este caso'''
imagenes = sopa2.select('.exi4f7p0')
for i, v in enumerate(imagenes):
    print(imagenes[i]['src'])
foto = requests.get(sopa2.select('.exi4f7p0')[3]['src'])
f = open('Tesla.jpg', 'wb')  # Significa write binary ya interpretara una imagen
f.write(foto.content)
f.close()


# *************************************************************************************************************
# *************************************************************************************************************

