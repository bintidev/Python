
# Adivinar un número. Se debe averiguar un número aleatorio entre 1 y 100. El
# usuario debe adivinarlo. En cada intento el programa nos debe dar una pista (es
#  mayor, o es menor). El proceso continuará hasta que el usuario acierte el
# resultado
def adivinarNumero(intento, numero):
    pista = ""

    if (numero > intento):
        pista = "El número que buscas es mayor ;D"
    else:
        pista = "El número que buscas es menor :P"
    
    return pista