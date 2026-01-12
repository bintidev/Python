from django.db import models

# Create your models here.
# Create your models here.
# Al aplicar esta herencia, Django va a saber que Author es una tabla en la BD
class Author (models.Model):

    name = models.CharField (
        verbose_name ='Nombre', # etiqueta dentro de la tabla
        max_length = 100,
        default = ''
    )

    last_name = models.CharField(
        verbose_name='Apellido',
        max_length = 150,
        default = ''
    )

    mail = models.CharField(
        verbose_name ='Email',
        max_length = 150,
        default = ''
    )

    age = models.PositiveSmallIntegerField(
        verbose_name = 'Edad',
        default = 0
    )

    phone_number = models.CharField(
        verbose_name = 'Teléfono',
        max_length = 9,
        default = ''
    )

    nivel_ingles = models.CharField(
        verbose_name = 'Nivel de inglés',
        max_length = 50,
        default = ''
    )

    # añadimos este código para que en el administrador al acceder a los
    # registros que contiene la tabla aparezca no Author object ID, sino que nos
    # de más información del registro que hay dentro (nombre y apellido).

    # con el método __str__, sobreescribimos la información por defecto. Indicamos
    # ahí lo que queramos que nos retorne

    # ojo, está dentro de la clase
    def __str__(self):
        return f'{self.name} {self.last_name}'
    

class Book (models.Model):

    # Unique=True , Django no va a permitir introducir dos libros con títulos
    # iguales. Cuando cree este campo en la BD solo permitir valores diferentes.
    cod = models.CharField(
        'Codigo',
        max_length = 15,
        unique = True
    )

    title = models.CharField(
        'Título del libro',
        max_length = 255,
        unique = True
    )

    num_paginas = models.PositiveSmallIntegerField(
        'Número de páginas',
        default = 50
    )

    editorial = models.CharField(
        'Editorial',
        max_length = 80,
        default = ''
    )

    author = models.ManyToManyField(Author)
    # Cascade ,de esta forma indicamos que cuando se borre un autor en la Bd,
    # también se borrará el libro.
    # De esta forma indicamos que en el campo author de aquellos libros en los
    # que el author se haya borrado, django pondrá el valor null. Para ello se le
    # indica que pude aceptar valor null a True.

    def __str__(self):
        return f'{self.title}'