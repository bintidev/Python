
'''Escribe un programa que recoja un número de filas y columnas, y muestre una
tabla con tantas filas y columnas como indicadas, numerando las celdas de
izquierda a derecha y de arriba abajo. Por ejemplo, si se introducen 2 filas y 3
columnas, se debe mostrar:
1   2   3
4   5   6'''

filas = int(input("Introduce un número de filas: "))
columnas = int(input("Introduce un número de columnas: "))

i = 1 # para la numeracion de celdas

for f in range(filas):
    for c in range(columnas):
        print (i, end="    ")
        i += 1
    print() # salto de linea por fila