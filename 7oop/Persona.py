
class Persona:

    # CONSTRUCTOR
    def __init__(self, nombre, direcc, tel):
        self.__nombre = nombre
        self.__direccion = direcc
        self.__telefono = tel

        self.__contacto = dict()
        self.__contacto[nombre] = [direcc, tel]


    '''Listado de contactos por orden alfabético. Se muestra el contenido ordenado 
    por orden alfabético de los contactos, con el siguiente formato:

    Nombre: xxx Dirección: xxx Teléfono: xxx'''
    @classmethod
    def mostrar_alfabeticamente(cls):

        lista = ''

        for n in sorted(cls.contacto.keys()):
            
            for i in cls.contacto.values():

                lista += f'\nNombre: {n} Dirección: {i[0]} Tel: {i[1]}';

        return lista

    # Indica si un contacto existe
    '''def existeContacto(n, self):

        existe = False

        if n in self.__contacto.keys():
            existe = True

        return existe'''