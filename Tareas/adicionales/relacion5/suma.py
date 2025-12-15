
'''3. Definir una función que devuelva la suma dos números. Utilizar esa función para sumar tres 
números.'''

def sumarDigitos(numeros):

    listaNumeros = numeros.split(',')
    suma = 0

    for i in range(len(listaNumeros)):
        suma += int(listaNumeros[i]) # casting a entero

    return suma