
import random
import impar, opcionValida, rombo, adivinar, numero

# 1. Al arrancar debe mostrar un menú de opciones como el siguiente
menu = ["MENÚ DE OPCIONES",
        "\na) Mostrar un rombo",
        "\nb) Adivinar un número",
        "\nc) Resolver una ecuación de segundo grado",
        "\nd) Tabla de números",
        "\ne) Cálculo del número factorial de un número",
        "\nf) Cálculo de un número de la sucesión de Fibonacci",
        "\ng) Tabla de multiplicar",
        "\nh) Salir"]

for i in menu:
     print(menu[i], end="\n")

opcion = input("Opcion: ")

# 3. Si se ha indicado una opción correcta, se ejecuta según estas instrucciones que
# se indican a continuación. Una vez finalizada la opción se espera a que se pulse
# una tecla para continuar
while (opcionValida.opcionValida(opcion)):

    # mostrar rombo
    if (opcion == 'a'):
        base = int(input("Ingrese un número impar para el rombo: "))

        while (numero.esNumero(base)):
            base = int(input("Error. Valor no númerico. Inténtelo de nevo: "))

        while (impar.esImpar(base) == False):
            base = int(input("Error. La base debe ser impar. Inténtelo de nuevo: "))

            rombo.mostrarRombo(base)

        opcion = input("Escoja otra opción: ")
    
    # adivinar número
    if (opcion == 'b'):
        aleatorio = random.randint(1, 100)
        intento = int(input("Adivina el número en el que estoy pensando: "))

        while (numero.esNumero(intento) == False):
            intento = int(input("Error. Valor no númerico. Inténtelo de nevo: "))

        while (intento != aleatorio):
                adivinar.adivinarNumero(intento, aleatorio)
                intento = int(input("Adivina el número en el que estoy pensando: "))
        
        opcion = input("Escoja otra opción: ")

    # resolver ecuacion de segundo grado
    if (opcion == 'c'):
        a = int(input("Ingrese el número de líneas: "))
        b = int(input("Ingrese el número de columnas: "))
