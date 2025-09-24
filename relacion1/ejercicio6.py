
'''Escribe un programa que recoja las notas de las tres evaluaciones de un
alumno. A continuación debe calcular y mostrar la nota final, teniendo en
cuenta que la primera evaluación cuenta un 20% de la nota final, la segunda
evaluación un 35% y la tercera evaluación un 45%.'''

# recogida de información
n = 0
nota = 0
notaF = 0

# lista de porcentajes de ponderacion
porcentajePorEval = [25, 35, 45]

for i in range(3):
    sum = 0
    nota = int(input("Introduce la nota de la evaluación: "))
    notaF += nota*(porcentajePorEval[n]/100) # por cada vuelta del bucle se avanza 1 posición
                                            # en la lectura de la lista, para usarla con su nota
                                            # correspondiente
    n += 1

print ("Tu nota es un",notaF)
