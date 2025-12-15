
# Escribe un programa que recoja un número y calcule su factorial.

num = int(input("Introduce un número: "))

f = 1
i = num # empezando desde el numero proporcionado (incluido9)

while (i > 1):

    # imprime en una misma linea los números por los que se multiplica para obtener el factorial
    print (i,end="! ")
    f *= i # acumula las multiplicaciones
    i -= 1 # decremento por vuelta

print ("\nEl factorial de {} es {}".format(num,f))