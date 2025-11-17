
# Escribe un programa que recoja un texto y escriba cada letra del texto en una línea distinta.

txt = input("Introduce un texto: ")

# la operacion se repite hasta el final de la cadena (ultimo caracter incluido) 
for i in range(len(txt)):
    print (txt[i])
    i += 1 # aumenta el iterador en 1 por cada vuelta