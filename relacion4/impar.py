
# devuelve si un numero es impar para la operación mostrar rombo
def esImpar(numRombo):
    
    n = numRombo

    while (n % 2 == 0):
        n = int(input('Error. Ingrese un número impar: '))

    return n