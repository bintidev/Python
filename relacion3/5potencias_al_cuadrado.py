
'''Escribe un programa que recoja un número por teclado y muestre los primeros
cuadrados hasta llegar al número introducido. Por ejemplo, si se ha introducido
el valor 5, se debe mostrar:
1 4 9 16 25'''

n = int(input("Introduce un número: "))

for i in range(1, n): # rango entre 1 y n (ambos incluidos)
    print (i ** 2, end=" ")