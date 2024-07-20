import re

rgex = r'^(https?://(www\.)?|www\.)([a-zA-Z])+\.([a-zA-Z]){2,90}$'
findall = re.findall(rgex, 'http://moure.dev')  # El findall busca una concordancia en alguna parte de la cadena y
# devuelve todas las concordancias encontradas
mch = re.match(rgex, 'www.moure.dev')  # El match busca una concordancia que aplique a la cadena entera desde el
# principio
srch = re.search(rgex, 'http://www.moure.dev')  # El search busca la primera coincidencia dentro de toda la cadena
print(f'match: {mch}, findall: {findall}, search: {srch} ')
