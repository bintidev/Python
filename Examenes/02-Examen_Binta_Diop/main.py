
'''from Material import Material
from Libro import Libro
from Revista import Revista'''
import math

class Material:

    material = {}
    lista_ids = []

    def __init__(self, id, titulo, autor, publicacion):

        self.id = id
        self.titulo = titulo
        self.autor = autor
        self.fecha_publicacion = publicacion
        
    def getIds(self):
        return self.lista_ids

    @classmethod
    def generarEstadisticas(self):

        totalMateriales = 0
        libros = 0
        revistas = 0
        pags = 0

        for i in range(len(self.material)):
            totalMateriales += 1

            if isinstance(self.material.values(), Libro):
                libros += 1
                pags += self.material.values().getPaginas()
            else:
                revistas += 1

        promedio_pags = pags / libros

        return f'[ Total materiales registrados: {totalMateriales} - Libros: {libros} - Revistas: {revistas}\n- Promedio páginas libros: {promedio_pags} ]'
    

    def buscarMaterial(self, id):

        if id in self.material.keys():
            return self.material[id]
        else:
            return False

    def eliminarMaterial(self, id):

        if id in self.material.keys():
            del self.material[id]
            return True
        else:
            return False

    @classmethod  
    def listarMateriales(self):

        resultado = ''

        for ids, mat in self.material.items():
            if isinstance(mat, Libro):
                tipo = 'libro'

            else:
                tipo = 'revista'

            resultado += f'[ Tipo: {tipo} - ID: {ids} - Titulo: {self.titulo} - Autor: {self.autor} - Año de publicación: {self.fecha_publicacion}'
    
        return resultado

########################################

class Libro(Material):

    def __init__(self, id, titulo, autor, publicacion, genero, paginas):

        super().__init__(id, titulo, autor, publicacion)
        self.genero = genero
        self.paginas = paginas
        super().material[id] = self
        super().lista_ids.append(id)

    def getPaginas(self):
        return self.paginas
    
    def getGenero(self):
        return self.genero
    
    def listarMaterial(self):
        resultado = super().listarMateriales()
        resultado += f'\nGenero: {self.getGenero()} - Número de páginas: {self.getPaginas()} ]'
        return resultado

##########################################

class Revista(Material):

    def __init__(self, id, titulo, autor, publicacion, num_edicion, mes_publicacion):

        super().__init__(id, titulo, autor, publicacion)
        self.numero_edicion = num_edicion
        self.mes_publicacion = mes_publicacion
        super().material[id] = self
        super().lista_ids.append(id)

    def getNumeroEdicion(self):
        return self.numero_edicion
    
    def getMesPublicacion(self):
        return self.mes_publicacion
    
    def listarMaterial(self):
        resultado = super().listarMateriales()
        resultado += f'\nNúmero de edición: {self.getNumeroEdicion()} - Mes de publicación: {self.getMesPublicacion()} ]'
        return resultado

###############################

def mostrarMenu():

    menu = [    "\n---------------------",
                "MENÚ DE OPCIONES",
                "---------------------",
                "a) Agregar Material",
                "b) Listar Materiales",
                "c) Buscar Material por ID",
                "d) Eliminar Material",
                "e) Generar Estadísticas",
                "f) Salir",
            ]

    for i in range(len(menu)):
        print(menu[i], end = "\n")


def opcionValida():

    op = input("\nIngrese una opción: ").lower()
    # no distingue entre mayusculas y minusculas
    validas = set("abcdef")

    while op not in validas:

        op = input("Error. Introduce una opción válida: ")

    return op


def agregarMaterial():

    id = input('Ingrese ID del material: ')

    '''while id in Material.getIds():
        id = input('Ingrese ID del material: ')'''

    titulo = input('Título: ')
    autor = input('Autor: ')
    publicacion = int(input('Año de publicación: '))

    while publicacion < 0 or publicacion > 2025 or math.isnan(publicacion):
        publicacion = int(input('Año de publicación: '))

    tipo = input('Tipo de Material (Libro o Revista): ').lower()
    tiposValidos = ['libro', 'revista']

    while tipo not in tiposValidos:
        tipo = input('Tipo de Material (Libro o Revista): ').lower()

    if tipo == 'libro':
        genero = input('Género: ').lower()
        generosValidos = ['ficcion', 'no ficcion', 'terror', 'ciencia']

        while genero not in generosValidos:
            genero = input('Género: ').lower()

        num_paginas = int(input('Número de páginas: '))

        while num_paginas < 0 or math.isnan(num_paginas):
            num_paginas = int(input('Número de páginas: '))

        libro = Libro(id, titulo, autor, publicacion, genero, num_paginas)

        return libro
    else:
        num_edicion = input('Número de edición: ')
        mesesValidos = ['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre']

        mes_publicacion = input('Mes de publicación: ').lower()

        while mes_publicacion not in mesesValidos:
            mes_publicacion = input('Mes de publicación: ').lower()

        revista = Revista(id, titulo, autor, publicacion, num_edicion, mes_publicacion)

        return revista

###########################

mostrarMenu()
entrada = opcionValida()

while (entrada != 'f'):

    if (entrada == 'a'):

        material = agregarMaterial()

    elif (entrada == 'b'):

        print(material.listarMateriales())

    elif (entrada == 'c'):

        id = input('Ingrese el ID del material que desea buscar: ')

        if Material.buscarMaterial(id) == False:
            print('Material no encontrado.')
        else:
            print(Material.buscarMaterial(id))

    elif (entrada == 'd'):

        id = input('Ingrese el ID del material que desea eliminar: ')

        if Material.eliminarMaterial(id) == False:
            print('Material no encontrado.')
        else:
            print('Se ha eliminado elmaterial exitosamente')

    elif (entrada == 'e'):

        Material.generarEstadisticas()

    mostrarMenu()
    entrada = opcionValida()

print("\nPrograma terminado. Bye bye! \n")
