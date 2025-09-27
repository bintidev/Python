'''Escribe un programa que recoja la hora del día y devuelva un saludo, según
las siguientes reglas:
INTERVALO DE HORAS SALUDO
[7,12) Buenos días
[12, 20) Buenas tardes
En otro caso Buenas noches'''

def saludo(h,m):
    s = ""

    '''para que se muestre el mensaje "buenas noches" al introducir horas
    de la madrugada, teniendo en cuenta, a la vez, los minutos, es necesario
    especificar el rango de hora.'''
    if ((h >= 7 and h < 12) and (m >= 0 and m <= 59)):
        s = "Buenos días"
    elif ((h >= 12 and h < 20) and (m >= 0 and m <= 59)):
        s = "Buenas tardes"
    else:
        s = "Buenas noches"

    return s

hora = int(input("Introduce la hora: "))
minutos = int(input("Especifica los minutos: "))

print (saludo(hora,minutos))
