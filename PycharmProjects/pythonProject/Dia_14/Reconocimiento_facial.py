import cv2
import face_recognition as fr

# cargar imagenes
foto_control = fr.load_image_file('FotoA.jpg')
foto_prueba = fr.load_image_file('FotoC.jpg')

# Pasar imagenes a RGB
foto_control = cv2.cvtColor(foto_control, cv2.COLOR_BGR2RGB)
foto_prueba = cv2.cvtColor(foto_prueba, cv2.COLOR_BGR2RGB)

# Localizar cara control
lugar_cara_A = fr.face_locations(foto_control)[0]  # Con coordenadas ubica la cara dentro de un rectangulo
cara_codificada_A = fr.face_encodings(foto_control)[0]  # Busca los numeros de la foto y encuentra lo necesario

# Localizar cara control
lugar_cara_B = fr.face_locations(foto_prueba)[0]  # Con coordenadas ubica la cara ddentro de un rectangulo
cara_codificada_B = fr.face_encodings(foto_prueba)[0]  # Busca los numeros de la foto y encuentra lo necesario

# Mostrar rectangulo
cv2.rectangle(foto_prueba, (lugar_cara_B[3], lugar_cara_B[0]), (lugar_cara_B[1], lugar_cara_B[2]), (255, 0, 0), 2)
# La primera tupla es la coordenada de el vertice superior izquierdo y la segunda la de el inferior derecho

# Mostrar rectangulo
cv2.rectangle(foto_control, (lugar_cara_A[3], lugar_cara_A[0]), (lugar_cara_A[1], lugar_cara_A[2]), (255, 0, 0), 2)

# Realizar comparacion
# El 3er parametro por defecto es 0.6 a menor sea el valor mas estricta se pone una coincidencia
resultado = fr.compare_faces([cara_codificada_A],  cara_codificada_B)
# Tiene que ser un objeto de tipo lista forzosamente
print(resultado)

print(lugar_cara_A)

# medida de la distancia
distancia = fr.face_distance([cara_codificada_A], cara_codificada_B)
print(distancia)

# mostrar resultado
cv2.putText(foto_prueba, f'{resultado}, {distancia.round(2)}', (50, 50), cv2.FONT_HERSHEY_COMPLEX,
            1, (255, 0, 0), 2)

# Mostrar imagenes
cv2.imshow('foto_control', foto_control)
cv2.imshow('foto_prueba', foto_prueba)

# Matener programa abierto
cv2.waitKey(0)

