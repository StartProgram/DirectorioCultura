from django.db import models
from django.contrib.auth.models import User

from apps.eventos.models import Evento

# Create your models here.

class NotificacionBase(models.Model):
	verificado = models.BooleanField(default=False)


class NotificacionArtista(NotificacionBase):
	artista = models.OneToOneField(User, unique=True)



class NotificacionEvento(NotificacionBase):
	evento = models.OneToOneField(Evento, unique=True)


class Capsula(models.Model):
	titulo = models.CharField(max_length=10,null=False, blank=False)
	contenido = models.TextField(max_length=255, null=False)
	fecha = models.DateField()