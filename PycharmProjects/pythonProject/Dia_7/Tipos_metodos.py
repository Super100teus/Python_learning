class Pajaro:
    alas = True  # atributo de clase igual para todos los objetos

    def __init__(self, color, especie):
        self.color = color  # Los atributos declarados en este metodo constructor pueden ser diferentes para cada objeto
        self.especie = especie

    def piar(self):
        print('pio mi color es {}'.format(self.color))  # Accede a atributo del objeto sin modificarlo

    def volar(self, metros):
        print(f'El pajaro ha volado {metros} metros')
        self.piar()  # Accede a otro metodo

    def pintarnegro(self):  # Metodo de instancia: Puede acceder y modificar atributos del objeto, acceder a otros
        # metodos, modificar el estado de la clase
        self.color = 'negro'
        print(f'Ahora el pajaro es {self.color}')  # Accede y modifica atributo del objeto

    @classmethod
    def poner_huevos(cls, huevos):
        print(f'Puso {huevos} huevos')
        cls.alas = False
        print(f'Mis pajaros tienen alas : {cls.alas}')

    @staticmethod
    def mirar():  # No se puede relacionar de ninguna forma con atributos de clase ni de instancia
        print('Pajaro mira')


piolin = Pajaro('amarillo', 'canario')
piolin.piar()
piolin.volar(34)
cirilo = Pajaro('blanco-anaranjado', 'mascota prisionera de guerra')
piolin.pintarnegro()
piolin.volar(333)
piolin.alas = False  # alas es una propiedad correponde a la clase
print(piolin.alas)
Pajaro.poner_huevos(7)
# Pajaro.piar() Da un error ya que la clase esta llamando un metodo de instancia (debe ser llamado por una instancia)
Pajaro.mirar()
cirilo.mirar()
