
import numerico, aleatorio

'''Tabla de números. Se debe pedir un número de filas y un número de columnas.
A continuación, mostrará una tabla con números aleatorios con las filas y
columnas indicadas.'''

def tablaDenumeros(filas, columnas):

    for i in range(filas):

        for j in range(columnas):

            numAleatorio = aleatorio.numAleatorio()
            print (numAleatorio, end="  ")

        print()