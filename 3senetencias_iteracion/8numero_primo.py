
# Escribe un programa que recoja un número y calcule si es primo.

n = int(input("Introduce un número: "))

contador = 2
esPrimo = True

# PENDIENTE DE ARREGLO APARA VALIDACION DEL 2 COMO NUM PRIMO
while (contador < n):

    if (n % contador == 0):
        esPrimo = False

    contador += 1

if (esPrimo):
    print ("El número {} es un número primo".format(n))
else:
    print ("El número {} no es un número primo".format(n))