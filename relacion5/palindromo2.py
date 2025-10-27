
'''4. Escribe un programa que lea dos textos y compruebe si una es palíndromo de 
la otra. El programa debe preguntar si se desea comprobar teniendo en cuenta 
mayúsculas/minúsculas o no'''

def palindromoDeOtro(txt):

    palindromoOtro = True

    texto1 = txt[0]
    texto2 = txt[1]

    texto1Inverso = txt[0][::-1]
    texto2Inverso = txt[1][::-1]
    print ("GMP El texto1  es"+texto1)
    print ("GMP El texto2  es"+texto2)
    print("Texto1: {} - Texto2: {}\n Texto1 Inverso: {} - Texto2 Inverso: {}".format(texto1,texto2,texto1Inverso,texto2Inverso))
    
    if (texto1 != texto2 or texto1Inverso != texto2Inverso):
        palindromoOtro = False

    else:
        palindromoOtro = True
    
    return palindromoOtro