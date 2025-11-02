
'''Buscar un número de teléfono. Se pide un número de teléfono de contacto y se 
busca en el diccionario. Si se encuentra, se indica el nombre del contacto, en otro 
caso se indica que no se encuentra.'''

def porNumero(numTel, dicc):

    buscado = ''

    for i in dicc.keys():

        if dicc[i] == numTel:

            # si el telefono almacenado por la clave es igual al numero
            # que se busca, se almacena la clave, es decir, el nombre
            # del contacto
            buscado = i

    return buscado