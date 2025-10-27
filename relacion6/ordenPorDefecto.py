
'''Listado de teléfonos, usando el orden por defecto. Se muestra por pantalla el 
contenido del diccionario, según el orden por defecto (el de inserción de 
elementos). El listado será de la forma: 

Nombre – Teléfono.'''

def mostrar(dicc):

    lista = ''

    for nombre, tel in dicc.items():
        lista += "Nombre de Contacto: {} - Número de Teléfono: {} \n".format(nombre, tel)

    return lista