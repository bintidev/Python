
import recorrer

# muestra una secuencia de la lista pasada por parametro

def mostrarSecuencia(lista):

    # lista[:] crea una copia de la lista pasada por parametros y la
    # almacena en las variables indicadas
    ascendente = lista[:]
    descendente = lista[:]

    secuencia = "\n"

    ascendente.sort() # automaticamente orden alfabeticamente
    descendente.sort(reverse = True)

    secuencia += recorrer.recorreLista(lista)
    secuencia += recorrer.recorreLista(ascendente)
    secuencia += recorrer.recorreLista(descendente)

    return secuencia