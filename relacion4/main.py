
import math, random, cmath
import impar, opcionValida, rombo, adivinar, numerico

# 1. Al arrancar debe mostrar un menú de opciones como el siguiente
menu = ["MENÚ DE OPCIONES",
        "a) Mostrar un rombo",
        "b) Adivinar un número",
        "c) Resolver una ecuación de segundo grado",
        "d) Tabla de números",
        "e) Cálculo del número factorial de un número",
        "f) Cálculo de un número de la sucesión de Fibonacci",
        "g) Tabla de multiplicar",
        "h) Salir"]

for i in range(len(menu)):
     print(menu[i], end="\n")

opcion = input("Opcion: ").lower()

# 3. Si se ha indicado una opción correcta, se ejecuta según estas instrucciones que
# se indican a continuación. Una vez finalizada la opción se espera a que se pulse
# una tecla para continuar
while (opcionValida.opcionValida(opcion)):

    # mostrar rombo
    if (opcion == 'a'):
        base = int(input("Ingrese un número impar para el rombo: "))

        while (math.isnan(base)):
            base = int(input("Error. Valor no númerico. Inténtelo de nevo: "))

        while (impar.esImpar(base) == False):
            base = int(input("Error. La base debe ser impar. Inténtelo de nuevo: "))

        rombo.mostrarRombo(base)

        opcion = input("Escoja otra opción: ")
    
    # adivinar número
    elif (opcion == 'b'):
        aleatorio = random.randint(1, 100)
        intento = int(input("Adivina el número en el que estoy pensando del 1 al 100: "))

        while (math.isnan(intento)):
            intento = int(input("Error. Valor no númerico. Ingrese un número del 1 al 100: "))

        while (intento != aleatorio):
                print (adivinar.adivinarNumero(intento, aleatorio))
                intento = int(input("Vuelve a intentarlo: "))
        
        print ("Has adivinado. Yupiii !!!!")
        
        opcion = input("Escoja otra opción: ")

    # resolver ecuacion de segundo grado
    elif (opcion == 'c'):
        a = int(input("Ingrese un valor para a: "))
        b = int(input("Ingrese un valor para b: "))
        c = int(input("Ingrese un valor para c: "))

        if (a == 0) and (b == 0):

            resultado1 = "Ecuación no válida"
             
        elif (a == 0):

            resultado1 = -c / b

        elif (b == 0):

            resultado1 = round(cmath.sqrt(-c / a).real, 2)
            resultado2 = -round(cmath.sqrt(-c / a).real, 2)

        elif (c == 0):

            resultado1 = 0
            resultado2 = round(-b / a, 2)

        else:

            discriminante = cmath.sqrt(b ** 2 - (4 * a * c))
            resultado1 = round(( -b + discriminante ).real / (2 * a), 2)
            resultado2 = round(( -b - discriminante ).real / (2 * a), 2)
        
        if (resultado2 is None or resultado2 == 0):

            print ("Único resultado posible: {}".format(resultado1))

        else:

            print ("Resultado 1: {} - Resultado 2: {}".format(resultado1, resultado2))
        
        opcion = input("Escoja otra opción: ")

