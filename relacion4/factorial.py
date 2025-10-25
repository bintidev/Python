
'''Cálculo del número factorial de un número. Se debe pedir un número y se debe
calcular su factorial (este ejercicio ya está resuelto, prueba a hacer una solución
recursiva).'''

def factorialNumero(num):

    if num == 1 or num == 0: # los factoriales de 1 y 0 es 1
        
        return 1
    
    else:

        # devuelve el numero pasado multiplicado por el que le precede
        # se decrementa simultaneamente el valor de num por cada llamada efectuada
        return num * factorialNumero(num - 1)