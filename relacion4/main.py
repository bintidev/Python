
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
        base = impar.esImpar(base)
        rombo.mostrarRombo(base)

    # adivinar número
    elif (opcionUsuario == 'b'):
        
        intento = numerico.esNumero("\nAdivina el número en el que estoy pensando del 1 al 100: ")
        print(adivinar.adivinarNumero(intento))
    

    # resolver ecuacion de segundo grado
    elif (opcionUsuario == 'c'):
        
        a = numerico.esNumero("\nIngrese un valor para a: ")
        b = numerico.esNumero("Ingrese un valor para b: ")
        c = numerico.esNumero("Ingrese un valor para c: ")

        print(ecuacion.resolver(a, b, c))
    

    # tabla de números
    elif (opcionUsuario == 'd'):

        filas = numerico.esNumero("\nIngrese un número de filas: ")
        columnas = numerico.esNumero("Ingrese un número de columnas: ")

        tabla.tablaDenumeros(filas, columnas)

    # factorial de un número
    elif (opcionUsuario == 'e'):

        numero = numerico.esNumero("Ingrese un número:")
        print ("Factorial del número {}: {}".format(numero, factorial.factorialNumero(numero)))

    # secuencia fibonacci
    elif (opcionUsuario == 'f'):

        numero = numerico.esNumero("Ingrese un número:")
        #fibonacci =
        print ("Número obtenido mediante cálculo Fibonacci: {}")


    menu.mostrarMenu()
    opcionUsuario = opcion.opcionValida()

print ("\nHas salido del programa")

