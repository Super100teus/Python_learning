import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser
import datetime
import wikipedia


# Escuchar nueztro microfono y devolver audio como texto
def audio_a_texto():
    # Almacenar el recognaizer en variable
    r = sr.Recognizer()
    # Configurar el microfono
    with sr.Microphone() as origen:
        # tiempo de espera
        r.pause_threshold = 0.8

        # informar que empezo grabacion
        print('Ya puedes hablar')
        # guardar lo que escuche como audio
        audio = r.listen(origen)

        try:
            # buscar en google
            pedido = r.recognize_google(audio, language='es-mx')
            # prueba de que se pudo ingresar
            print(f'Dijiste: {pedido}')
            # Devolver pedido
            return pedido
        # En caso de no comprender el audio
        except sr.UnknownValueError:
            # prueba de comprendio el audio
            print('no se entendio')

            # devolver error
            return 'sigo esperando'

        # En caso de no resolver el pedido
        except sr.RequestError:
            # prueba de comprendio el audio
            print('no se entendio 2')

            # devolver error
            return 'sigo esperando'
        except:
            # prueba de comprendio el audio
            print('no se entendio 3')

            # devolver error
            return 'sigo esperando'


# funcion para que el asistente sea escuchado
def hablar(mensaje):
    # Encender el motor de pyttsx3
    engine = pyttsx3.init()
    engine.setProperty('voice', id3)
    # pronuciar mensaje
    engine.say(mensaje)
    engine.runAndWait()


'''engine = pyttsx3.init()
for voz in engine.getProperty('voices'):
    print(voz)'''


# Informar dia de la semana
def pedir_dia_semana():
    dia = datetime.date.today()
    print(dia)
    # crear var para dia de la semana
    dia_semana = dia.weekday()
    print(dia_semana)
    # Dicccionario con nombre de dias
    semana = {0: 'Lunes', 1: 'Martes', 2: 'Miercoles', 3: 'Jueves', 4: 'Viernes', 5: 'Sabado', 6: 'Domingo'}
    hablar(f'Hoy es {semana[dia_semana]}')


# opcion
id1 = 'HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\TTS_MS_EN-US_DAVID_11.0'
id2 = 'HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\TTS_MS_EN-US_ZIRA_11.0'
id3 = 'HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\TTS_MS_ES-MX_SABINA_11.0'


# Informar hora
def pedir_hora():
    # Crear variable con datos de la hora
    hora = datetime.datetime.now()
    hora = f' Son las {hora.hour} con {hora.minute} minutos y {hora.second} segundos'
    hablar(hora)


# Pedir saludo
def saludo():
    # crear variable con datos hora
    hora = datetime.datetime.now()
    if 5 > hora.hour >= 19:
        momento = 'Buenas noches'
    elif 5 <= hora.hour <= 13:
        momento = 'Buenos dias'
    else:
        momento = 'Buenas tardes'
    hora = f'{momento}, Son las {hora.hour} en que te puedo ayudar'
    hablar(hora)

# Funcion central del asistente
def pedir_cosas():
    saludo()
    # Variable de corte
    comenzar = True
    # loop central
    while comenzar:
        # Activar el microfono
        pedido = audio_a_texto().lower()
        if 'abrir youtube' in pedido:
            hablar('Claro')
            webbrowser.open('https://www.youtube.com/')
            continue
        elif 'abrir el navegador' in pedido:
            hablar('Claro')
            webbrowser.open('https://www.google.com/')
            continue
        elif "qué día es hoy" in pedido:
            pedir_dia_semana()
            continue
        elif 'qué hora es' in pedido:
            pedir_hora()
        elif 'buscar en wikipedia' in pedido:
            hablar('buscando en wikipedia')
            pedido = pedido.replace('busca en wikipedia', '')
            wikipedia.set_lang('es')
            resultado = wikipedia.summary(pedido, sentences=1)
            hablar('wikipedia dice lo siguiente')
            hablar(resultado)
            continue
        elif 'buscar en internet' in pedido:
            hablar('buscando')
            pedido = pedido.replace('busca en internet', '')
            pywhatkit.search(pedido)
            hablar('internet dice lo siguiente')
            continue
        elif 'terminar asistencia' in pedido:
            comenzar = False
            continue
        elif 'broma' in pedido:
            hablar(pyjokes.get_joke('es'))
            continue
        elif 'precio de acciones' in pedido:
            acciones = pedido.split('de')[-1].strip()
            cartera = {'apple': 'AAPL', 'amazon': 'AMZN', 'google': 'GOOGL'}
            try:
                accion_buscada = cartera[acciones]
                accion_buscada = yf.Ticker(accion_buscada)
                precio_ctual = accion_buscada.info['regularMarketPrice']
                hablar(f'El precio de {acciones} es {precio_ctual}')
                continue
            except:
                print('No lo he encontrado')



pedir_cosas()
