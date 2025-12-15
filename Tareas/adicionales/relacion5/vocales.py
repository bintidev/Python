
'''1. Definir una función que, al recibir una cadena de texto, cuente cuántas vocales hay y 
devuelva dicho valor.'''

def contar(cadena):

    vocales = set('aeiouAEIOU')
    cantVocales = 0

    for i in range(len(cadena)):

        if cadena[i] in vocales:
            cantVocales += 1

    return cantVocales