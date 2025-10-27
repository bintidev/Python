
# devuelve una lista con los textos pasados por parametro
# en mayuscula si se ignora la distincion o tal como estaba
# si se quiere hacer la distincion
def distincionMinMay(txt1, txt2, r):

    if (r.lower() == "n"):
        # elimina los espacios
        return [txt1.lower().replace(" ", ""), txt2.lower().replace(" ", "")]
    
    else:
        return [txt1.replace(" ", ""), txt2.replace(" ", "")]