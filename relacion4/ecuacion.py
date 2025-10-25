
import cmath

'''Resolver una ecuación de segundo grado. Se deben leer los tres coeficientes
de una ecuación de segundo grado y encontrar la solución. Si la tiene, porque hay
ecuaciones que no tienen solución.'''

# uso de cmath puesto que soporta numero complejos
# (resultados negativos de raices, en este caso)

def resolver(a, b, c):

    if (a == 0) and (b == 0):

        resultado1 = "Ecuación no válida"
        resultado2 = None # se declara resultado2 como no definida
            
    elif (a == 0):

        resultado1 = -c / b
        resultado2 = None

    elif (b == 0):

        # redondeo a 2 decimales tras la coma
        # extraccion de la parte real del resultado para aplicar la funcion round
        resultado1 = round(cmath.sqrt(-c / a).real, 2)
        resultado2 = -round(cmath.sqrt(-c / a).real, 2)

    elif (c == 0):

        resultado1 = 0
        resultado2 = round(-b / a, 2)

    else:

        discriminante = cmath.sqrt(b ** 2 - (4 * a * c))
        resultado1 = round(( -b + discriminante ).real / (2 * a), 2)
        resultado2 = round(( -b - discriminante ).real / (2 * a), 2)


    if (resultado2 is None):

        resultado = "Único resultado posible: {}".format(resultado1)

    else:

        resultado = "Resultado 1: {} - Resultado 2: {}".format(resultado1, resultado2)

    return resultado