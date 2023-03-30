import itertools
import random

# Preguntar si se incluirán caracteres especiales
caracteres_especiales = input("¿You want to include special characters? (s/n): ")

if caracteres_especiales.lower() == "s":
    # Definir los caracteres que se combinarán, incluyendo caracteres especiales
    caracteres = "abcdefghijklmnopqrstuvwxyz!#$%&()*+,-./:;<=>?@[\\]^_`{|}~"
    caracteres_mayus = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numeros = "0123456789"
else:
    # Definir los caracteres que se combinarán, sin caracteres especiales
    caracteres = "abcdefghijklmnopqrstuvwxyz"
    caracteres_mayus = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numeros = "0123456789"

# Pedir la cantidad de letras mayúsculas y minúsculas
cant_mayus = int(input("Enter the amount of the number of capital letters you want to include: "))
cant_minus = int(input("Enter the amount of the number of lowercase letters you want to include: "))

# Pedir la cantidad de números que se incluirán
cant_numeros = int(input("Enter the amount of the numbers of numbers you want to include: "))

# Pedir la cantidad de combinaciones a generar
cant_combinaciones = int(input("Enter the amount of the number of combinations you want to generate: "))

# Calcular la longitud total de cada combinación
longitud = cant_mayus + cant_minus + cant_numeros

# Generar múltiples combinaciones
for i in range(cant_combinaciones):
    # Elegir al azar los caracteres que se utilizarán en cada combinación
    caracteres_comb = [random.choice(caracteres) for i in range(longitud-cant_mayus-cant_minus-cant_numeros)]
    caracteres_mayus_comb = [random.choice(caracteres_mayus) for i in range(cant_mayus)]
    caracteres_minus_comb = [random.choice(caracteres) for i in range(cant_minus)]
    numeros_comb = [random.choice(numeros) for i in range(cant_numeros)]

    # Combinar todos los caracteres
    caracteres_comb.extend(caracteres_mayus_comb)
    caracteres_comb.extend(caracteres_minus_comb)
    caracteres_comb.extend(numeros_comb)

    # Mezclar los caracteres para generar combinaciones únicas
    random.shuffle(caracteres_comb)

    # Convertir la lista de caracteres en una cadena
    combinacion = ''.join(caracteres_comb)

    # Escribir la combinación en el archivo "generated.txt"
    with open("generated.txt", "a") as archivo:
        archivo.write(combinacion + "\n")

print(f"Generated {cant_combinaciones} combinations 'generated.txt'.")
