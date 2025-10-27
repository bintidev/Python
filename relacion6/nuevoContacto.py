
'''Añadir un nuevo contacto. Se debe leer por teclado un nombre de contacto y su 
número de teléfono. Se añade en el diccionario. Si ya existe, se informa que ya 
existe y pregunta si se quiere actualizar su teléfono. Si se responde 
afirmativamente se actualiza.'''

def aniadir(n, t, dicc):
    
    dicc[n] = t
    lista = dicc

    return lista