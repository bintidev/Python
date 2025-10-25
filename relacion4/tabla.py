
import aleatorio

'''Tabla de números. Se debe pedir un número de filas y un número de columnas.
A continuación, mostrará una tabla con números aleatorios con las filas y
columnas indicadas.'''

def tablaDenumeros(filas, columnas):

    tabla = ""

    for i in range(filas):

        for j in range(columnas):

            numAleatorio = aleatorio.numAleatorio() # numero aleaotrio por celda
            tabla += numAleatorio, "end='  '" # espacio entre columnas

        tabla += print()