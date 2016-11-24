from django.db import models
from django.contrib.auth.models import User

from apps.artistas.models import Artista, Categoria
# Create your models here.


class Tamanio(models.Model):
    descripcion = models.CharField(max_length=10)


class Evento(models.Model):
    user = models.ForeignKey(User,null=False, blank=False, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=45)
    categoria = models.ForeignKey(Categoria, null=True, blank=True, on_delete=models.CASCADE)
    direccion = models.CharField(max_length=70)
    horario = models.DateTimeField(null=True, blank=True)
    tamanio = models.ForeignKey(Tamanio, null=True, blank=True, on_delete=models.CASCADE)
    descripcion = models.TextField(max_length=200)
    imagen = models.ImageField(upload_to='img/', null=True, blank=True)


class Resenia(models.Model):
	user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
	nombre = models.CharField(max_length=35, null=True, blank=True)
	contenido = models.TextField(max_length=250)
	evento = models.ForeignKey(Evento, null=False, blank=False, on_delete=models.CASCADE)
