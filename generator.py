import itertools
import random

# Pedir la cantidad de letras mayúsculas y minúsculas
cant_mayus = int(input("Enter the number of capital letters you want to include: "))
cant_minus = int(input("Enter the number of lowercase letters you want to include: "))

# Pedir la cantidad de números que se incluirán
cant_numeros = int(input("Enter the number of numbers you want to include: "))

# Definir los caracteres que se combinarán
caracteres = "abcdefghijklmnopqrstuvwxyz"
caracteres_mayus = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numeros = "0123456789"

# Calcular la longitud total de cada combinación
longitud = cant_mayus + cant_minus + cant_numeros

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
with open("generated.txt", "w") as archivo:
    archivo.write(combinacion + "\n")

#El creador es español, por si quieres leer la descripcion y no entiendes (para ingleses)
#The creator is Spanish, in case you want to read the description and don't understand (for English)