
import existencia

'''Modificar  el  teléfono  de  un  contacto.  Se  pide  un  nombre  de  contacto.  Si  no 
existe,  se  pregunta  si  se  desea  insertar.  Si  se  responde  afirmativamente  (o  el 
contacto ya existía), se pide el número de teléfono y se actualiza el diccionario.'''

def actualizarTelefono(n, dicc):

    if (existencia.existeContacto(n, dicc) == False):

        eleccion = input('Este contacto no existe. ¿Desea insertarlo? [ S / N ] ')

        if (eleccion.lower() == 's'):
            dicc[n] = input('Ingrese el número de teléfono: ')

    else:
        dicc[n] = input('Ingrese el número de teléfono actualizado: ')

    return dicc