
# 1. Al arrancar debe mostrar un menú de opciones como el siguiente

# devuelve el menus de operaciones
def mostrarMenu():

    menu = [    "\n---------------------",
                "MENÚ DE OPCIONES",
                "---------------------",
                "1. Contar vocales",
                "2. Contar palabras",
                "3. Suma de dígitos",
                "4. Rotar una lista",
                "5. Lista de elementos mayor y menor de otra",
                "6. Eliminar extremos de una lista",
                "7. Lista de elementos finales de otra",
                "8. Lista de elementos entre rango de posiciones",
                "9. Lista de elementos N iniciales y N finales de otra",
                "10. Comparación de rectángulos",
                "11. Intercambio de coordenadas de un punto",
                "12. Salir"
            ]

    for i in range(len(menu)):
        print(menu[i], end = "\n")