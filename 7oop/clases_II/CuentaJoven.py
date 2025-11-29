
from Cuenta import Cuenta
from Persona import Persona

'''3. Crea  una  clase  CuentaJoven,  para  clientes  menores  de  25  años.  Hereda  de  la 
clase Cuenta, a la que se añade: '''

class CuentaJoven(Cuenta):
    
    '''a. Un atributo bonificacion, que guarda el porcentaje de bonificación que se le 
    da al cliente a final de año. Al tratarse de un porcentaje, debe ser un valor 
    entre 0 y 100. '''
    def __init__(self, titular: Persona, cantidad: float, bonificacion: int):
        
        if bonificacion < 0 or bonificacion > 100:
            raise ValueError('El porcentaje de bonificaión debe estar entre 0 y 100')
        
        super().__init__(titular, cantidad)
        self.__bonificacion = bonificacion
        
    
    ''''b. Adapta mostrar para que se vea toda la información de la cuenta joven.'''
    def mostrar(self):
        
        super().mostrar()
        print (f'[ Bonificación: {self.__bonificacion}% ]')