
import cmath, numerico

'''Resolver una ecuación de segundo grado. Se deben leer los tres coeficientes
de una ecuación de segundo grado y encontrar la solución. Si la tiene, porque hay
ecuaciones que no tienen solución.'''

def resolver(a, b, c):

    if (a == 0) and (b == 0):

        resultado1 = "Ecuación no válida"
            
    elif (a == 0):

        resultado1 = -c / b

    elif (b == 0):

        resultado1 = round(cmath.sqrt(-c / a).real, 2)
        resultado2 = -round(cmath.sqrt(-c / a).real, 2)

    elif (c == 0):

        resultado1 = 0
        resultado2 = round(-b / a, 2)

    else:

        discriminante = cmath.sqrt(b ** 2 - (4 * a * c))
        resultado1 = round(( -b + discriminante ).real / (2 * a), 2)
        resultado2 = round(( -b - discriminante ).real / (2 * a), 2)


    if (resultado2 is None or resultado2 == 0):

        resultado = "Único resultado posible: {}".format(resultado1)

    else:

        resultado = "Resultado 1: {} - Resultado 2: {}".format(resultado1, resultado2)

    return resultado