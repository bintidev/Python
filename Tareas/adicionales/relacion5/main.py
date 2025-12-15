
import menu, opcion, vocales, palabras, suma, lista

menu.mostrarMenu()
entrada = opcion.opcionValida()

while (entrada != 12):

    # contar vocales
    if (entrada == 1):

        cadena = input("Ingrese una cadena de texto: ")

        cantidadVocales = vocales.contar(cadena)

        print("\nSe han encontrado {} vocales en la palabra".format(cantidadVocales))

    # contar palabras
    elif (entrada == 2):

        cadena = input("Ingrese una cadena de texto: ")

        cantidadPalabras = palabras.contar(cadena)

        print("\nHay un total de {} palabras en el texto".format(cantidadPalabras))

    # sumar digitos
    elif (entrada == 3):

        numeros = input("Ingrese una secuencia numérica separada por comas: ")

        resultado = suma.sumarDigitos(numeros)

        print("\nResultado de la suma de los dígitos: {}".format(resultado))

    # rotar lista
    elif (entrada == 4):

        numeros = input("Ingrese una secuencia numérica separada por comas: ")
        posicion = int(input("Indique los N primeros número que desea mover al final: "))

        resultado = lista.rota(posicion, numeros)

        print("\nResultado tras la rotación de los {} primeros elementos: {}".format(posicion, resultado))

    # lista formada por mayor y menor de otra
    elif (entrada == 5):

        numeros = input("Ingrese una secuencia numérica separada por comas: ")

        resultado = lista.rango(numeros)

        print("\nLsita con los valores menor y mayor de la introducida: {}".format(resultado))

    # eliminar exterior de una lista
    elif (entrada == 6):

        numeros = input("Ingrese una secuencia numérica separada por comas: ")

        resultado = lista.interior(numeros)

        print("\nResultado tras la eliminación de los extremos: {}".format(resultado))

    # lista compuesta por n finales de otra
    elif (entrada == 7):

        numeros = input("Ingrese una secuencia numérica separada por comas: ")
        posicion = int(input("Indique los N últimos número que compondrán la nueva lista: "))

        resultado = lista.finales(posicion, numeros)

        print("\nLista con los {} últimos números de la proporcionada: {}".format(posicion, resultado))

    # lista segmentada
    elif (entrada == 8):

        numeros = input("Ingrese una secuencia numérica separada por comas: ")
        inicio = int(input("Indique la posición de comienzo de extracción de elementos: "))
        fin = int(input("Indique la posición de fin de extracción de elementos: "))

        resultado = lista.segmento(inicio, fin, numeros)

        print("\nLista de elementos extraídos entre las posiciones {} y {}: {}".format(inicio, fin, resultado))

    # n primeros y n ultimos
    elif (entrada == 9):

        numeros = input("Ingrese una secuencia numérica separada por comas: ")
        cantidad = int(input("Indique los N primeros y últimos números que formarán parte de la nueva lista: "))

        resultado = lista.extremos(cantidad, numeros)

        print("\nLista de los {} elementos extraídos del principio y del final: {}".format(cantidad, resultado))

    # triangulo de mayor area
    elif (entrada == 10):

        triangulo1 = input("Ingrese las la base y la altura (separada por comas) del primer triángulo: ")
        triangulo2 = input("Ingrese las la base y la altura (separada por comas) del primer triángulo: ")

        resultado = lista.extremos(cantidad, numeros)

        print("\nLista de los {} elementos extraídos del principio y del final: {}".format(cantidad, resultado))

    menu.mostrarMenu()
    entrada = opcion.opcionValida()

print("\nSaliendo del programa...\n¡Hasta otra! \n")
