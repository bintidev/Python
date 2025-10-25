
# 1. Al arrancar debe mostrar un menú de opciones como el siguiente

# devuelve el menus de operaciones
def mostrarMenu():

    menu = [    "\n---------------------",
                "MENÚ DE OPCIONES",
                "---------------------",
                "1. Mostrar secuencia de números",
                "2. Mostrar secuencia de caracteres",
                "3. Palíndromo",
                "4. Palabra palíndroma de otra",
                "5. Salir"
            ]

    for i in range(len(menu)):
        print(menu[i], end = "\n")