from Paquete_Mateus import suma_resta
from Paquete_Mateus.Subpaquete import Saludo
# De esta manera puedo mandar a traer todos los modulos dentro del Paquete_Mateus , aunque tengo que importarlos primero
# claro, en este caso a dia del comentario de hoy solo importe el modulo suma_resta

suma_resta.resta(23, 78)  # Puedo llamar los metodos de los modulos de la manera anterior

# Ahora hare lo mismo pero con un subpaquete
Saludo.saludar()
