
import confirmar, existencia

class Persona:

    __contacto = dict()

    # CONSTRUCTOR
    def __init__(self, nombre, direcc, tel):
        self.__contacto[nombre] = [direcc, tel]

    '''Listado de contactos por orden alfabético. Se muestra el contenido ordenado 
    por orden alfabético de los contactos, con el siguiente formato:

    Nombre: xxx Dirección: xxx Teléfono: xxx'''
    @classmethod
    def mostrar_alfabeticamente(cls):

        lista = ''

        for k,v in sorted(cls.__contacto.items()):
    
            # accede a las posiciones de cada uno de los valores almacenados
            lista += f'\nNombre: {k} - Dirección: {v[0]} - Tel: {v[1]}';

        return lista
    
    '''Añadir  un  nuevo  contacto.  Se  debe  leer  por  teclado  un  nombre  de  contacto, 
    dirección y número de teléfono. Se añade en el diccionario. Si ya existe, se informa 
    que  ya  existe  y  pregunta  si  se  quiere  actualizar  su  teléfono.  Si  se  responde 
    afirmativamente se actualiza.'''
    @classmethod
    def nuevo_contacto(cls, nombre, direcc, tel):

        # verificacion de la existencia del contacto
        if (existencia.existeContacto(nombre, cls.__contacto) == True):

            # para confirmar que se desea actualizar
            if (confirmar.operacion('Este contacto ya existe. ¿Desea actualizarlo? [ S / N ]: ')):
                p = Persona(nombre, direcc, tel)
                aniadido = True

            else:
                # de lo contrario se queda el contacto tal como esta
                aniadido = False

        else:
            # si el contacto no existe, automaticamente lo añade como unp nuevo
            p = Persona(nombre, direcc, tel)
            aniadido = True

        return aniadido

    '''Modificar un contacto. Se pide un nombre de contacto. Si no existe, se pregunta 
    si se desea insertar. Si se responde afirmativamente (o el contacto ya existía), se 
    pide la dirección y el número de teléfono, y se actualiza el diccionario.'''
    @classmethod
    def modificar_contacto(cls, nombre):

        # verificacion de la existencia del contacto
        if (existencia.existeContacto(nombre, cls.__contacto) == False):

            # para confirmar que se desea insertar
            if (confirmar.operacion('Este contacto no existe. ¿Desea insertarlo? [ S / N ]: ')):

                # informacion para el nuevo contacto
                direcc = input('Ingrese la dirección de domicilio de la persona: ')
                tel = input('Ingrese el número de teléfono asociado: ')

                # creacion del nuevo contacto
                cls.__contacto[nombre] = [direcc,tel]
                modificado = True

            else:
                # de lo contrario no se inserta ningun nuevo contacto
                modificado = False

        else:
            # si el contacto existe, se modifica su informacion automaticamente
            # nueva informacion para el contacto
            direcc = input('Ingrese la nueva dirección: ')
            tel = input('Ingrese el nuevo teléfono: ')

            # modificacion con la informacion dada
            cls.__contacto[nombre] = [direcc,tel]
            modificado = True

        return modificado
    
    '''Buscar un número de teléfono. Se pide un número de teléfono de contacto y se 
    busca en el diccionario. Si se encuentra, se indica el nombre del contacto, en otro 
    caso se indica que no se encuentra.'''
    @classmethod
    def buscar_contacto(cls, tel):
        
        buscado = ''
        
        for nombre, telefono in cls.__contacto.items():
            
            if telefono[1] == tel:
                
                buscado = nombre
                
        return buscado
    
    
    '''Eliminar un contacto. Se pide un nombre de contacto. Si no existe, se indica que 
    no se encuentra, si existe se debe eliminar del diccionario.'''
    @classmethod
    def eliminar_contacto(cls, nombre):
        
        eliminado = False
        
        if nombre in cls.__contacto.keys():
            
            del cls.__contacto[nombre]
            eliminado = True
            
        return eliminado