
def operacion(msj):

    proceder = False
    
    eleccion = input(f'{msj} ')

    if (eleccion.lower() == 's'):
        proceder = True

    return proceder