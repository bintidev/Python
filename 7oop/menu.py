
# devuelve el menus de operaciones
def mostrarMenu():

    menu = [    "\n---------------------",
                "MENÚ DE OPCIONES",
                "---------------------",
                "a) Listado de contactos por orden alfabético",
                "b) Añadir un nuevo contacto",
                "c) Modificar un contacto",
                "d) Buscar un número de teléfono",
                "e) Eliminar un contacto",
                "f) Salir",
            ]

    for i in range(len(menu)):
        print(menu[i], end = "\n")