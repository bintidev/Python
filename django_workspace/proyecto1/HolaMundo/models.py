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

    # añadimos este código para que en el administrador al acceder a los
    # registros que contiene la tabla aparezca no Author object ID, sino que nos
    # de más información del registro que hay dentro (nombre y apellido).

    # con el método __str__, sobreescribimos la información por defecto. Indicamos
    # ahí lo que queramos que nos retorne

    # ojo, está dentro de la clase
    def __str__(self):
        return f'{self.name} {self.last_name}'