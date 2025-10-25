
# funciones definidas en ficheros aparte
# importación como si fueran clases
import menu, opcion, numerico
import rombo, adivinar, ecuacion, tabla, factorial, fibonacci, tablaMultiplicar

menu.mostrarMenu() # muestra el menu de operaciones
opcionUsuario = opcion.opcionValida() # validacion de opcion introducida

# 3. Si se ha indicado una opción correcta, se ejecuta según estas instrucciones que
# se indican a continuación. Una vez finalizada la opción se espera a que se pulse
# una tecla para continuar

while (opcionUsuario != 'h'):

    # mostrar rombo
    if (opcionUsuario == 'a'):

        # valida entrada numerica proporcionando el mensaje a mostrar
        base = numerico.esNumero("\nIngrese un número impar para el rombo: ")
        print(rombo.mostrarRombo(base))

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

        print(tabla.tablaDenumeros(filas, columnas))

    # factorial de un número
    elif (opcionUsuario == 'e'):

        numero = numerico.esNumero("Ingrese un número: ")
        print ("Factorial del número {}: {}".format(numero, factorial.factorialNumero(numero)))

    # secuencia fibonacci
    elif (opcionUsuario == 'f'):

        posicion = numerico.esNumero("Ingrese una posición: ")
        print ("Número obtenido mediante cálculo Fibonacci: {}".format(fibonacci.secuenciaFib(posicion)))

    # tablas de multiplicar
    elif (opcionUsuario == 'g'):

        numero = numerico.esNumero("Ingrese un número: ")
        print(tablaMultiplicar.mostrarTablas(numero))

    menu.mostrarMenu()
    opcionUsuario = opcion.opcionValida()

print ("\nHas salido del programa \nHasta luego! <3 \n")

