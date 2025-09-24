'''Escribe un programa que muestre la nota final de un alumno a partir de su
calificación numérica (valor decimal), teniendo en cuenta que:
a. Nota menor de 5 es suspenso.
b. Nota entre 5 y 6 (sin llegar) es suficiente.
c. Nota entre 6 y 7 (sin llegar) es bien.
d. Nota entre 7 y 9 (sin llegar) es notable.
e. Nota entre 9 y 10 (sin llegar) es sobresaliente.
f. Nota igual a 10 es matrícula de honor.
g. Cualquier otro valor numérico fuera de este rango es un error.'''

# cálculo dela nota teniendo en cuenta rangos
def calculoNotaFinal(n):
    nf = 0

    if (n < 5):
        nf = "suspenso"
    elif (n < 6):
        nf = "suficiente"
    elif (n < 7):
        nf = "bien"
    elif (n < 9):
        nf = "notable"
    elif (n < 10):
        nf = "sobresaliente"
    elif (n == 10):
        nf = "matrícula de honor"
    else:
        nf = "Valor numérico fuera de rango. No se puede calcular la nota"
        
    return nf


nota = float(input("Introduce tu calificación: "))

print ("Nota final: {}".format(calculoNotaFinal(nota)))