balas = 16

while balas > 0:
    print(f"Disparaste una bala te quedan __{balas}__ en el cargador")
    balas -= 1
    # balas += -1 esta linea funciona igual que la anterior
else:
    print("\nTe quedaste sin balas")

respuesta = 'y'
while respuesta == 'y':
    respuesta =input('Introduce y para seguir , cualquier otra cosa para parar .. ')
else:  # Se puede usar un else en el ciclo while
    print('\nHa parado')
nom = input('Escribe tu nombre .. ')
for i in nom:
    if i == 'i':
        break
    print(f"\n__________{i}")

for i in nom:
    if i == 'i':
        continue  # Lo que hace continue es brincarse la iteracion, al contrario de break que la rompe o interrumpe por
        # completo
    print(f'\n----------{i}')
