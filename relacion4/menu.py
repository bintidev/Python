
# 1. Al arrancar debe mostrar un menú de opciones como el siguiente

# devuelve el menus de operaciones
def mostrarMenu():

    menu = [    "\n---------------------",
                "MENÚ DE OPCIONES",
                "---------------------",
                "a) Mostrar un rombo",
                "b) Adivinar un número",
                "c) Resolver una ecuación de segundo grado",
                "d) Tabla de números",
                "e) Cálculo del número factorial de un número",
                "f) Cálculo de un número de la sucesión de Fibonacci",
                "g) Tabla de multiplicar",
                "h) Salir"
            ]

    for i in range(len(menu)):
        print(menu[i], end = "\n")