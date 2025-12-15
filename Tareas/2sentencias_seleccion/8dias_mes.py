'''Escribe un programa que recoja un mes del año (en número) y devuelva el
número de días que tiene el mes. En caso de indicar un mes incorrecto deberá
mostrar un mensaje de error.'''

# verificación de mes válido
def diasMes(m):
    dm = 0

    if (m == 1 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12):
        dm = 31
    elif (m == 2):
        dm = 28
    elif (m == 4 or m == 6 or m == 8 or m == 11):
        dm = 30
    else:
        dm = 0

    return dm

mes = int(input("Introduce un mes en formato numérico: "))

if (diasMes(mes) != 0):
    print ("El mes tiene {} días".format(diasMes(mes)))
else:
    print ("Error. Mes inexistente.")