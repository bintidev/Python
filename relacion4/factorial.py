
import numerico

'''Cálculo del número factorial de un número. Se debe pedir un número y se debe
calcular su factorial (este ejercicio ya está resuelto, prueba a hacer una solución
recursiva).'''

def factorialNumero(num):

    if num == 1:
        
        f = 1
    
    else:

        f = num * factorialNumero(num - 1)

    return f