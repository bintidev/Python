
'''4. Definir la función 
# rota : (int, List[A]) -> List[A] 
# tal que rota(n, xs) es la lista obtenida poniendo los n primeros 
# elementos de xs al final de la lista. Por ejemplo, 
# rota(1, [3, 2, 5, 7]) == [2, 5, 7, 3] 
# rota(2, [3, 2, 5, 7]) == [5, 7, 3, 2] 
# rota(3, [3, 2, 5, 7]) == [7, 3, 2, 5]'''

def rota (n, lista):

    listaRotada = lista.split(',')

    for i in range(0, n):
        # añade al final de la lista los elementos
        # desde la primera posicion, hasta la especificada
        # por el usuario
        listaRotada.append(listaRotada[i])
    
    # borra los elementos que estaban en un principio al inicio de la lista
    del listaRotada[0:n]

    return listaRotada


'''5. Definir la función 
# rango : (List[int]) -> List[int] 
# tal que rango(xs) es la lista formada por el menor y mayor elemento 
# de xs. 
# rango([3, 2, 7, 5]) == [2, 7]'''

def rango(lista):

    listaNueva = lista.split(',')
    # crea una nueva lista con el elemento más pequeño
    # y el más grande de la lista pasada por parámetro
    listaMenorMayor = (min(listaNueva), max(listaNueva))

    return listaMenorMayor


'''6. Definir la función 
# interior : (list[A]) -> list[A] 
# tal que interior(xs) es la lista obtenida eliminando los extremos de 
# la lista xs. Por ejemplo, 
# interior([2, 5, 3, 7, 3]) == [5, 3, 7] '''

def interior (lista):

    exteriorEliminado = lista.split(',')

    # elimina el primer elemento
    del exteriorEliminado[0]
    # elimina el ultimo elemento
    exteriorEliminado.pop()

    return exteriorEliminado



'''7. # Definir la función 
# finales : (int, list[A]) -> list[A] 
# tal que finales(n, xs) es la lista formada por los n finales 
# elementos de xs. Por ejemplo, 
# finales(3, [2, 5, 4, 7, 9, 6]) == [7, 9, 6]'''

def finales(n, lista):

    listaFinales = lista.split(',')
    # obtiene los ultimos 2 elementos de la lista
    listaFinales = listaFinales[-n:]

    return listaFinales


'''8. # Ejercicio 13. Definir la función 
# segmento : (int, int, list[A]) -> list[A] 
# tal que segmento(m, n, xs) es la lista de los elementos de xs 
# comprendidos entre las posiciones m y n. Por ejemplo, 
# segmento(3, 4, [3, 4, 1, 2, 7, 9, 0]) == [1, 2] 
# segmento(3, 5, [3, 4, 1, 2, 7, 9, 0]) == [1, 2, 7] 
# segmento(5, 3, [3, 4, 1, 2, 7, 9, 0]) == []'''

def segmento(ini, fin, lista):

    listaSegmentada = lista.split(',')
    # almacena una lista segmentada con los elementos comprendidos
    # entre los limites dados (ambos incluidos)
    listaSegmentada = listaSegmentada[ini - 1:fin]

    return listaSegmentada


'''9. Definir la función 
# extremos : (int, list[A]) -> list[A] 
# tal que extremos(n, xs) es la lista formada por los n primeros 
# elementos de xs y los n finales elementos de xs. Por ejemplo, 
# extremos(3, [2, 6, 7, 1, 2, 4, 5, 8, 9, 2, 3]) == [2, 6, 7, 9, 2, 3]'''

def extremos(cant, lista):

    listaExtremos = lista.split(',')
    # extrae la cantidad de elementos pasados por parámetro
    #del principio y del final, saltandose los que se encuentran
    # en medio
    listaExtremos = listaExtremos[0::cant + cant]

    return listaExtremos

'''10. Las dimensiones de los rectángulos puede representarse 
# por pares; por ejemplo, (5,3) representa a un rectángulo de base 5 y 
# altura 3. 
# 
# Definir la función 
# mayorRectangulo : (tuple[float, float], tuple[float, float]) 
# -> tuple[float, float] 
# tal que mayorRectangulo(r1, r2) es el rectángulo de mayor área entre 
# r1 y r2. Por ejemplo, 
# mayorRectangulo((4, 6), (3, 7)) == (4, 6) 
# mayorRectangulo((4, 6), (3, 8)) == (4, 6) 
# mayorRectangulo((4, 6), (3, 9)) == (3, 9)'''

def mayorRectangulo (rect1, rect2):

    if ((rect1[0] * rect1[1]) > (rect2[0] * rect2[1])):
        mayor = rect1
    
    else:
        mayor = rect2

    return mayor