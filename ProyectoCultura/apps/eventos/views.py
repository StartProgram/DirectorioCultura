from django.shortcuts import render
from django.http import  HttpResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

from braces.views import LoginRequiredMixin

from .models import Evento
from .forms import EventoForm

# Create your views here.

def index(request):
    return render(request,'evento/evento.html')


class ListarEvento(ListView):
    model = Evento
    template_name = 'eventos/listar.html'


class ListarEventoUser(ListView):
    model = Evento
    template_name = 'eventos/listar_form.html'


class RegistrarEvento(LoginRequiredMixin ,CreateView):
    model = Evento
    form_class = EventoForm
    template_name = 'eventos/registro_form.html'
    login_url = '/'
    success_url = '/'

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)
        if form.is_valid():
            evento = form.save(commit=False)
            evento.user = request.user
            evento.save()
            return HttpResponse('Evento Creado')
        else:
            return self.render_to_response(self.get_context_data(form=form))



class EditarEvento(LoginRequiredMixin ,UpdateView):
    model = Evento
    form_class =EventoForm
    template_name= 'eventos/editar_form.html'
    success_url = '/'
    login_url= '/'

class EventoDelete(DeleteView):
    model = Evento
    template_name='evento/evento_delete.html'
    success_url = '/'