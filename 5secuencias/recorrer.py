
# recorre la lista pasada por parámetro y la devuelve como cadena

def recorreLista(lista):

    resultado = ""

    # comienza desde el elemento en la primera posicion (0), hasta
    # el ultimo elemento (obtenido del largo de la lista -1, automaticamente
    # excluido del rango)
    for i in range(len(lista)):
        resultado += str(lista[i]) + " " # formateo de salida
    resultado += "\n"
    
    return resultado