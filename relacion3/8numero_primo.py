
# Escribe un programa que recoja un número y calcule si es primo.

n = int(input("Introduce un número: "))

contador = 2
esPrimo = False

# PENDIENTE DE ARREGLO APARA VALIDACION DEL 2 COMO NUM PRIMO
while (n % contador != 0 and contador < n):
    contador += 1
    esPrimo = True

if (esPrimo):
    print ("El número {} es un número primo".format(n))
else:
    print ("El número {} no es un número primo".format(n))