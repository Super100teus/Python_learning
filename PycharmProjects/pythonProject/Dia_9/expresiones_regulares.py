"""
Funcionalidades de las expresiones regulares en python
"""
import re
texto = """Son principalmente herbívoros y dedican casi la mitad de su día a alimentarse
de tallos, brotes de bambú y una gran variedad de frutas, dieta que complementan con
invertebrados y cortezas de árboles. Se sabe también que algunas subespecies rompen nidos
de termitas y se alimentan de las larvas."""

regex = 'de'
busqueda = re.search(regex, texto)
print(busqueda)  # Solo me da los indices de la primera coincidencia
print(busqueda.span())  # Solo obtenemos informacion de la palabra encontrada
print(busqueda.start())
print(busqueda.end())
busqueda = re.findall(regex, texto)
print(busqueda)
for i in re.finditer(regex, texto):
    print(i.span())

texto2 = "En caso de emergencia llama al 345-456-9721"
regex2 = r'(\d){3}-(\d){3}-(\d){4}'
res = re.search(regex2, texto2)
print(res)
print(res.group())

