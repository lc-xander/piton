import os
import sys
import time
import datetime
import socket
def get_ip():
    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname)
    return ip
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")
def wait(seconds):
    time.sleep(seconds)
def execute_command(command):
        if command.lower() == "help":
            print("Comandos disponibles:")
            print("help - Muestra esta ayuda")
            print("clear - Limpia la pantalla")
            print("exit - Sale del sistema")
            print("open <nombre> - Abre un programa o archivo")
            print("about - Muestra información sobre el sistema")
            print("date - Muestra la fecha y hora actual")
            print("ip - Muestra tu dirección IP local")
            print("echo <texto> - Muestra el texto proporcionado")
        elif command.lower() == "clear":
             clear_screen()
        elif command.lower() == "exit":
            sys.exit()
        elif command.lower().startswith("open "):
            filename = command[5:].strip()
            if os.path.exists(filename):
                os.system(f"python {filename}")
            else:
                print(f"El archivo o programa '{filename}' no existe.")
        elif command.lower() == "about":
            print("mangOS beta 0.1")
            print()
            print("version de python:", sys.version.split()[0])
            print("desarrollado por bro macetas tecnology")
            print("ingrese help para ver los comandos disponibles")
        elif command.lower() == "date":
            print("Fecha y hora actual:", datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        elif command.lower() == "ip":
            print("Tu IP local es:", get_ip())
        elif command.startswith("echo "):
            texto = command[5:]  # recorta "echo "
            print(texto)
        else:
            print(f"Comando desconocido: {command}. Escriba 'help' para ver los comandos disponibles.")

clear_screen()
print("mangOS beta 0.1")
print()
print("version de python:", sys.version.split()[0])
print("desarrollado por bro macetas tecnology")
print("ingrese help para ver los comandos disponibles")
while True:
    command = input("admin>")
    execute_command(command)


    
