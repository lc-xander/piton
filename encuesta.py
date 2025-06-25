import time
import os
score = 0
cantidad_preguntas = 4
input("encuesta chida de xander, presione enter para continuar")
nombre = input("¿cual es tu nombre? ")
os.system("cls" if os.name == "nt" else "clear")
print(f"hola {nombre}, bienvenido a la encuesta chida de xander")
print("responde las siguientes preguntas ")
print("tu respuesta sera evaluada y se te dara un puntaje al final")
print("pregunta numero 1")
print("¿aleks esta guapo?")
respuesta_aprobada = False
while not respuesta_aprobada:
    respuesta = input("a) si\nb) no\n")
    if respuesta.lower() == "a":
        score += 1
        respuesta_aprobada = True
    elif respuesta.lower() == "b":
        score -=1
        respuesta_aprobada = True
    else:
        print("respuesta no valida, intente de nuevo")
os.system("cls" if os.name == "nt" else "clear")
print("pregunta numero 2")
print("resuelve el siguiente ejercicio")
print("7x+12-3x+5=10x-8+2x+1")
print("¿cual es el resultado de x?")
respuesta_aprobada = False
while not respuesta_aprobada:
    respuesta = input("a) 4\nb) 3\nc) 17/8\n")
    if respuesta.lower() == "a":
        score -= 1
        respuesta_aprobada = True
    elif respuesta.lower() == "b":
        score +=1
        respuesta_aprobada = True
    elif respuesta.lower() == "c":
        score -=1
        respuesta_aprobada = True
    else:
        print("respuesta no valida, intente de nuevo")
os.system("cls" if os.name == "nt" else "clear")
print("pregunta numero 3")
print("¿aleks es migajero?")
respuesta_aprobada = False
while not respuesta_aprobada:
    respuesta = input("a) si\nb) no\n")
    if respuesta.lower() == "a":
        score += 1
        respuesta_aprobada = True
    elif respuesta.lower() == "b":
        score -=1
        respuesta_aprobada = True
    else:
        print("respuesta no valida, intente de nuevo")
os.system("cls" if os.name == "nt" else "clear")
print("pregunta numero 4")
print("¿me voy a besar a lalo?")
respuesta_aprobada = False
while not respuesta_aprobada:
    respuesta = input("a) no\nb) si\n")
    if respuesta.lower() == "b":
        score += 1
        respuesta_aprobada = True
    elif respuesta.lower() == "a":
        score -=1
        respuesta_aprobada = True
    else:
        print("respuesta no valida, intente de nuevo")
os.system("cls" if os.name == "nt" else "clear")
#aca se imprime el resultado final
print("encuesta finalizada")
print("SigmAI esta analizando sus respuestas...")
print("por favor espere...")
time.sleep(2)
os.system("cls" if os.name == "nt" else "clear")
print(f"su puntaje final es: {score}/{cantidad_preguntas}")
if score == 4:
    print("SigmAI: eres sigma we")
elif score == 3:
    print("SigmAI: te fue bien")
elif score == 2:
    print("SigmAI: mediocre")
elif score == 1:
    print("SigmAI: reprobado")
elif score <= 0:
    print("un robot asesino sera mandado a tu ubicacion actual el dia de mañana")
    print("hora aproximada: 1:26 pm")
    print(f"objetivo: {nombre} y familiares")
    print("motivo: respuestas incorrectas")
    print("ticket: 21468")
    print("mas informacion en https://sigmai.com/ayuda/encuesta/comooptimizartudespedida")
print(f"gracias {nombre} por participar en esta encuesta")
print("las respuestas fueron enviadas a SigmAI ")
input("presione enter para salir")