import cv2
import face_recognition as fr
import os
import numpy
from datetime import datetime
from sklearn.metrics import accuracy_score, confusion_matrix, ConfusionMatrixDisplay

# crear base de datos
ruta = 'Empleados'
mis_imagenes = []
nombres_empleados = []
lista_empleados = os.listdir(ruta)
print(lista_empleados)

for nombre in lista_empleados:
    nombre_actual = cv2.imread(f'{ruta}/{nombre}')
    mis_imagenes.append(nombre_actual)
    nombres_empleados.append(os.path.splitext(nombre)[0])


# codificar imagenes
def codificar(imagenes):
    # crear lista nueva
    lista_codificada = []
    # Pasar todas las imagenes a RGB
    for imagen in imagenes:
        imagen = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)
        # codificar
        codificado = fr.face_encodings(imagen)[0]
        # agregar a la lista
        lista_codificada.append(codificado)

    # Devolver lista codificada
    return lista_codificada


# Registrar ingresos
def registrar_ingresos(persona):
    f = open('registro.csv', 'r+')
    lista_datos = f.readlines()
    nombres_registro = []
    for linea in lista_datos:
        ingreso = linea.split(',')
        nombres_registro.append(ingreso[0])

    if persona not in nombres_registro:
        ahora = datetime.now()
        string_ahora = ahora.strftime('%H:%M:%S')
        f.writelines(f'\n{persona}, {string_ahora}')


lista_empleados_codificada = codificar(mis_imagenes)
print(len(lista_empleados_codificada))

# Tomar imagen de camara web
captura = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# leer la imagen de la camara
exito, imagen = captura.read()

if not exito:
    print('No se tomo la captura')
else:
    # reconocer cara en captura
    cara_captura = fr.face_locations(imagen)
    # codificar cara capturada
    cara_captura_codificada = fr.face_encodings(imagen, cara_captura)

    # buscar coinciencias
    for caracodif, caraubi in zip(cara_captura_codificada, cara_captura):
        coincidencias = fr.compare_faces(lista_empleados_codificada, caracodif)
        distancias = fr.face_distance(lista_empleados_codificada, caracodif)
        print(distancias)
        indice_coincidencia = numpy.argmin(distancias)

        # mostrar coincidencia
        if distancias[indice_coincidencia] > 0.7:
            print('No coincides con nadie')
        else:
            print('Bienvenido')
            # Buscar el nombre del empleado encontrado
            nombre = nombres_empleados[indice_coincidencia]
            y1, x2, y2, x1 = caraubi
            cv2.rectangle(imagen, (x1, y1), (x2, y2), (255, 0, 0), 2)
            cv2.rectangle(imagen, (x1, y2 - 35), (x2, y2), (255, 0, 0), 2)
            cv2.putText(imagen, nombre, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
            registrar_ingresos(nombre)

            # mostrar imagen obtenida
            cv2.imshow('Imagen web', imagen)
            # matener ventana abierta
            cv2.waitKey(0)



