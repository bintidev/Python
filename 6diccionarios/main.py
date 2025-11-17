

import menu, opcion
import ordenPorDefecto, ordenAlfabetico, nuevoContacto, modificar, busqueda, eliminar, borrar

menu.mostrarMenu()
entrada = opcion.opcionValida()

'''3. Si se ha indicado una opción correcta, se ejecuta según estas instrucciones que 
se indican a continuación. Una vez finalizada la opción se espera a que se pulse 
una tecla para continuar.'''

listinTelefonico = {
                        "Paola": "629 34 52 88",
                        "Jorge": "651 23 23 40",
                        "Marina": "617 45 62 34"
                    }

while (entrada != 'h'):

    # orden por defecto
    if (entrada == 'a'):

        print("\n" + ordenPorDefecto.mostrar(listinTelefonico))

    # orden alfabetico
    elif (entrada == 'b'):

        print("\n" + ordenAlfabetico.mostrar(listinTelefonico))

    # nuevo contacto
    elif (entrada == 'c'):

        nombre = input('Escriba el nombre del contacto a añadir: ')
        tel = input('Introduzca el numero del contacto a añadir: ')

        nuevoContacto.aniadir(nombre, tel, listinTelefonico)
        # actualiza el listin tras añadir el nuevo contacto
        listinTelefonico.update()

        print("\n¡Contacto añadido con éxito!")

    # modificar telefono de contacto
    elif (entrada == 'd'):

        nombre = input('Escriba el nombre del contacto a modificar: ')

        modificar.actualizarTelefono(nombre, listinTelefonico)
        # actualiza el listin tras modificar/añadir el contacto
        listinTelefonico.update()

        print("\n¡Contacto modificado/añadido con éxito!")

    # buscar teléfono
    elif (entrada == 'e'):

        telefono = input('Ingrese el número de teléfono a buscar: ')

        encontrado = busqueda.porNumero(telefono, listinTelefonico)

        if (encontrado != ''):
            print("\nNombre de contacto: {}".format(encontrado))

        else:
            print("\n¡Ups! Parece que no existe ningún contacto con ese número")

    # eliminar contacto
    elif (entrada == 'f'):

        nombre = input('Escriba el nombre del contacto a eliminar: ')

        if(eliminar.eliminarContacto(nombre, listinTelefonico)):
            # actualiza la lista si se ha podido borrar el contacto
            listinTelefonico.update()
            print("\n¡Contacto {} eliminado con éxito!".format(nombre))

        else:
            print("\n⚠ El contacto no existe. No se ha podido borrar el contacto")

    # borrar listin
    elif (entrada == 'g'):

        print("\n⚠ ¡¡ATENCION!! Está a punto de borrar toda su lista de contactos")
        confirmacion = input("\n¿Está seguro de querer proseguir con la operación? [ S / N ] ")
        
        if (borrar.borrarListin(confirmacion, listinTelefonico)):
            listinTelefonico.update()
            print("\n¡Se ha borrado la lista de contactos correctamente!")

        else:
            print("\n¡La operación ha sido cancelada!")
        

    menu.mostrarMenu()
    entrada = opcion.opcionValida()

print("\n¡Hasta luego! \n")
