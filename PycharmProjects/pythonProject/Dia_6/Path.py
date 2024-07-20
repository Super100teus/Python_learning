from pathlib import Path

base = Path.home()  # Instacia Path devuelve una ruta absoluta del usuario principal
guia = Path(base, 'Barcelona', 'Moises.jpng')  # El constructor Path admite cadenas y objetos Path
print(base)
print(guia)
guia0 = Path(base, 'desk', Path('Barcelona', 'Moises.jpng'))
print(guia0)
guia2 = guia0.with_name('Elias.txt')
print(guia2)  # Tiene la misma estructura que guia0 pero cambia el nombre del supuesto archivo
print(guia2.parent)  # Es una instancia de Path que recorre a el antecesor mas imediato de una ruta de archivos indicada
print(guia2.parent.parent)
archivos = Path(Path.home(), 'OneDrive', 'Escritorio', 'Trabajos', 'Curso_python')  # En el bucle for me devuelve
# todos los archivos con la terminacion especificada
aux = Path('C:', 'Users', 'BatMa', 'OneDrive', 'Escritorio', 'Trabajos', 'Curso_python', 'carpeta_prueba', 'Nuevo2.txt')
carpeta_prueba = aux.relative_to(Path('C:', 'Users', 'BatMa', 'OneDrive', 'Escritorio', 'Trabajos', 'Curso_python',
                                      'carpeta_prueba'))
# Aqui me devuelve el archivo que especificado a el final del Path, lasveces que se encuentre en
# carpeta_prueba o Curso_python
Curso_python = aux.relative_to(Path('C:', 'Users', 'BatMa', 'OneDrive', 'Escritorio', 'Trabajos', 'Curso_python'))
print(carpeta_prueba)
print(Curso_python)
for txt in Path(archivos).glob('*.txt'):
    print(txt.stem)

# Agregara a todos los archivos txt que se encuentren dentro de Curso_python incluyendo otras carpetas
print('\n-----------------------------------------------------------------------------------------------------\n')
for txt in Path(archivos).glob('**/*.txt'):
    print(txt)

