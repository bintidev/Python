
# Comprueba que la opcion introducida es valida
def opcionValida():

    op = input("\nIngrese una opción: ")
    # no distingue entre mayusculas y minusculas
    validas = set("abcdef")

    for i in validas:

        while op not in validas:

            op = input("Error. Introduce una opción válida: ")

    return op