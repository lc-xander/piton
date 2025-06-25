#no se que es esto pero lo voy a hacer
import random
print("generador de contraseñas aleatorias")
caracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+"
longitud = int(input("Ingrese la longitud de la contraseña: "))
contraseña = "".join(random.choice(caracteres) for _ in range(longitud))
print("contraseña generada")
print(contraseña)