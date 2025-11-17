
'''Borrar  el  listín  telefónico.  Se  pide  confirmación  de  la  operación.  Si  el  usuario 
responde afirmativamente, se borra todo el diccionario.'''

def borrarListin(r, dicc):

    borrado = False

    if r.lower() == 's':

        dicc.clear()
        borrado = True

    return borrado