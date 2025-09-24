
# Escribe un programa que recoja tres números y calcule su media aritmética.

n = 0
num = 0
suma = 0

# pide 3 números al usuario y almacena su suma en la variable suma
# conforme son introducidos por teclado
for n in range (3):
    num = float(input("Introduce un número: "))
    suma+=num

media = suma / 3

print ("La media de los números introducidos es", media)