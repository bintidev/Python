

import menu, opcion
import ordenPorDefecto, ordenAlfabetico, nuevoContacto, modificar

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

        listinTelefonico.update(nuevoContacto.aniadir(nombre, tel, listinTelefonico))

        print("\n¡Contacto añadido con éxito!")

    # modificar telefono de contacto
    elif (entrada == 'd'):

        nombre = input('Escriba el nombre del contacto a modificar: ')

        listinTelefonico.update(modificar.actualizarTelefono(nombre, listinTelefonico))

        print("\n¡Contacto modificado/añadido con éxito!")

    # buscar teléfono



    menu.mostrarMenu()
    entrada = opcion.opcionValida()

print("\nPrograma terminado. Bye bye! \n")
