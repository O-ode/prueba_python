from queue import Queue
from threading import Thread
USERS = {"Alice":1234, "Bob":4321}
TIMEOUT = 10
inputQueue = Queue()

class Puerta:
    def __init__(self) -> None:
        self.open = False

#Función que se usará para obtener input de manera no bloqueante
def get_keyboard_input(inputQueue):
    while (True):
        input_str = input()
        inputQueue.put(input_str)
    pass

#Obtención y transformación de la cadena desde una Queue
def get_from_queue():
    strIn = None
    try:
        strIn = inputQueue.get(timeout=10)
        strIn = int(strIn)
    except Exception as e:
        pass
    return strIn

def ask_for_pass():
    for attempt in range(1,4):
        print(f"\nIntento {attempt}. Por favor, introduce tu contraseña:")
        passwd = get_from_queue()
        if passwd is None: print("Se ha acabado el tiempo.")
        elif passwd in USERS.values(): return list(USERS.keys())[list(USERS.values()).index(passwd)]
    return None

# Al ser un programa pequeño, dejo este hilo como un daemon para que no bloquee la ejecución del programa y se limpie de la memoria al salir
inputThread = Thread(target=get_keyboard_input, args=([inputQueue]),daemon=True)
inputThread.start()

puerta = Puerta()
user = ask_for_pass()
if user is not None:
    puerta.open = True
    print(f'Hola, {user}. Puerta desbloqueada.')
else:
    print(f'No se ha introducido una contraseña correcta, la puerta permanece cerrada.')