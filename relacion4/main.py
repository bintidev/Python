
import math, cmath
import impar, aleatorio, menu, opcion, numerico
import rombo, adivinar, ecuacion, tabla, factorial

menu.mostrarMenu()
opcionUsuario = opcion.opcionValida()

# 3. Si se ha indicado una opción correcta, se ejecuta según estas instrucciones que
# se indican a continuación. Una vez finalizada la opción se espera a que se pulse
# una tecla para continuar

while (opcionUsuario != 'h'):

    # mostrar rombo
    if (opcionUsuario == 'a'):

        base = numerico.esNumero("\nIngrese un número impar para el rombo: ")
        rombo.mostrarRombo(base)

        menu.mostrarMenu()
        opcionUsuario = opcion.opcionValida()

    # adivinar número
    elif (opcionUsuario == 'b'):
        
        intento = input("\nAdivina el número en el que estoy pensando del 1 al 100: ")

        copiaIntento = numerico.esNumero(intento)
        print(adivinar.adivinarNumero(copiaIntento))
        
        menu.mostrarMenu()
        opcionUsuario = opcion.opcionValida()

    # resolver ecuacion de segundo grado
    elif (opcionUsuario == 'c'):
        
        a = input("\nIngrese un valor para a: ")
        b = input("Ingrese un valor para b: ")
        c = input("Ingrese un valor para c: ")

        copiaA = numerico.esNumero(a)
        copiaB = numerico.esNumero(b)
        copiaC = numerico.esNumero(c)
        print(ecuacion.resolver(a, b, c))
        
        menu.mostrarMenu()
        opcionUsuario = opcion.opcionValida()

    # tabla de números
    elif (opcionUsuario == 'd'):

        filas = input("\nIngrese un número de filas: ")
        columnas = input("Ingrese un número de columnas: ")

        copiaFilas = numerico.esNumero(filas)
        copiaColumnas = numerico.esNumero(columnas)
        tabla.tablaDenumeros(filas, columnas)

        menu.mostrarMenu()
        opcionUsuario = opcion.opcionValida()

    # factorial de un número
    elif (opcionUsuario == 'e'):

        numero = input("Ingrese un número:")
        print ("Factorial del número {}: {}".format(numero, factorial.factorialNumero(numero)))

        menu.mostrarMenu()
        opcionUsuario = opcion.opcionValida()

print ("\nHas salido del programa")

