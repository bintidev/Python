
'''Escribe un programa que recoja una cadena de texto por teclado y una letra a
buscar. Luego debe buscar dicha letra por la cadena y al finalizar debe indicar
el número de veces que se repite la letra en el texto.'''

txt = input("Introduce una cadena de texto: ").lower()
letra = input("Introduzca el caracter que desea buscar dentro de la cadena: ").lower()

buscador = 0 # recorre la cadena
coincidencias = 0 # veces que se encuentra el caracter dentro de la cadena

# ya que el buscador se inicializa a 0, los índices
# de posición funcionan como en los arrays y no debe pasar
# del largo de la cadena (0 hasta len(cadena) será igual a len(cadena)) 
while (buscador < len(txt)):
    
     # por cada caracter que encuentre el buscador dentro de la cadena y coincida con la letra a buscar especificada
    if (txt[buscador] == letra):
        coincidencias += 1
    buscador += 1 # lee lel siguiente caracter en la cadena

if (coincidencias == 0):
    print ("La letra {} no se repite en el texto".format(letra))
else:
    print ("La letra {} se repite {} veces en el texto".format(letra, coincidencias))