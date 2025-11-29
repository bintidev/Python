
'''1. Crea  una  clase  Persona  para  guardar  nombre,  apellidos,  DNI  y  edad  de  una 
persona. '''

class Persona:
    
    '''a. Define un constructor, donde se puedan indicar los datos iniciales (pueden 
    estar vacíos).'''
    def __init__(self, nombre: str, apellidos: str, dni: str, edad: int):
    
        if edad < 0 or isinstance(edad, int) == False:
            raise ValueError('El valor de edad debe ser un entero positivo')
    
        self.__nombre = nombre.upper()
        self.__apellidos = apellidos.upper()
        self.__dni = dni.upper()
        self.__edad = edad
        
        
    '''b. Para cada atributo define sus correspondientes setter (para poder validar el 
    valor de entrada: nombre, apellidos y DNI no pueden ser cadenas vacías y 
    se guardará en mayúsculas. Edad debe ser un valor entero positivo.'''
    def setNombre(self, nombre: str):
        
        if nombre == '':
            raise ValueError('El valor nombre no puede estar vacío')
        
        self.__nombre = nombre.upper()
        
    
    def setApellidos(self, apellidos: str) :
        
        if apellidos == '':
            raise ValueError('El valor apellidos no puede estar vacío')
        
        self.__apellidos = apellidos.upper()
        
        
    def setDni(self, dni: str) :
        
        if dni == '':
            raise ValueError('El valor DNI no puede estar vacío')
        
        self.__apellidos = dni.upper()
        
        
    def setEdad(self, edad: int) :
        
        if edad < 0 or isinstance(edad, int) == False:
            raise ValueError('El valor de edad debe ser un entero positivo')
        
        self.__edad = edad
        
    
    '''c. Para cada atributo define sus correspondientes getter. '''
    def getNombre(self):

        return self.__nombre
    
    def getApellidos(self):

        return self.__apellidos
    
    def getDni(self):

        return self.__dni
    
    def getEdad(self):

        return self.__edad
    
    
    '''d. Añade el método mostrar(), que muestra los datos de la persona (nombre, 
    apellidos, DNI edad).'''
    def mostrar(self):
        
        print(f'[ Nombre: {self.getNombre()} - Apellidos: {self.getApellidos()} - DNI: {self.getDni()} - Edad: {self.getEdad()} - Mayor de edad: {self.mayorDeEdad()} ]')
        
    '''e. Añade  el  método  mayorDeEdad(),  que  indica  si  la  persona  es  mayor  de 
    edad o no.'''
    def mayorDeEdad(self):
        
        esMayorDeEdad = False
        
        if self.__edad >= 18:
            esMayorDeEdad = True
            
        return esMayorDeEdad
    