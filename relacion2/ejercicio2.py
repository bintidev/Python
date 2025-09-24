
'''Escribe un programa que recoja un número por teclado y muestre el día de la
semana que es (1 = Lunes, 2 = Martes...). En caso de introducir un número
incorrecto, mostrará el mensaje “Día de la semana incorrecto”.'''

def diaSemana(n):
    d = ""

    if n < 8:
        d = dias[n-1]
    else:
        d = "Día de la semana incorrecto"

    return d

dias = ("Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo")

n = int(input("Introduce un número a partir del cual se mostrará el día de la semana al que corresponde: "))

print (diaSemana(n))