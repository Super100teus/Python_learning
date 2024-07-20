class Pajaro:
    alas = True  # atributo de clase igual para todos los objetos

    def __init__(self, color, especie):
        self.color = color  # Los atributos declarados en este metodo constructor pueden ser diferentes para cada objeto
        self.especie = especie

    def piar(self):
        print('pio mi color es {}'.format(self.color))

    def volar(self, metros):
        print(f'El pajaro ha volado {metros} metros')


piolin = Pajaro('amarillo', 'canario')
piolin.piar()
piolin.volar(34)
cirilo = Pajaro('blanco-anaranjado', 'mascota prisionera de guerra')
