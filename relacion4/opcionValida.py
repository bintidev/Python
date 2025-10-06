
# 2. El usuario introducirá la opción que debe ejecutar. Para ello, introducirá una letra
# (ya sea minúscula o mayúscula) de la operación a realizar. En caso de introducir
# una letra incorrecta se mostrará un mensaje de error
def opcionValida(opcion):
    op = opcion.lower
    valida = True

    if (op != 'a' and op != 'b' and op != 'c' and op != 'd' and op != 'e'
        and op != 'f' and op != 'g' and op != 'h'):

        valida = False

    return valida