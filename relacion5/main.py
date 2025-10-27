
import menu, opcion, numerico, comprobacion
import secuencia, palindromo, palindromo2

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

    # palindromo
    elif (entrada == 3):

        texto = input("Ingrese texto: ")

        # evitar distincion por mayusculas y minusculas
        # y eliminar espacios antes de pasar el texto a la funcion
        if(palindromo.esPalindromo(texto.lower().replace(" ", ""))):
            print ("{} es un texto palíndromo".format(texto))
        else:
            print ("{} no es un texto palíndromo".format(texto))

    # palindromo de otra
    elif (entrada == 4):

        texto1 = input("Ingrese primera cadena: ")
        texto2 = input("Ingrese segunda cadena: ")

        comprobar = comprobacion.distincionMinMay(texto1, texto2, input("¿Desea distinguir entre mayúsculas/minúsculas? [ S / N ] "))

        
        if(palindromo2.palindromoDeOtro(comprobar)):
            print ("{} si es un texto palíndromo de {}".format(texto1, texto2))
        else:
            print ("{} no es un texto palíndromo de {}".format(texto1, texto2))


    menu.mostrarMenu()
    entrada = opcion.opcionValida()

print("\nPrograma terminado. Bye bye! \n")
