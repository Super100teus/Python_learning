"""
Aqui es donde le doy estructura a los metodos hechos en el modulo y clase que a continuacion
voy a importar, para que el resultado sea el esperado que es una maquina turnera que acumule
los turnos de los clientes segun vallan llegando acorde a una de las 3 areas
"""
from numeros_proyectodia8 import MaquinaTurnos

def inicio():
    op = 0
    x, y, z = 0, 0, 0
    a = MaquinaTurnos(x, y, z)
    farmacia_com = a.comentarios(a.farmacia)
    cosmetico_com = a.comentarios(a.cosmeticos)
    perfume_com = a.comentarios(a.perfumeria)
    '''verificar_f = a.verificacion(a.farmacia)
    verificar_c = a.verificacion(a.cosmeticos)
    verificar_p = a.verificacion(a.perfumeria)'''
    op_sec = 1
    menu = """________________M  E  N  U________________
    1 . - Turno a farmacia 
    2 . - Turno a cosmetica
    3 . - Turno a perfumeria
    4 . - Verificar turno actual
    5 . - Finalizar"""
    while op != 5:
        try:
            print(menu)
            op = int(input('Ingresa que servicio deseas .. '))

            match op:
                case 1:
                    farmacia_com()

                case 2:
                    cosmetico_com()

                case 3:
                    perfume_com()

                case 4:
                    op_sec = 1
                    sub_menu = '''menu_verificacion
                    1 . - Farmacia 
                    2 . - Cosmeticos 
                    3 . - Perfumeria 
                    Cualquier otro numero para salir'''
                    while op_sec in range(1, 4):
                        print(sub_menu)
                        try:
                            op_sec = int(input('Selecciona la seccion que quieres verificar .. '))
                            if op_sec == 1:
                                verificar_f = a.verificacion(op_sec)
                                verificar_f()
                            elif op_sec == 2:
                                verificar_c = a.verificacion(op_sec)
                                verificar_c()
                            elif op_sec == 3:
                                verificar_p = a.verificacion(op_sec)
                                verificar_p()
                            else:
                                op_sec = 0
                        except ValueError:
                            print('Ingresa un valor si quieres verificar los turnos actuales en el rango de 1-3 o '
                                  'cualquier otro numero para salir')
                            op_sec = 1

                case 5:
                    print('Ejecucion finalizada')

        except ValueError:
            print('Ingresa un valor numerico en el rango de 1-4')
            op = 0


inicio()
