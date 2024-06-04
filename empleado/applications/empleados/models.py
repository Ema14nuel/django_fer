from django.db import models
from applications.departamento.models import Departamento


class Habilidades(models.Model):
    habilidad = models.CharField('Habilidad', max_length=50)

    class Meta:
        verbose_name = 'Habilidad'
        verbose_name_plural = 'Habilidades del Empleado'

    def __str__(self):
        return str(self.id)+ ' - '+ self.habilidad

# Create your models here.
class Empleado(models.Model):
    """ Datos empleado """

    JOB_CHOICES = (
        ('0', 'CONTADOR'),
        ('1', 'ADMINISTRADOR'),
        ('2', 'ECONOMISTA'),
        ('3', 'OTRO'),
    )

    first_name = models.CharField('Nombres', max_length=50)
    last_name = models.CharField('apellidos', max_length=50)
    job = models.CharField('trabajo', max_length=1, choices=JOB_CHOICES)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='empleado', blank=True, null=True)
    habilidades = models.ManyToManyField(Habilidades)
    hoja_vida = models.TextField()

    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'
        ordering = ['first_name']

    def __str__(self):
        return str(self.id) + '-' + self.first_name + '-' + self.last_name
    