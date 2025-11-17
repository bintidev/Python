'''Escribe un programa que recoja dividendo y divisor, y realice su división
siempre que el divisor sea distinto de cero.'''

dividendo = int(input("Introduce el dividendo: "))
divisor = int(input("Introduce el divisor: "))

# validación del divisor
esCero = False if (divisor != 0) else True

if(esCero):
    print ("El divisor no puede ser cero")
else:
    resultado = dividendo / divisor
    print ("El cociente de la división es",resultado)