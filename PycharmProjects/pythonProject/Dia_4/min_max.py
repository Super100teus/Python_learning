menor = min(12, 45, 76, 2, 99)
mayor = max(12, 45, 76, 2, 99)  # Saca el menor y mayor de estos numeros
lista = [12, 45, 76, 2, 99]
print(f'{menor} , {mayor}')
print(f'lista menor {min(lista)} , lista mayor {max(lista)}')
nom = ['juan', 'mario', 'julio', 'veronica', 'pablo']
palabra = 'Homelander'
print(f'{min(nom)}  {max(nom)} , {max(palabra.lower())} , {min(palabra.lower())}')  # En strings trabaja por orden alfabetico dando
# prioridad a las mayusculas por lo que usamos el metodo lower
dic = {'C1': 56, 'C2': 11}
print(f'{min(dic)} , {min(dic.values())}')
