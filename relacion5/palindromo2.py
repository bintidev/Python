
import palindromo

'''4. Escribe un programa que lea dos textos y compruebe si una es palíndromo de 
la otra. El programa debe preguntar si se desea comprobar teniendo en cuenta 
mayúsculas/minúsculas o no'''

def palindromoDeOtro(txt1, txt2):

    palindromoOtro = True

    if (palindromo.esPalindromo(txt1) != palindromo.esPalindromo(txt2)):
        palindromoOtro = False
    
    return palindromoOtro