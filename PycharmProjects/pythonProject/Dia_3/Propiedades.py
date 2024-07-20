# Los strings son inmutables
n1 = "laPaka"
n2 = "lop"
print(n1 * 10)  # Repite la misma cadena 10 veces seguidas
texto = """Reunió ejércitos, creó a los balrog y los dragones, asesinó a varios Valar, robó las joyas de los elfos
conocidas como Silmarils, cambió de nombre a Morgoth y, en definitiva, acabó proclamándose Señor Oscuro llegando
incluso a destruir, como recuerda Galadriel, los dos árboles sagrados de Valinor."""
print(texto)  # Manera mas facil de hacer saltos de linea evitando usar el \n
print("recuerda" in texto)  # Verificamos si se encuentra la subcadena en la variable string retorna True o False
print("recuerda" not in texto)  # Verificamos si no se encuentra la subcadena en la variable string retorna True o False
# (proceso inverso del in)
print(len(texto))  # Retorna el numero de caracteres del string

