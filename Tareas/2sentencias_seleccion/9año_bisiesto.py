'''Escribe un programa que recoja un año e indique si se trata de un año bisiesto
o no. Un año es bisiesto si cumple estas condiciones:
a. El año es divisible por 4.
b. Si además el año es divisible por 100, debe ser también divisible por
400.
Ejemplos:
- 1992 es bisiesto (cumple el caso a. Al no ser divisible por 100 no aplica el
caso b)
- 2023 no es bisiesto (no cumple ningún caso)
- 2000 es bisiesto (cumple los casos a y b)
- 1900 no es bisiesto (cumple el caso a, pero no el b porque es divisible por
100 y no por 400)'''

def esBisiesto(d):
    b = False

    if (d % 4 == 0): # cualquier año es bisiesto si es divisible por 4
        b = True

        if (d % 100 == 0): # los siglos son bisiestos si son divisibles por 100

            if (d % 400 == 0): # y también por 400
                b = True
            else:
                b = False # si no cumplen todas las condiciones, salen por esta rama
    else:
        b = False
    
    return b

anyo = int(input("Introduce un año e indicaré si es o no bisiesto: "))

anyobisiesto = "Es un año bisiesto" if esBisiesto(anyo) else "No es un año bisiesto"

print (anyobisiesto)