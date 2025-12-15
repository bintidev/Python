
# Escribe un programa que recoja un texto y lo muestre cinco veces
# consecutivas en la misma línea.

txt = str(input("Escribe un texto cualquiera: "))

for i in range(5):
    print (txt, end=' ')