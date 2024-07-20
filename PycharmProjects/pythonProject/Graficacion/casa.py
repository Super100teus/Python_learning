import turtle

# Configuración de la pantalla
wn = turtle.Screen()
wn.bgcolor("white")

# Crear un objeto Turtle
house = turtle.Turtle()
house.shape("turtle")
house.speed(1)

# Mover a la posición inicial
house.penup()
house.goto(-50, -100)
house.pendown()

# Dibujar el cuerpo de la casa (cuadrado)
house.fillcolor("yellow")
house.begin_fill()
for _ in range(4):
    house.forward(100)
    house.left(90)
house.end_fill()

# Mover a la posición del techo
house.penup()
house.goto(-60, 0)
house.pendown()

# Dibujar el techo (triángulo)
house.fillcolor("red")
house.begin_fill()
house.goto(0, 50)
house.goto(60, 0)
house.end_fill()

# Mover a la posición de la puerta
house.penup()
house.goto(-15, -100)
house.pendown()

# Dibujar la puerta (rectángulo)
house.fillcolor("brown")
house.begin_fill()
house.goto(-15, -40)
house.goto(15, -40)
house.goto(15, -100)
house.goto(-15, -100)
house.end_fill()

# Dibujar la ventana derecha (rectángulo)
house.penup()
house.goto(25, -30)
house.pendown()
house.fillcolor("blue")
house.begin_fill()
house.goto(25, -10)
house.goto(45, -10)
house.goto(45, -30)
house.goto(25, -30)
house.end_fill()

# Dibujar la ventana izquierda (rectángulo)
house.penup()
house.goto(-45, -30)
house.pendown()
house.fillcolor("blue")
house.begin_fill()
house.goto(-45, -10)
house.goto(-25, -10)
house.goto(-25, -30)
house.goto(-45, -30)
house.end_fill()

# Cerrar la ventana al hacer clic en ella
wn.exitonclick()

# Opción 2: Traslación
house.penup()
house.goto(50, -100)  # Nueva posición
house.pendown()

# Opción 3: Escalamiento
scale_factor = 1.5  # Factor de escala
for i in range(4):
    house.setx(house.xcor() * scale_factor)
    house.sety(house.ycor() * scale_factor)

# Opción 4: Rotación
def rotate_house(angle):
    house.seth(angle)
    turtle.done()  # Cierra la ventana al finalizar

# Solicitar al usuario el ángulo de rotación
angle = int(input("Ingrese el ángulo de rotación: "))
rotate_house(angle)

# Opción 5: Sesgado
house.penup()
house.goto(-50, -100)
house.pendown()
for i in range(4):
    if i % 2 == 0:  # Sesgo en las coordenadas X
        house.setx(house.xcor() + 20)
    else:  # Sesgo en las coordenadas Y
        house.sety(house.ycor() + 20)

# Mantener la ventana abierta
turtle.done()