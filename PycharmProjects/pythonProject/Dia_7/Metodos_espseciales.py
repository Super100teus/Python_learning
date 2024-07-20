mi_lista = [1,1,1,1,1]
print(len(mi_lista))
print(mi_lista)


class Objeto:
    pass


mi_objeto = Objeto()
print(mi_objeto)


class CD:
    def __init__(self, autor, titulo, cancion):
        self.autor = autor
        self.titulo = titulo
        self.cancion = cancion

    def __str__(self):
        return f'Album: {self.titulo}, autor: {self.autor},  no.canciones{self.cancion}'
# Modifique el metodo especial str() para que haga lo que aqui acabo de sobreescribir

    def __len__(self):
        return self.cancion

    def __del__(self):
        print(f'Se ha eliminado el album: {self.titulo}')


mi_disco = CD('Floyd', 'The wall', 34)
print(mi_disco)
print(len(mi_disco))
del mi_disco
