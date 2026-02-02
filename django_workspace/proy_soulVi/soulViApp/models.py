from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Usuario(models.Model):

    num_tarjeta_sanitaria = models.CharField(
        primary_key = True,
        verbose_name = 'Nº de tarjeta sanitaria',
        max_length = 10,
        default = ''
    )

    nombre = models.CharField(
        verbose_name = 'Nombre',
        max_length = 100,
        default = ''
    )

    apellidos = models.CharField(
        verbose_name = 'Apellidos',
        max_length = 100,
        default = ''
    )

    email = models.EmailField(
        verbose_name = 'Correo',
        max_length = 100,
        default = '',
        blank = False,
        unique = True
    )

    contrasenya = models.CharField(
        verbose_name = 'Contraseña',
        min_length = 8,
        default = '',
        null = False,
        unique = True
    )


class Medico(models.Model):

    id_medico = models.CharField(
        primary_key = True,
        verbose_name = 'ID Doctor',
        max_length = 5,
        default = ''
    )

    nombre = models.CharField(
        verbose_name = 'Nombre',
        max_length = 100,
        default = ''
    )

    apellidos = models.CharField(
        verbose_name = 'Apellidos',
        max_length = 100,
        default = ''
    )

    especializacion = models.CharField(
        verbose_name = 'Especialización',
        max_length = 100,
        default = ''
    )


class Cita(models.Model):

    id_cita = models.CharField(
        primary_key = True,
        verbose_name = 'ID Cita',
        max_length = 8,
        default = ''
    )

    paciente = models.ForeignKey(Usuario.num_tarjeta_sanitaria)

    medico = models.ManyToManyField(Medico)

    fecha = models.DateField(
        blank = False,
        null = False
    )

    hora = models.TimeField(
        blank = False,
        null = False
    )

