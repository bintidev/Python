
'''Tabla  de  multiplicar.  Se  debe  pedir  un  número  y  debe  mostrar  la  tabla  de 
multiplicar de ese número.'''

def mostrarTablas(num):

    tabla = ""

    for i in range(1): # iteracion unica (1 tabla)

        # para el multiplicador, numero por el que se multiplica el numero pasado
        # por parametro del [1,10]
        for j in range(1, 10 + 1):
            tabla += "{} * {} = {} \n".format(num, j, (num * j));

    return tabla