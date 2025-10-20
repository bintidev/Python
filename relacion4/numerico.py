import math

'''4. Si la entrada de datos es númerica, hay que asegurarse de que el valor introducido
es un número. Procura que el programa sea robusto. Es decir, que se controlen
los errores en el programa'''

def esNumero (mensaje):

    error = False

    while False:
        try:
            num = int(input(mensaje))
            error = False
            return num
        except:
            num = int(input("Error. Introduce valor numérico: "))
