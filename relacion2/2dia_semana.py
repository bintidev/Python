
'''Escribe un programa que recoja un número por teclado y muestre el día de la
semana que es (1 = Lunes, 2 = Martes...). En caso de introducir un número
incorrecto, mostrará el mensaje “Día de la semana incorrecto”.'''

def diaSemana(n):
    d = ""

    if n < 8: # validadndo que el día introducido sea menor que el número de días existente en el array
        d = dias[n-1] # restarle 1 porque las posiciones del array van del 0 al 6
    else:
        d = "Día de la semana incorrecto"

    return d

dias = ("Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo")

n = int(input("Introduce un número a partir del cual se mostrará el día de la semana al que corresponde: "))

print (diaSemana(n))