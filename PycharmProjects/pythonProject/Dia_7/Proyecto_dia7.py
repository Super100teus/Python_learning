from os import system


class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido


class Cliente(Persona):
    def __init__(self, no_cuenta, balance, nombre, apellido):
        super().__init__(nombre, apellido)
        self.no_cuenta = no_cuenta
        self.balance = balance

    def print(self):
        print(f'{self.nombre} {self.apellido} tu numero de cuenta es, {self.no_cuenta} y tu balance actual es de '
              f'${self.balance}')

    def depositar(self):
        deposito = float(input('Ingrese la cantidad que desea depositar .. '))
        self.balance = self.balance + deposito
        print(f'Tu saldo es de {self.balance}')

    def retiro(self):
        retiro = float(input('Ingresa el monto a retirar .. '))
        if retiro > self.balance:
            print(f'No puedes retirar ese monto tu saldo es de {self.balance}')
        else:
            self.balance = self.balance - retiro
            print(f'Tu saldo restante es de {self.balance}')


def usuario_nuevo():
    nom, n_cuenta, apell = '', '', ''
    saldo = 0
    aux = False
    nom = input('Ingresa tu nombre .. ')
    apell = input('Ingresa tus apellidos .. ')
    n_cuenta = input('Ingresa tu numero de cuenta .. ')
    while not aux:
        try:
            saldo = float(input('Define tu saldo total .. '))
            aux = True

        except ValueError:
            print('Debes ingresar un valor numerico en el saldo')
    usuario = Cliente(n_cuenta, saldo, nom, apell)
    return usuario


def inicio():
    cliente = usuario_nuevo()
    op = 0
    while op != 4:
        menu = '''__________MENU DE OPCIONES__________
        1 . - Retirar
        2 . - Depositar
        3 . - Verificar datos
        4 . - Salir de transaccion'''
        print(menu)
        op = int(input('Escoge la opcion deseada .. '))
        match op:
            case 1:
                system('cls')
                cliente.retiro()
            case 2:
                system('cls')
                cliente.depositar()
            case 3:
                system('cls')
                cliente.print()
            case 4:
                system('cls')
                print('Fin de la transaccion')


inicio()
