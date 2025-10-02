
'''Escribe un programa que recoja un número impar. Debe asegurarse de que
sea impar, en caso de no serlo debe descartarlo y pedirlo de nuevo. Una vez
tenga el número impar debe mostrar una pirámide de asteriscos cuya base es
igual al número introducido. Por ejemplo, si se introduce el valor 7 se debe
mostrar:
*
***
*****
******* <- base de la pirámide (7 asteriscos)'''

base = int(input("Introduce un número impar para la base de la pirámide: "))

while (base % 2 == 0):
    base = int(input("Error. Base inválida. Prueba con otro número: "))

for i in range(1, base + 1, 2): # rango del 1 a base (ambos incluidos) con un aumento de dos en dos (numeros impares)
    
    # (base - i) -> permite saber la cantidad de espacios totales (tanto derecha como izquierda)
    # necesarios para centrar la línea en relación a la base

    # // 2 -> ya que la consola "rellena" el lado derecho, solo necesitamos rellenarlo por la izquierda
    # por tanto, como por ambos lados se rellena la misma cantidad, nos sirve conocer la cantidad de un
    # solo lado (la mitad) 
    espacios = (base - i) // 2
    print (" " * espacios + "*" * i) # imprime los espacios por la izquierda seguido de asteriscos