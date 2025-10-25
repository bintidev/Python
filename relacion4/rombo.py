
import impar

'''Mostrar un rombo. Se debe recoer un número impar (debe asegurarse de que
sea impar, en caso de no serlodebe descratarlo y pedirlo de nuevo). Una vez
tenga el número impar debe mostrar un rombo de asteriscos. Por ejemplo, si se
introduce el valor 7 se debe mostrar:
   *
  ***
 *****
*******
 *****
  ***
   *'''

def mostrarRombo(base):

    # asegura que la base es impar antes de continuar
    baseimpar = impar.esImpar(base)
    mitad = baseimpar // 2 # division entera para determinar la linea del medio del rombo

    # bucle que dibuja la parte superior del rombo
    for i in range(mitad + 1): # desde primera línea hasta línea central (ambas inluidas)
        espacios = mitad - i # calcular espacios a la izquierda
        asteriscos = 2 * i + 1
        rombo += " " * espacios + "*" * asteriscos + "\n"

    # bucle que dibuja la parte inferior del rombo
    for i in range(mitad - 1, -1, -1): # desde línea siguiente a la central
        espacios = mitad - i
        asteriscos = 2 * i + 1
        rombo += " " * espacios + "*" * asteriscos + "\n"

    return rombo