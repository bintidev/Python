
'''3. Escribe  un  programa  lea  un  texto  y  determine  si  es  un  palíndromo.  Procura 
crear una función palindromo(s) -> Bool. 

NOTA: una cadena es palíndromo si se lee igual de izquierda a derecha que 
de derecha a izquierda. Por ejemplo, la palabra OSO es un palíndromo.'''

def esPalindromo(txt):

    esPld = True
    # recoge la cadena al revés
    txtInverso = txt[::-1]

    if (txtInverso != txt):
        esPld = False
    
    return esPld