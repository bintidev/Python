
'''2. Definir una función que, al recibir una cadena de texto, cuente cuántas palabras hay y 
devuelva dicho valor.'''

def contar(cadena):

    dividida = cadena.split()
    cantPalabras = 0

    for i in range(len(dividida)):
        cantPalabras += 1

    return cantPalabras