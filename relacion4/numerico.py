
'''4. Si la entrada de datos es númerica, hay que asegurarse de que el valor introducido
es un número. Procura que el programa sea robusto. Es decir, que se controlen
los errores en el programa'''

# devuelve mensaje de error y solicita datos o
# devuelve numero dependiendo de si la
# entrada es o no numerica
def esNumero (mensaje):

    while True: # se ejecuta mientras se pase un parámetro mensaje
        try:
            # muestra el mensaje proporcionado, solicitando un número
            # si la entrada inicial no era numérica
            num = int(input(mensaje))
            return num
        except:
            print("Error. Introduce un valor numérico válido") # mensaje de error
