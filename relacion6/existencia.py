
# Indica si un contacto ya existe

def existeContacto(n, dicc):

    existe = False

    if n in dicc.keys():
        existe = True

    return existe