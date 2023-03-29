import itertools
import random

# Pedir la cantidad de letras mayúsculas y minúsculas
cant_mayus = int(input("Ingrese la cantidad de letras mayúsculas que desea incluir: "))
cant_minus = int(input("Ingrese la cantidad de letras minúsculas que desea incluir: "))

# Pedir la cantidad de números que se incluirán
cant_numeros = int(input("Ingrese la cantidad de números que desea incluir: "))

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

# Escribir la combinación en el archivo "generado.txt"
with open("generado.txt", "w") as archivo:
    archivo.write(combinacion + "\n")

