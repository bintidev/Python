
import recorrer

'''1. Escribe un programa que recoja números de teclado hasta que se introduce un 
cero. Luego debe mostrar la secuencia de números de tres modos: 
a. En el orden en que se introdujeron. 
b. En orden creciente. 
c. En orden decreciente. 

Ejemplo: si se introduce 4 3 5 2 0, debe mostrarse: 
- 4 3 5 2 
- 2 3 4 5 
- 5 4 3 2'''

def mostrarSecuencia(nums):

    # copias de la lista pasada por parametro
    # [:] -> copia todos los elementos del principio al final
    # de la lista, con un salto de, automaticamente, 1
    creciente = nums[:]
    decreciente = nums[:]

    secuencia = "\n"

    creciente.sort()
    decreciente.sort(reverse = True)
    
    secuencia += recorrer.recorreLista(nums)
    secuencia += recorrer.recorreLista(creciente)
    secuencia += recorrer.recorreLista(decreciente)

    return secuencia