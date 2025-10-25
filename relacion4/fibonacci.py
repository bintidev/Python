
'''Cálculo de un número de la sucesión de Fibonacci. Se debe pedir una posición y 
debe calcular el número de la sucesión de Fibonacci en esa posición. La sucesión 
de Fibonacci es la siguiente: 
1 1 2 3 5 8 13 21... 
Es  decir,  a  partir  de  los  dos  primeros  valores  (que  son  1),  cualquier  valor  es  la 
suma de los dos anteriores.'''

def secuenciaFib(pos):

    if pos == 0 or pos == 1:
        fib = 1

    else:

        for i in range(pos + 1):
            
            fib = (i - 1) + (i - 2)
            if i == 1:
                i = 0

    return fib