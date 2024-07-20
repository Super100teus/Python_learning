

class Prueba1:

    def inicio1(self):
        import datetime
        a = """****************************************************"""
        mi_hora = datetime.time(20, 51)
        print(mi_hora)
        print(a)
        print(mi_hora.minute)
        print(a)
        print(mi_hora.hour)
        print(a)
        mi_fecha = datetime.date(2024, 1, 15)
        print(mi_fecha)
        print(a)
        print(mi_fecha.year)
        print(a)
        print(mi_fecha.month)
        print(a)
        print(mi_fecha.day)
        print(a)  # Tambien se puede expresar la fecha con otro tipo de formato
        print(mi_fecha.ctime())
        print(a)
        '''Fecha de hoy'''
        print(mi_fecha.today())
        print(a)


class Prueba2:

    def inicio2(self):
        from datetime import datetime
        a = """****************************************************"""
        mi_fecha = datetime(2024, 1, 15, 22, 12, 12, 1114)
        print(mi_fecha)
        print(a)
        mi_fecha = mi_fecha.replace(2024, 3)
        print(mi_fecha)
        print(a)
        mi_fecha = mi_fecha.replace(year=2027)
        print(mi_fecha)
        print(a)
        print(mi_fecha.year)
        print(a)
        print(mi_fecha.month)
        print(a)
        print(mi_fecha.day)
        print(a)  # Tambien se puede expresar la fecha con otro tipo de formato
        print(mi_fecha.ctime())
        print(a)
        '''Fecha de hoy'''
        print(mi_fecha.today())
        print(a)
        despierto = datetime(2024, 7, 11, 8, 34, 18)
        duerme = datetime(2024, 7, 12, 1, 9, 54)
        vigilia = duerme - despierto
        print(vigilia.seconds)
        print(a)



class Prueba3:

    def inicio3(self):
        from datetime import date
        a = """****************************************************"""
        nacimiento = date(2001, 1, 28)
        deceso = date(9990, 1, 22)
        vida = deceso - nacimiento
        print(f'Mateus vivio {vida} ')


i2 = Prueba2()
i2.inicio2()
