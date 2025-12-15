
'''2. El usuario introducirá la opción que debe ejecutar. Para ello, introducirá una letra
(ya sea minúscula o mayúscula) de la operación a realizar. En caso de introducir
una letra incorrecta se mostrará un mensaje de error'''

def opcionValida():

    # no distingue entre mayusculas y minusculas
    op = input("\nOpcion: ").lower()
    validas = set("abcdefgh")

    while (op not in validas):

        op = input('Error. Ingrese una opción válida: ').lower()

    return op