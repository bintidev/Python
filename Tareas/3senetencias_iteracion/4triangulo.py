
'''Escribe un programa que recoja un número y muestre un triángulo. Por
ejemplo, si se ha introducido el valor 5, se debe mostrar:
*
**
***
****
*****'''

n = int(input("Introduce un número: "))

for i in range(1, n + 1): # rango [1,n] **NOTA: n+1 para que incluya el limite (valor de n) al rango
    print ("*" * i)