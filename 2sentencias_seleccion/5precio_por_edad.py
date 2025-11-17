'''Escribe un programa que calcule el precio de entrada a un museo a partir de
la edad del visitante, teniendo en cuenta que:
a. Menores de 5 años entran gratis.
b. Niños entre 5 años y 18 (sin llegar a los 18) pagan 3€.
c. Mayores de edad hasta los 65 (sin llegar a los 65) pagan 6€.
d. Jubilados entran gratis.'''

# calculo del precio en base a la edad
def precioPorEdad(e):
    p = 0

    if(e) < 5:
        p = 0
    elif (e < 18):
        p = 3
    elif(e < 65):
        p = 6
    else:
        p = 0
    
    return p

edad = int(input("Introduce tu edad: "))

print ("El importe a pagar por su entrada es de {}€".format(precioPorEdad(edad)))