archivo = open('dia6_prueba2.txt', 'w')  # Coneste segundo parametro python entiende que el archivo se abre en modo solo
# lectura, si no se pone el parametro python al haber mas parametros python usa este por defecto
# Asegurate de que este abierto en 'w' o en 'a' , 'w'=escribir;  'a'=escribir desde el
# ultimo punto de este archivo por que si esta en modo de solo lectura 'r' no se podra modificar
archivo.write('Nueva linea\n')  # Este contenido de archivo sera reemplazado por el texto que yo aqui ponga y en caso de
# no existir se creara un nuevo archivo
archivo.write('Nueva linea ')
archivo.writelines(['voy', 'a', 'pasar', 'una', 'lista'])  # Pareceria que escribe diferentes renglones pero NO, lo que
# hace es escribir estos strings sin espacios ni nada de separacion
archivo.close()
archivo = open('dia6_prueba.txt', 'a')  # Ubica el cursor hasta el final de mi archivo NO SOBREESCRIBE
archivo.write('\n concateno nueva linea al archivo existente')


archivo.close()
