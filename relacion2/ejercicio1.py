# Escribe un programa que recoja un número e indique si se trata de un número
#par o impar

num = int(input("Introduzca un número entero: "))

if (num % 2 == 0):
    print ("El número {} es par".format(num))
else:
    print ("El número {} es impar".format(num))