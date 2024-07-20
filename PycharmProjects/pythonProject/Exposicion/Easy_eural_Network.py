"""En este modulo escribire un modelo sumamente simple de una red neural"""
# Importaremos librerias
import numpy as np
import os

# Set the environment variable
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
import tensorflow as tf
import matplotlib.pyplot as plt

'''             Estos ejmplos seran usados por la red para aprender              '''

celsius = np.array([40, 10, 0, 8, 15, 22, 38], dtype=float)  # Arreglo de numeros con las 7 entradas de grados celcius
fahrenheit = np.array([-40, 14, 32, 46, 59, 72, 100], dtype=float)  # Arreglo con las salidas o resultados en Fº

'''----------------------------------------------------------------------------------'''
''' Usare el framework Keras, este framework nos permite hacer las redes neuronales de manera simple 
(es decir hace lo mas dificil por nosotros) '''

capa = tf.keras.layers.Dense(units=1, shape=[1])
#capa_salida=tf.keras.layers.Dense(units=1)
'''Una capa del tipo densa se refiera a que cada neurona tiene una conexion con todas
las neuronas de la siguiente capa. Con el la variable "units" se le dice las neuronas que tendra en la capa de salida
y con la variable input_shape se le dice cuantas neuronas tendra en la capa de entrada '''
modelo = tf.keras.Sequential([capa])  # El modelo de esta red sera secuencial


# A continuacion empezara el entrenamiento del modelo, lo cual se reduce a puros calculos matematicos

modelo.compile(optimizer=tf.keras.optimizers.Adam(0.1),
               loss='mean_squared_error')  # Adam permite a la red saber como ajustar los pesos y
# sesgos de manera eficiente para que pueda aprender y llegar a los valores deseados
'''El valor numerico pasado a Adam es la taza de aprendizaje, ese numero le dice que tanto ajustar los pesos y sesgos,
si le ponemos un numero muy pequeño la red aprendera muy poco a poco de manera muy lenta, y si le ponemos un numero 
muy grande los resultados seran muy inexactos por lo que no podra realizar los aajustes finales que seran muy finos'''

#     Compilando entrenamiento
historial = modelo.fit(celsius, fahrenheit, epochs=1000, verbose=False)
# historial = modelo.fit
# (Datos de entrada, datos de salida a buscar, numero de vueltas para comparacion, para evitar exceso de impresiones)
plt.xlabel("# Epoca")
plt.ylabel("# Magnitud perdida")
plt.plot(historial.history["loss"])

