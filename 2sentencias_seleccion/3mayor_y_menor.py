# Escribe un programa que lea tres números y que muestre los números mayor y menor.

mayor = 0
menor = 0

for i in range(3):
    n = int(input("Introduce un número: "))

    if (n > mayor):
        mayor = n
    elif (n < menor):
        menor = n

print ("El mayor de los tres número es el",mayor,"y el menor es",menor)