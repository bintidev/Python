
##################################################################################

# Al arrancar debe mostrar un menú de opciones como el siguiente

# devuelve el menus de operaciones
def mostrarMenu():

    menu = [    "\n---------------------",
                "MENÚ DE OPCIONES",
                "---------------------",
                "a) Reemplazar vocales de una frase",
                "b) Mensaje cuando el numero introducido no sea mayor que el primero",
                "c) Encontrar la primera palabra más larga",
                "d) Mostrar rectángulo con números impares entre 0 y 100",
                "e) Contar la aparición de cada carácter en una palabra.\nMostrar diccionario y el carácter con más apariciones.",
                "f) Salir",
            ]

    for i in range(len(menu)):
        print(menu[i], end = "\n")

# Comprueba que la opcion introducida es valida
def opcionValida():

    op = input("\nIngrese una opción: ")
    # no distingue entre mayusculas y minusculas
    validas = set("abcdef")

    for i in validas:

        while op not in validas:

            op = input("Error. Introduce una opción válida: ")

    return op

# comprueba que un dato introducido sea numerico
def esNumero (mensaje):

    while True: # se ejecuta mientras se pase un parámetro mensaje
        try:
            # muestra el mensaje proporcionado, solicitando un número
            # si la entrada inicial no era numérica
            num = int(input(mensaje))
            return num
        except:
            print("\nError. Introduce un valor numérico válido\n") # mensaje de error


###############################################################################

'''a)  La opción permite reemplazar vocales de una frase por el carácter “*”. La 
frase se introduce por teclado 
.  Ejemplo: "Hola Mundo" 
.  Devuelve: "H*l* M*nd*'''
def reemplazarVocal(cadena):

    vocalA = cadena.replace('a', '*')
    vocalE = vocalA.replace('e', '*')
    vocalI = vocalE.replace('i', '*')
    vocalO = vocalI.replace('o', '*')
    vocalU = vocalO.replace('u', '*')

    return vocalU


'''b)  En esta opción el programa preguntará  cuántos números se van a 
introducir, pide esos números, y muestre un mensaje cada vez que un 
número no sea mayor que el anterior.'''
def mayorAnterior(nums):

    msg = ""

    for i in range(len(nums)):

            if nums[i - 1] > nums[i]:
                msg = f"El número {nums[i]} no es mayor que el número {nums[i - 1]}\n"

            else:
                msg = ''

    return msg


'''c)  Dada una frase, encuentra primera palabra más larga dentro de esa 
frase. 
Ejemplo: "La programación en Python es increíble" 
Devuelve: "programación"'''
def palabraMasLarga(txt):

    arrCadena = txt.split(' ')
    masLarga = ''

    for i in range(len(arrCadena)):
        if len(arrCadena[i]) > len(arrCadena[i - 1]):
            masLarga = arrCadena[i]

    return masLarga


'''d) Mostrar los números impares entre 0 y 100 en un formato rectangular   
eligiendo el número de filas y columnas introducidas por teclado: 
Aquí tienes un ejemplo donde mostramos los números impares en un 
rectángulo de 5 filas y 4 columnas: 
99      97      95      93 
91      89      87      85 
83      81      79      77 
75      73      71      69 
67     65      63      61'''
def tablaDeValores(f, c):

    impares = []

    for i in range(0, 100):

        if i % 2 != 0:
            impares.append(i)

    contador = len(impares) - 1

    for fila in range(f):

        for columna in range(c):

            print(f"{impares[contador]}", end="  ")
            contador -= 1

        print()


'''e)Contar la aparición de cada carácter dentro de una palabra. Utiliza la 
estructura de datos diccionarios. Muestra el diccionario ordenado ignorando 
mayúsculas y minúsculas y muestra además la letra o letras que más se 
repitan. 
Ejemplo: "mississippi" 
Devuelve: m: 1  
        i: 4  
        s: 4  
        p: 2'''
def masRepetida(palabra):

    letras = {}

    for i in range(len(palabra)):
        letras[palabra[i].lower()] = 0

    for i in range(len(palabra)):

        if palabra[i].lower() in letras.keys():
            letras[palabra[i].lower()] += 1


    for l, oc in letras.items():
        print(f"{l}: {oc}\n")


################################################################################


mostrarMenu()
entrada = opcionValida()

while (entrada != 'f'):

    # HECHO (no es la mejor manera)
    if (entrada == 'a'):

        texto = input("Ingrese una cadena de la que reemplazar vocales con '*': ")

        print(f"Resultado del reemplazo: {reemplazarVocal(texto)}")

    # HECHO
    elif (entrada == 'b'):

        numeros = []
        cantidad = esNumero("Cantidad de números que va a introducir: ")

        for i in range(1, cantidad + 1):
            num = esNumero("Ingrese un número: ")
            numeros.append(num)
            print(mayorAnterior(numeros))

    # HECHO
    elif (entrada == 'c'):

        texto = input("Ingrese un texto: ")

        print(f"La palabra más larga en la cadena es {palabraMasLarga(texto)}")

    # HECHO
    elif (entrada == 'd'):

        filas = esNumero("Ingrese un número de filas: ")
        columnas = esNumero("Ingrese un número de columnas: ")

        tablaDeValores(filas, columnas)

    # HECHO
    elif (entrada == 'e'):

        texto = input("Ingrese texto: ")
        masRepetida(texto)

    mostrarMenu()
    entrada = opcionValida()

print("\nPrograma terminado. Bye bye! \n")
