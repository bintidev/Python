import math

'''4. Si la entrada de datos es númerica, hay que asegurarse de que el valor introducido
es un número. Procura que el programa sea robusto. Es decir, que se controlen
los errores en el programa'''

def esNumero (mensaje):

    while True:
        try:
            num = int(input(mensaje))
            return num
        except:
            print("Error. Introduce valor numérico válido")
