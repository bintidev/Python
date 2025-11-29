
import menu, opcion, existencia, confirmar
from Persona import Persona

menu.mostrarMenu()
entrada = opcion.opcionValida()

while (entrada != 'f'):

    # listado alfabetico
    if (entrada == 'a'):

        print(Persona.mostrar_alfabeticamente())

    # añadir un nuevo contacto
    elif (entrada == 'b'):

        nombre = input('\nIngrese el nombre del nuevo contacto: ')
        direcc = input('Ingrese la dirección de domicilio de la persona: ')
        tel = input('Ingrese el número de teléfono asociado: ')
        
        if (Persona.nuevo_contacto(nombre.upper(), direcc, tel)):
            print('\n¡Contacto añadido/actualizado con éxito!')
        else:
            print('\nSe ha cancelado la operación')

    # HECHO
    elif (entrada == 'c'):

        nombre = input('\nIngrese el nombre del contacto a modificar: ')
        
        if (Persona.modificar_contacto(nombre.upper())):
            print('\n¡Contacto modificado/insertado con éxito!')
        else:
            print('\nSe ha cancelado la operación')

    # HECHO
    elif (entrada == 'd'):

        tel = input('\nIngrese el número de teléfono asociado: ');
        
        if Persona.buscar_contacto(tel) == '':
            print(f'\nNo hay ningún contacto con el teeléfono {tel} asociado')
            
        else:
            print(f'\nNombre de contacto con el teléfono {tel}: {Persona.buscar_contacto(tel)}')

    # HECHO
    elif (entrada == 'e'):

        nombre = input('\nIngrese el nombre del contacto que desea eliminar: ')
        
        if Persona.eliminar_contacto(nombre.upper()):
            print(f'\n¡Se ha eliminado el contacto correctamente!')
            
        else:
            print(f'\nError. No se ha encontrado el contacto.')

    menu.mostrarMenu()
    entrada = opcion.opcionValida()

print("\nPrograma terminado. Bye bye! \n")