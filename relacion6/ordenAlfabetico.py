
'''Listado  de  teléfonos  por  orden  alfabético.  Ahora  se  muestra  el  contenido 
ordenado por orden alfabético de los contactos.'''

def mostrar(dicc):

    lista = ''

    for nombre, tel in sorted(dicc.items()):
        lista += "Nombre de Contacto: {} - Número de Teléfono: {} \n".format(nombre, tel)

    return lista