
# Escribe un programa que recoja un número y muestre su valor absoluto.

n = int(input("Introduce un número: "))
valAb = 0

# valor absoluto: distancia de un número a cero en la recta númerica
if (n > 0):
    valAb = n
elif (n < 0):
    valAb = (n) * (-1)
else:
    valAb = 0

print("El valor absoluto de",n,"es",valAb)