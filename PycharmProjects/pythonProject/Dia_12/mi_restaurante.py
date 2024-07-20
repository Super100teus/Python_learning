"""
Utilizando la libreria grafica de tkinter hare un gestor de restaurantes en
donde ingresare todos los consumos de una mesa, cantidades y precios, tendra incorporado
una calculadora, te podra decir cuanto dinero le corresponde pagar al cliente,
al final dara un recibo con numero de ticket, fecha, costos y en si lo necesario,
el ticket se podra guardar en una archivo txt
"""
from tkinter import *
import random
import datetime
from tkinter import filedialog, messagebox


operador = ''
precios_comida = [1.32, 1.65, 2.31, 3.22, 1.22, 1.99, 2.05, 2.65]
precios_bebida = [0.25, 0.99, 1.21, 1.54, 1.08, 1.10, 2.00, 1.58]
precios_postres = [1.54, 1.68, 1.32, 1.97, 2.55, 2.14, 1.94, 1.74]


def click_boton(numero):
    global operador
    operador = operador + numero
    # eliminara lo que haya en el widget de texto desde el indice 0 hasta el final
    visor_caluladora.delete(0, END)
    # END inserta la variable operador al final de el widget de texto
    visor_caluladora.insert(END, operador)


def borrar():
    visor_caluladora.delete(0, END)
    global operador
    operador = ''


def ce():
    global operador
    resultado = str(eval(operador))
    visor_caluladora.delete(0, END)
    visor_caluladora.insert(END, resultado)
    operador = resultado


def revisar_check():
    x = 0
    for i in cuadros_comida:
        if variables_comida[x].get() == 1:
            cuadros_comida[x].config(state=NORMAL)
            if cuadros_comida[x].get() == '0':
                # El metodo delete es para widgets de entrada de texto
                cuadros_comida[x].delete(0, END)
            cuadros_comida[x].focus()
        else:
            cuadros_comida[x].config(state=DISABLED)
            texto_comida[x].set('0')
        x += 1


def revisar_check2():
    x = 0
    for i in cuadros_bebida:
        if variables_bebida[x].get() == 1:
            cuadros_bebida[x].config(state=NORMAL)
            if cuadros_bebida[x].get() == '0':
                # El metodo delete es para widgets de entrada de texto
                cuadros_bebida[x].delete(0, END)
            cuadros_bebida[x].focus()
        else:
            cuadros_bebida[x].config(state=DISABLED)
            texto_bebida[x].set('0')
        x += 1


def revisar_check3():
    x = 0
    for i in cuadros_postre:
        if variables_postre[x].get() == 1:
            cuadros_postre[x].config(state=NORMAL)
            if cuadros_postre[x].get() == '0':
                # El metodo delete es para widgets de entrada de texto
                cuadros_postre[x].delete(0, END)
            cuadros_postre[x].focus()
        else:
            cuadros_postre[x].config(state=DISABLED)
            texto_postre[x].set('0')
        x += 1


def total():
    subtotal_comida = 0
    p = 0
    for cantidad in texto_comida:
        subtotal_comida = subtotal_comida + (float(cantidad.get())) * precios_comida[p]
        p += 1
    print(subtotal_comida)
    # Bebidas ************************
    subtotal_bebida = 0
    p = 0
    for cantidad in texto_bebida:
        subtotal_bebida = subtotal_bebida + (float(cantidad.get())) * precios_bebida[p]
        p += 1
    print(subtotal_bebida)
    # postres ************************
    subtotal_postre = 0
    p = 0
    for cantidad in texto_postre:
        subtotal_postre = subtotal_postre + (float(cantidad.get())) * precios_postres[p]
        p += 1
    print(subtotal_postre)
    sub_total = subtotal_postre + subtotal_bebida + subtotal_comida
    impuestos = sub_total * 0.16
    total = sub_total + impuestos
    var_costo_comida.set(f'$ {round(subtotal_comida, 2)}')
    var_costo_bebida.set(f'$ {round(subtotal_bebida, 2)}')
    var_costo_postre.set(f'$ {round(subtotal_postre, 2)}')
    var_subtotal.set(f'$ {round(sub_total, 2)}')
    var_impuestos.set(f'$ {round(impuestos, 2)}')
    var_total.set(f'$ {round(total, 2)}')


def recibo():
    texto_recibo.delete(1.0, END)
    num_recibo = f'# {random.randint(1000, 9999)}'
    fecha = datetime.datetime.now()
    fecha_recibo = f'{fecha.day} / {fecha.month} / {fecha.year} - {fecha.hour} : {fecha.minute}'
    texto_recibo.insert(END, f'Datos\t{num_recibo}\t\t{fecha_recibo}\n')
    texto_recibo.insert(END, f'*' * 57 + '\n')
    texto_recibo.insert(END, 'Items\t\tCantidad\t\tCosto items\n')
    texto_recibo.insert(END, f'-' * 68 + '\n')
    x = 0
    for comida in texto_comida:
        if comida.get() != '0':
            texto_recibo.insert(END, f'{lista_comidas[x]}\t\t{comida.get()}\t\t'
                                     f'$ {round(int(comida.get()) * precios_comida[x], 2)}\n')
        x += 1

    x = 0
    for bebida in texto_bebida:
        if bebida.get() != '0':
            texto_recibo.insert(END, f'{lista_bebidas[x]}\t\t{bebida.get()}\t\t'
                                     f'$ {round(int(bebida.get()) * precios_bebida[x], 2)}\n')
        x += 1

    x = 0
    for postres in texto_postre:
        if postres.get() != '0':
            texto_recibo.insert(END, f'{lista_postres[x]}\t\t{postres.get()}\t\t'
                                     f'$ {round(int(postres.get()) * precios_postres[x], 2)}\n')
        x += 1
    texto_recibo.insert(END, f'*' * 57 + '\n')
    texto_recibo.insert(END, f'Costo comida: {var_costo_comida.get()}\n')
    texto_recibo.insert(END, f'Costo bebida: {var_costo_bebida.get()}\n')
    texto_recibo.insert(END, f'Costo postre: {var_costo_postre.get()}\n')
    texto_recibo.insert(END, f'*' * 57 + '\n')
    texto_recibo.insert(END, f'Subtotal: {var_subtotal.get()}\n')
    texto_recibo.insert(END, f'Impuestos: {var_impuestos.get()}\n')
    texto_recibo.insert(END, f'Total: {var_total.get()}\n')


def guardar():
    info_recibo = texto_recibo.get(1.0, END)
    archivo = filedialog.asksaveasfile(mode='w', defaultextension='.txt')
    archivo.write(info_recibo)
    archivo.close()
    messagebox.showinfo('Informacion', 'Su recibo ha sido guardado')


def resetear():
    texto_recibo.delete(1.0, END)
    for texto in texto_comida:
        texto.set('0')
    for texto in texto_bebida:
        texto.set('0')
    for texto in texto_postre:
        texto.set('0')
    for cuadro in cuadros_comida:
        cuadro.config(state=DISABLED)
    for cuadro in cuadros_bebida:
        cuadro.config(state=DISABLED)
    for cuadro in cuadros_postre:
        cuadro.config(state=DISABLED)
    for v in variables_comida:
        v.set(0)
    for v in variables_bebida:
        v.set(0)
    for v in variables_postre:
        v.set(0)
    var_costo_comida.set('')
    var_costo_bebida.set('')
    var_costo_postre.set('')
    var_subtotal.set('')
    var_impuestos.set('')
    var_total.set('')
    visor_caluladora.delete(0, END)



# Iniciar tkinter
aplicacion = Tk()

# Tamño de la ventana
'''anchoxaltura y los otros dos numeros concatenados con el simbolo + son las coordenadas en
donde la esquina superior izquierda de mi ventana emergente aparecera en MI VENTANA
todo debe de ir junto o da error'''
aplicacion.geometry('1020x630+280+100')

# Evitar maximizar
aplicacion.resizable(False, False)

# Establecer titulo de ventana
aplicacion.title('Restaurant - sistema de facturacion')

# Color de fondo
# Podemos utilizar el sistema RGB con el sistemanumerico hexadecimal (#RRGGBB)o una lista de nombres de
# colores predeterminados lista:
# https://es.wikibooks.org/wiki/Python/Interfaz_gr%C3%A1fica_con_Tkinter/Los_nombres_de_los_colores
aplicacion.config(bg='#AAA67F')
# Panel superior
panel_superior = Frame(aplicacion, bd=1, relief=FLAT)
panel_superior.pack(side=TOP)
# Etiqueta titulo
etiqueta_titulo = Label(panel_superior, text='sistema de facturacion', fg='azure4', font=('Dosis', 58, 'bold'),
                        bg='burlywood', width=20)
etiqueta_titulo.grid(row=0, column=0)


# Panel izquierdo
panel_izquierdo = Frame(aplicacion, bd=1, relief=FLAT)
panel_izquierdo.pack(side=LEFT)

# Panel costos
panel_costos = Frame(panel_izquierdo, bd=1, relief=FLAT, bg='azure4', padx=50)
panel_costos.pack(side=BOTTOM)

# Panel de comidas
panel_comidas = LabelFrame(panel_izquierdo, text='Comida', font=('Dosis', 14, 'bold'), bd=1, relief=FLAT,
                           fg='aquamarine3')
panel_comidas.pack(side=LEFT)

# Panel de bebidas
panel_bebidas = LabelFrame(panel_izquierdo, text='Bebidas', font=('Dosis', 14, 'bold'), bd=1, relief=FLAT,
                           fg='aquamarine3')
panel_bebidas.pack(side=LEFT)

# Panel de Postres
panel_postres = LabelFrame(panel_izquierdo, text='Postres', font=('Dosis', 14, 'bold'), bd=1, relief=FLAT,
                           fg='aquamarine3')
panel_postres.pack(side=LEFT)

# Panel derecha
panel_derecho = Frame(aplicacion, bd=1, relief=FLAT)
panel_derecho.pack(side=RIGHT)

# Panel calculadora
panel_calculadora = Frame(panel_derecho, bd=1, relief=FLAT, bg='burlywood')
panel_calculadora.pack(side=TOP)  # Esto no es necesario, si se deja vacia a pack por defecto se utiliza TOP

# Panel recibo
panel_recibo = Frame(panel_derecho, bd=1, relief=FLAT, bg='burlywood')
panel_recibo.pack(side=TOP)

# Panel botones
panel_botones = Frame(panel_derecho, bd=1, relief=FLAT, bg='burlywood')
panel_botones.pack(side=TOP)

# Lista de productos
lista_comidas = ['pollo', 'mole', 'pizza', 'sushi', 'pulpo', 'atun', 'tacos', 'bagre']
lista_bebidas = ['agua', 'J. naranja', 'cerveza', 'tequila', 'soda', 'cafe', 'capuccino', 'michelada']
lista_postres = ['pastel', 'pie', 'flan', 'nieve', 'tejuino', 'caramelo', 'chocolate', 'cacahuates']

# Items para generar comida
variables_comida = []
cuadros_comida = []
texto_comida = []
contador = 0
for alimento in lista_comidas:

    # Checkbutton
    variables_comida.append('')
    variables_comida[contador] = IntVar()
    alimento = Checkbutton(panel_comidas, text=alimento.title(), font=('Dosis', 14, 'bold'), onvalue=1, offvalue=0,
                           variable=variables_comida[contador], command=revisar_check)
    '''Aqui se utiliza contador para tratar de ubicar cada objeto de la lista uno encima de otro
    todos en la columna 0, por ahora supongo que el cuadro de seleccion en la columna 0
    debio de haaber sido añadido por defecto gracias a la funcion Checkbutton'''
    alimento.grid(row=contador, column=0, sticky=W)
    # Crear los cuadros de entrada
    cuadros_comida.append('')
    texto_comida.append('')
    texto_comida[contador] = StringVar()  # Tipo de varible exclusivo de tkinter
    texto_comida[contador].set('0')
    cuadros_comida[contador] = Entry(panel_comidas, font=('Dosis', 13, 'bold'), bd=1, width=6, state=DISABLED,
                                     textvariable=texto_comida[contador])
    cuadros_comida[contador].grid(row=contador, column=1, sticky=W)
    contador += 1

# Items para generar bebida
variables_bebida = []
cuadros_bebida = []
texto_bebida = []
contador = 0
for bebida in lista_bebidas:
    variables_bebida.append('')
    variables_bebida[contador] = IntVar()
    bebida = Checkbutton(panel_bebidas, text=bebida.title(), font=('Dosis', 14, 'bold'), onvalue=1, offvalue=0,
                         variable=variables_bebida[contador], command=revisar_check2)
    bebida.grid(row=contador, column=0, sticky=W)
    # Crear los cuadros de entrada
    cuadros_bebida.append('')
    texto_bebida.append('')
    texto_bebida[contador] = StringVar()  # Tipo de varible exclusivo de tkinter
    texto_bebida[contador].set('0')
    cuadros_bebida[contador] = Entry(panel_bebidas, font=('Dosis', 13, 'bold'), bd=1, width=6, state=DISABLED,
                                     textvariable=texto_bebida[contador])
    cuadros_bebida[contador].grid(row=contador, column=1, sticky=W)
    contador += 1

# Items para generar postre
variables_postre = []
cuadros_postre = []
texto_postre = []
contador = 0
for postre in lista_postres:
    variables_postre.append('')
    variables_postre[contador] = IntVar()
    postre = Checkbutton(panel_postres, text=postre.title(), font=('Dosis', 14, 'bold'), onvalue=1, offvalue=0,
                         variable=variables_postre[contador], command=revisar_check3)
    postre.grid(row=contador, column=0, sticky=W)
    # Crear los cuadros de entrada
    cuadros_postre.append('')
    texto_postre.append('')
    texto_postre[contador] = StringVar()  # Tipo de varible exclusivo de tkinter
    texto_postre[contador].set('0')
    cuadros_postre[contador] = Entry(panel_postres, font=('Dosis', 13, 'bold'), bd=1, width=6, state=DISABLED,
                                     textvariable=texto_postre[contador])
    cuadros_postre[contador].grid(row=contador, column=1, sticky=W)
    contador += 1


# variables de costos de comida
var_costo_comida = StringVar()

# Etiquetas de costos y campos de entrada
etiqueta_costo_comida = Label(panel_costos, text='Costo comida', font=('Dosis', 12, 'bold'), bg='aquamarine3',
                              fg='white')
etiqueta_costo_comida.grid(row=0, column=0)
texto_costo_comida = Entry(panel_costos, font=('Dosis', 12, 'bold'), bd=1, width=10, state='readonly',
                           textvariable=var_costo_comida)
texto_costo_comida.grid(row=0, column=1, padx=41)


# variables de costos de bebida
var_costo_bebida = StringVar()

# Etiquetas de costos y campos de entrada
etiqueta_costo_bebida = Label(panel_costos, text='Costo bebida', font=('Dosis', 12, 'bold'), bg='aquamarine3',
                              fg='white')
etiqueta_costo_bebida.grid(row=1, column=0)
texto_costo_bebida = Entry(panel_costos, font=('Dosis', 12, 'bold'), bd=1, width=10, state='readonly',
                           textvariable=var_costo_bebida)
texto_costo_bebida.grid(row=1, column=1, padx=41)

# variables de costos de postre
var_costo_postre = StringVar()

# Etiquetas de costos y campos de entrada
etiqueta_costo_postre = Label(panel_costos, text='Costo postre', font=('Dosis', 12, 'bold'), bg='aquamarine3',
                              fg='white')
etiqueta_costo_postre.grid(row=2, column=0)
texto_costo_postre = Entry(panel_costos, font=('Dosis', 12, 'bold'), bd=1, width=10, state='readonly',
                           textvariable=var_costo_postre)
texto_costo_postre.grid(row=2, column=1, padx=41)

# variables del subtotal
var_subtotal = StringVar()

# Etiquetas de costos y campos de entrada
etiqueta_subtotal = Label(panel_costos, text='Subtotal', font=('Dosis', 12, 'bold'), bg='aquamarine3',
                              fg='white')
etiqueta_subtotal.grid(row=0, column=2)
texto_subtotal = Entry(panel_costos, font=('Dosis', 12, 'bold'), bd=1, width=10, state='readonly',
                       textvariable=var_subtotal)
texto_subtotal.grid(row=0, column=3, padx=41)

# variables de los impuestos
var_impuestos = StringVar()

# Etiquetas de costos y campos de entrada
etiqueta_impuestos = Label(panel_costos, text='impuestos', font=('Dosis', 12, 'bold'), bg='aquamarine3',
                              fg='white')
etiqueta_impuestos.grid(row=1, column=2)
texto_impuestos = Entry(panel_costos, font=('Dosis', 12, 'bold'), bd=1, width=10, state='readonly',
                        textvariable=var_impuestos)
texto_impuestos.grid(row=1, column=3, padx=41)

# variables del total
var_total = StringVar()

# Etiquetas de costos y campos de entrada
etiqueta_total = Label(panel_costos, text='total', font=('Dosis', 12, 'bold'), bg='aquamarine3',
                       fg='white')
etiqueta_total.grid(row=2, column=2)
texto_total = Entry(panel_costos, font=('Dosis', 12, 'bold'), bd=1, width=10, state='readonly',
                    textvariable=var_total)
texto_total.grid(row=2, column=3, padx=41)


# botones
botones = ['total', 'recibo', 'guardar', 'resetear']
botones_creados = []
columnas = 0
for boton in botones:
    boton = Button(panel_botones, text=boton.title(), font=('Dosis', 11, 'bold'), fg='white', bg='azure4', bd=1,
                   width=9)
    boton.grid(row=0, column=columnas)
    botones_creados.append(boton)
    columnas += 1
botones_creados[0].config(command=lambda: total())
botones_creados[1].config(command=lambda: recibo())
botones_creados[2].config(command=lambda: guardar())
botones_creados[3].config(command=lambda: resetear())
# area de recibo
texto_recibo = Text(panel_recibo, font=('Dosis', 11, 'bold'), bd=1, width=43, height=10)
texto_recibo.grid(row=0, column=0)

# calculadora
visor_caluladora = Entry(panel_calculadora, font=('Dosis', 12, 'bold'), width=32, bd=1)
visor_caluladora.grid(row=0, column=0, columnspan=4)

# botones de la calculadora
botones_calculadora = ['7', '8', '9', '+', '4', '5', '6', '-', '1', '2', '3', 'x', 'CE', 'borrar', '0', '/']
botones_guardados = []
fila = 1
columna = 0
for boton in botones_calculadora:
    boton = Button(panel_calculadora, text=boton.title(), font=('Dosis', 9, 'bold'), fg='white', bg='azure4', bd=1,
                   width=9)
    boton.grid(row=fila, column=columna)
    columna += 1
    if columna == 4:
        fila += 1
        columna = 0
    botones_guardados.append(boton)

botones_guardados[0].config(command=lambda: click_boton('7'))
botones_guardados[1].config(command=lambda: click_boton('8'))
botones_guardados[2].config(command=lambda: click_boton('9'))
botones_guardados[3].config(command=lambda: click_boton('+'))
botones_guardados[4].config(command=lambda: click_boton('4'))
botones_guardados[5].config(command=lambda: click_boton('5'))
botones_guardados[6].config(command=lambda: click_boton('6'))
botones_guardados[7].config(command=lambda: click_boton('-'))
botones_guardados[8].config(command=lambda: click_boton('1'))
botones_guardados[9].config(command=lambda: click_boton('2'))
botones_guardados[10].config(command=lambda: click_boton('3'))
botones_guardados[11].config(command=lambda: click_boton('*'))
botones_guardados[12].config(command=lambda: ce())
botones_guardados[13].config(command=lambda: borrar())
botones_guardados[14].config(command=lambda: click_boton('0'))
botones_guardados[15].config(command=lambda: click_boton('/'))




# ***************************************************************************************************************
# ***************************************************************************************************************
# ***************************************************************************************************************
# Evitar que la ventana se cierre
# mainloop() es un metodo de la clase Tk en el cual ejecuta un bucle y al mismo tiempo debe de estar
# atento a eventos como clics de ratón, pulsaciones de teclas y otros eventos de entrada del usuario.
# Este bucle se ejecuta continuamente hasta que decides cerrar la ventana de la aplicación
aplicacion.mainloop()


