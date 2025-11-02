
# 1. Al arrancar debe mostrar un menú de opciones como el siguiente

# devuelve el menu de operaciones
def mostrarMenu():

    menu = [    "\n---------------------",
                "MENÚ DE OPCIONES",
                "---------------------",
                "a) Listado de teléfonos, usando el orden por defecto.",
                "b) Listado de teléfonos por orden alfabético.",
                "c) Añadir un nuevo contacto.",
                "d) Modificar el teléfono de un contacto.",
                "e) Buscar un número de teléfono.",
                "f) Eliminar un contacto.",
                "g) Borrar el listín telefónico.",
                "h) Salir."
            ]

    for i in range(len(menu)):
        print(menu[i], end = "\n")