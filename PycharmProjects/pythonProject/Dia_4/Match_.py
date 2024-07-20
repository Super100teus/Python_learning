op = 'Homelander'

match op:
    case 'soldier boy':
        print('Ben')
    case 'Homelander':
        print('John')
    case 'a-train':
        print('eres negro')
    case _:
        print('no hay manera')
cliente = {'Nombre': 'Mateus', 'Edad': '22', 'Ocupacion': 'Estudiante'}
pelicula = {'titulo': 'La pasion de cristo', 'ficha tecnica': {'Protagonista': 'Jim Caviezel', 'Director': 'Mel Gibson'}}

elementos = [cliente, pelicula, 'l']
for e in elementos:
    match e:
        case {'Nombre': nombre, 'Edad': edad, 'Ocupacion': ocupacion}:
            print(f'Es un cliente llamado {nombre} de {edad} años y es {ocupacion}')
        case {'titulo': titulo, 'ficha tecnica': {'Protagonista': protagonista, 'Director': director}}:
            print(f'Es {titulo} una pelicula dirigida por {director}, y protagonizada por {protagonista}')
        case _:
            print('no se alv')
