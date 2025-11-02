
import existencia

'''Eliminar un contacto. Se pide un nombre de contacto. Si no existe, se indica que 
no se encuentra, si existe se debe eliminar del diccionario.'''

def eliminarContacto(nombre, dicc):

    borrado = False

    if(existencia.existeContacto(nombre, dicc)):

        del dicc[nombre]
        borrado = True

    return borrado