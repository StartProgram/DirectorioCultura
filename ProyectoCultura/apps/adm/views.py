from django.shortcuts import render
from django.views.generic import UpdateView, ListView, DetailView
from django.http import HttpResponse
from django.contrib.auth.models import User

from .models import NotificacionArtista, NotificacionEvento
from apps.artistas.models import Artista
from apps.eventos.models import Evento
# Create your views here.


class ListarNotificacion(ListView):
	#General
	model = NotificacionArtista
	template_name = 'usuarios/adm/notificacion.html'
	queryset = NotificacionArtista.objects.filter(verificado=False)
	context_object_name = 'artistas'
	

	def get_context_data(self, **kwargs):
		context = super(ListarNotificacion, self).get_context_data(**kwargs)
		context['eventos'] = NotificacionEvento.objects.filter(verificado=False)
		return context

class AutorizacionUsuario(UpdateView):
	model = User
	second_model = Artista
	template_name = 'usuarios/adm/autorizacionArtista.html'
	context_object_name = 'usuario'

	def post(self, request, *args, **kwargs):
		self.object = self.get_object
		pk = kwargs['pk']
		noti = NotificacionArtista.objects.get(artista = pk)
		artista = Artista.objects.get(user = pk)
		artista.autorizado = True
		noti.verificado = True
		noti.save()
		artista.save()
		return render(request, 'home/index_user.html')


class AutorizacionEvento(UpdateView):
	model = Evento
	template_name = 'usuarios/adm/autorizacionEvento.html'
	context_object_name = 'evento'

	def post(self, request, *args, **kwargs):
		self.object = self.get_object
		pk = kwargs['pk']
		noti = NotificacionEvento.objects.get(evento = pk)
		evento = Evento.objects.get(id = pk)
		evento.autorizado = True
		noti.verificado = True
		noti.save()
		evento.save()
		return render(request, 'home/index_user.html')