
import recorrer

'''2. Repite el ejercicio anterior, pero ahora lo que se leen son textos. La condición 
de finalización será la cadena vacía.'''

def mostrarSecuencia(txt):

    ascendente = txt[:]
    descendente = txt[:]

    secuencia = "\n"

    ascendente.sort() # automaticamente orden alfabeticamente
    descendente.sort(reverse = True)

    secuencia += recorrer.recorreLista(txt)
    secuencia += recorrer.recorreLista(ascendente)
    secuencia += recorrer.recorreLista(descendente)

    return secuencia