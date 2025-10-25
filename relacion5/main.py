
import menu, opcion, numerico
import secuencia

menu.mostrarMenu()
entrada = opcion.opcionValida()

while (entrada != 5):

    # secuencia de numeros
    if (entrada == 1):

        secuenciaNumeros = []
        numero = numerico.esNumero("Ingrese un número (o pulse 0 para salir): ")

        while (numero != 0):

            secuenciaNumeros.append(numero)
            numero = numerico.esNumero("Ingrese otro número (o pulse 0 para salir): ")

        print(secuencia.mostrarSecuencia(secuenciaNumeros))

    # secuencia de cadenas
    elif (entrada == 2):

        secuenciaCadenas = []
        cadena = input("Ingrese una cadena de texto (o déjela vacía para salir): ")

        while (cadena != ""):

            secuenciaCadenas.append(cadena)
            cadena = input("Ingrese otra cadena de texto (o déjela vacía para salir): ").lower()

        print(secuencia.mostrarSecuencia(secuenciaCadenas))

    menu.mostrarMenu()
    entrada = opcion.opcionValida()

print("\nPrograma terminado. Bye bye! \n")
