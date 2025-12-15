
from Persona import Persona

'''2. Crea  una  clase  Cuenta,  que  tendrá  los  siguientes  atributos:  titular  (que  es  una 
persona) y cantidad (puede tener decimales).'''

class Cuenta:
    
    '''a. Define un constructor, teniendo en cuenta que el titular es obligatorio y la 
    cantidad es opcional.'''
    def __init__(self, titular: Persona, cantidad: float):
        
        self._titular = titular
        self._cantidad = cantidad
        
        
    '''b. Define los getter y setter, teniendo en cuenta que la cantidad no se puede 
    modificar directamente sino realizando ingresos o retiradas de dinero. '''
    def getTitular(self):
        
        self._titular.mostrar()
    
    def getCantidad(self):
        
        return self._cantidad
    
    def setTitular(self, nombre: str, apellidos: str, dni: str, edad: int):
        
        self._titular.setNombre(nombre)
        self._titular.setApellidos(apellidos)
        self._titular.setDni(dni)
        self._titular.setEdad(edad)
        
        
    '''c. Define  ingresar(cantidad),  que  ingresa  la  cantidad  indicada  (hay  que 
    comprobar que la cantidad es positiva).'''
    def ingresar(self, cantidad: float):
        
        if cantidad < 0:
            raise ValueError('La cantidad a ingresar debe ser positiva')
        
        self._cantidad += cantidad
        
        
    '''d. Define retirar(cantidad), que retira la cantidad indicada (hay que comprobar 
    que la cantidad es positiva). La cuenta se puede quedar en números rojos. '''
    def retirar(self, cantidad: float):
        
        if cantidad < 0:
            raise ValueError('La cantidad a retirar debe ser positiva')
        
        self._cantidad -= cantidad
        
        
    '''e. Define mostrar, que muestra todos los datos de la cuenta.'''
    def mostrar(self):
        
        self.getTitular()
        print (f'[ Cantidad: {self.getCantidad()}€ ]')