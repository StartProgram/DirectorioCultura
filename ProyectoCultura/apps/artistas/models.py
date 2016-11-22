from django.db import models
from django.contrib.auth.models import User

class Categoria(models.Model):
	nombre = models.CharField(max_length=25)

	def __unicode__(self):
		return '{}'.format(self.nombre)


class Departamento(models.Model):
	nombre = models.CharField(max_length=30)

	def __unicode__(self):
		return '{}'.format(self.nombre)


class Artista(models.Model):
	BOOL_CHOICES = ((True,'Masculino'),(False,'Femenino'))
	user = models.OneToOneField(User, unique=True)
	genero = models.BooleanField(choices = BOOL_CHOICES,default=True)
	fecha_nacimiento = models.DateField()
	imagen = models.ImageField(upload_to='img/', null=True, blank=True)
	autorizado = models.BooleanField(default=False)
	departamento = models.ForeignKey(Departamento, null=True, blank=True, on_delete=models.CASCADE)
	telefono = models.CharField(max_length=10, null=True, blank=True)
	categoria = models.ForeignKey(Categoria, null=True, blank=True, on_delete=models.CASCADE)
	descripcion = models.TextField(max_length=150, null=True, blank=True)

	def __unicode__(self):
		return '{}'.format(self.user.username)
