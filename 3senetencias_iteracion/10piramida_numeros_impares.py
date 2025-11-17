
'''Escribe un programa que recoja un número y muestre un triángulo formado por
secuencias decrecientes de números impares. Por ejemplo, si se introduce el
5 se debe mostrar:
1
3 1
5 3 1
7 5 3 1
9 7 5 3 1'''

n = int(input("Introduzca un número para la base del triángulo: "))

for i in range(1, n + 1):

    primeroFila = (2 * i) - 1 # determinar el numero de comienzo de cada fila

    # por cada fila se comienza imprimiendo desde el primer numero de fila (primeroFila)
    # terminando en 1, decreciendo en 2 (para imprimir solo impares)
    for j in range(1, primeroFila, 2):

        print (str(j))