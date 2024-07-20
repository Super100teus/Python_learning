class Vaca:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print(self.nombre + ' Dice muuu')


class Oveja:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print(self.nombre + ' Dice beee')


vaca1 = Vaca('otis')
oveja1 = Oveja('bigoton')
print(vaca1.hablar())
print(oveja1.hablar())

animales = [vaca1, oveja1]

for animalito in animales:
    animalito.hablar()


def animal_habla(animal):
    animal.hablar()


animal_habla(vaca1)
animal_habla(oveja1)
