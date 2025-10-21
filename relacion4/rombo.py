
import numerico, impar

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

    

    for i in range(1, base + 1, 2):
        espacios = (base - i) // 2
        print (" " * espacios + "*" * i)

        for j in range(base - 2, 0, -2):
            espacios = (base - i) // 2
            print (" " * espacios + "*" * i)