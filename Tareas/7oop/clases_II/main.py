
from Persona import Persona
from Cuenta import Cuenta
from CuentaJoven import CuentaJoven

print('\n##########################################')
print('DATOS DE PERSONAS Y GESTIÓN DE CUENTAS')
print('##########################################')

print('\nCreación y visualización de objetos persona')
print('=============================================')

personaAdulta = Persona('', '', '02020202X', 30)

# prueba de funcionamiento de excepcion pasando edad tipo loat
print('\nIntento de instanciación de objeto Persona con edad tipo float...')
try:
    personaJoven = Persona('Binta', 'Diop Diop', '26771299N', 32.5)
except Exception as e:
    print(f'Error. {e}')

personaJoven = Persona('Binta', 'Diop Diop', '26771299N', 20)

print('\nPersona mayor de 25 años...')
personaAdulta.mostrar()

print('\nPersona menor de 25 años...')
personaJoven.mostrar()

print('\nModificación de datos de persona')
print('=================================')

# prueba de excepcion de setter pasando nombre vacio
print('\nIntento de modificación de nombre pasando una candena vacía...')
try:
    personaAdulta.setNombre('')
except Exception as e:
    print(f'Error. {e}')

personaAdulta.setNombre('Javier')
print('\nEstableciendo nombre de persona... LISTO')

personaAdulta.setApellidos('Figueroa Ramos')
print('Estableciendo apellidos de persona... LISTO')

print()

personaAdulta.mostrar()

print('\nCreación de cuentas bancarias')
print('===============================')

cuentaNormal = Cuenta(personaAdulta, 30543)

print('\nIntentando crear una cuenta joven con una bonificación de 120%...')
try:
    cuentaJoven = CuentaJoven(personaJoven, 1800.52, 120)
except Exception as e:
    print(f'Error. {e}')
    
cuentaJoven = CuentaJoven(personaJoven, 1800.52, 37)

print('\nCreación de una cuenta bancaria normal')
cuentaNormal.mostrar()

print('\nCreación de una cuenta bancaria joven')
cuentaJoven.mostrar()

print('\nOperaciones de cuenta')
print('===============================')

print('\nIntentando retirar -500€ de la cuenta normal...')
try:
    cuentaNormal.retirar(-500)
except Exception as e:
    print(f'Error. {e}')
    
print('\nIntentando retirar 1540,34€ de la cuenta normal...')
cuentaNormal.retirar(1540.34)
cuentaNormal.mostrar()

print('\nIntentando ingresar -2054€ en la cuenta joven...')
try:
    cuentaJoven.retirar(-2054)
    
except Exception as e:
    print(f'Error. {e}')
    
print('\nIntentando ingresar 1500€ en la cuenta joven...')
cuentaJoven.ingresar(1500)
cuentaJoven.mostrar()

print()

