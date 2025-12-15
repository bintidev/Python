
'''4. Escribe un programa que lea dos textos y compruebe si una es palíndromo de 
la otra. El programa debe preguntar si se desea comprobar teniendo en cuenta 
mayúsculas/minúsculas o no'''

def palindromoDeOtro(textos):

    palindromoOtro = False

    if (textos[0] == textos[1]):

        if (textos[0][::-1] == textos[1][::-1]):
            palindromoOtro = True

    else:
        palindromoOtro = False
    
    return palindromoOtro