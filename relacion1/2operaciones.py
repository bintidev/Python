
'''Escribe un programa que recoja dos números enteros por teclado y muestre
los siguientes resultados: suma, resta, multiplicación, división real, división
entera, resto de la división entera y potencia.'''

n1 = int(input("Introduce primer entero: "))
n2 = int(input("Introduce segundo entero: "))

# Operaciones
suma = n1+n2
resta =  n1-n2
multiplicacion = n1*n2
division = n1/n2
divisionE = n1//n2 # división entera
resto = n1%n2
potencia = n1**n2

# Impresión por pantalla
print ("\nRESULTADOS")
print ("===========================================================")

print("Resultado de la suma:", suma)
print("Resultado de la resta:", resta)
print("Resultado de la multiplicación:", multiplicacion)
print("Resultado de la division real:", division)
print("Resultado de la division entera:", divisionE)
print("Resultado del resto de la división entera:", resto)
print("Resultado de la potencia:", potencia)