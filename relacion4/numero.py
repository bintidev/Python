
# 4. Si la entrada de datos es númerica, hay que asegurarse de que el valor introducido
# es un número. Procura que el programa sea robusto. Es decir, que se controlen
# los errores en el programa
# def esNumerico (n):
def esNumero (n):
    esNum = True

    if ( n.is_integer() != int):
        esNum = False

    return esNum