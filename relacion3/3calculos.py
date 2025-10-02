
'''Escribe un programa que recoja números por teclado hasta que se introduzca
el valor cero. A continuación, debe mostrar el número de valores introducidos,
el valor mínimo introducido, el máximo, la suma de todos ellos y su media
aritmética (todos los cálculos sin contar el cero)'''

num = int(input("Introduce un número (o pulsa 0 para salir): "))

contador = 0 # contador de numeros introducidos
max = 0
min = 0
suma = 0

while (num != 0):

    # se empieza primero con las operaciones en caso de que
    # inicialmente el numero introducido no sea cero
    contador += 1 # aumenta en 1 por cada numero introducido distinto de cero

    if (num > max):
        max = num
    elif (num < min):
        min = num

    suma += num # acumula la suma de los numeros introducidos por el usuario

    num = int(input("Introduce otro número (o pulsa 0 para salir): "))

media = suma / contador # calculo de la media a partir de la suma y cantidad de valores introducidos

print ("Número de valores introducidos: {} - Mínimo: {} - Máximo: {} \nSuma: {} - Media: {}".format(contador, min, max, suma, media))
    

    