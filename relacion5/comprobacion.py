
# devuelve una lista con los textos pasados por parametro
# en mayuscula si se ignora la distincion o tal como estaba
# si se quiere hacer la distincion
def distincionMinMay(txt1, txt2, r):

    if (r.lower() == "n"):
        return [txt1.upper(), txt2.upper()]
    
    else:
        return [txt1, txt2]