from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from apps.eventos.models import Evento
# Create your views here.

class IndexView(ListView):
	template_name = 'home/index.html'
	model = Evento
	context_object_name = 'eventos'
	queryset = Evento.objects.all()[:3]



class IndexViewUser(TemplateView):
	template_name = 'home/index_user.html'
