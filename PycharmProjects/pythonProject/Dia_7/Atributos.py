class Pajaro:
    alas = True  # atributo de clase igual para todos los objetos

    def __init__(self, color, especie):
        self.color = color  # Los atributos declarados en este metodo constructor pueden ser diferentes para cada objeto
        self.especie = especie


piolin = Pajaro('amarillo', 'canario')
cirilo = Pajaro('blanco-anaranjado', 'mascota prisionera de guerra')

print(f'Mi pajaro es un {piolin.especie} de color {piolin.color}  {piolin.alas}')
print(f'Mi pajaro es un {cirilo.especie} de color {cirilo.color}  {cirilo.alas}')
