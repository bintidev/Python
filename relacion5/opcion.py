
import numerico

'''2. El usuario introducirá la opción que debe ejecutar. Para ello, introducirá una letra
(ya sea minúscula o mayúscula) de la operación a realizar. En caso de introducir
una letra incorrecta se mostrará un mensaje de error'''

def opcionValida():

    # no distingue entre mayusculas y minusculas
    op = numerico.esNumero("\nOpcion: ")
    validas = (1,2,3,4,5)

    for i in validas:

        while op not in validas:

            op = numerico.esNumero("Error. Introduce una opción válida: ")

    return op