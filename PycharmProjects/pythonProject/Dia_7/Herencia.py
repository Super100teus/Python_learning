class Animal:
    def __init__(self, edad, color):
        self.edad = edad
        self.color = color

    def nacer(self):
        print('Este animal nacio')

    def hablar(self):
        print('Hace ruido')


class Pajaro(Animal):

    def __init__(self, altitud, edad, color):
        super().__init__(edad, color)
# Puedo hacerlo con el comando super() o quitando ese comando y poniendo las dos lineas de abajo
        #self.edad = edad
        #self.color = color
        self.altitud = altitud

    def hablar(self):
        print('Hace pio')

    def volar(self, metros):
        print(f'El pajaro vuela {metros} metros')


print(Pajaro.__bases__)
print(Animal.__bases__)
print(Pajaro.__subclasses__())
print(Animal.__subclasses__())
piolin = Pajaro(3, 'azul', 40)
piolin.nacer()
print(f'Piolin tiene {piolin.edad} años y es de color {piolin.color}')
piolin.hablar()
piolin.volar(2222)
elefante = Animal(31, 'gris')

# ********************************************************************************************************************************************************************************************************************
# ********************************************************************************************************************************************************************************************************************
# *********************************                                                    *********************************
# ********************************* H  E  R  E  N  C  I  A      M  U  L  T  I  P  L  E *********************************
# *********************************                                                    *********************************
# ********************************************************************************************************************************************************************************************************************
# ********************************************************************************************************************************************************************************************************************


class Padre:
    def hablar(self):
        print('Hola')


class Madre:
    def reir(self):
        print('jajajja')

    def hablar(self):
        print('Que tal')


class Hijo(Madre, Padre):  # En caso de heredar 2 metodos iguales de 2 clases diferentes hay un orden de herencia ,
    # heredando el metodo de la primera clase de la que se heredo
    pass


class Nieto(Hijo):
    pass


mi_nieto = Nieto()
mi_nieto.hablar()
mi_nieto.reir()
print(Nieto.__mro__)







