from django.shortcuts import render
from django.http import  HttpResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

from braces.views import LoginRequiredMixin

from .models import Evento
from .forms import EventoForm
from apps.adm.models import NotificacionEvento

# Create your views here.

def index(request):
    return render(request,'evento/evento.html')


class ListarEvento(ListView):
    model = Evento
    template_name = 'eventos/listar.html'
    queryset = Evento.objects.filter(autorizado=True)

    def get_context_data(self, **kwargs):
        context = super(ListarEvento, self).get_context_data(**kwargs)
        context['eventos'] = Evento.objects.filter(autorizado=True)[:3]
        return context


class ListarEventoUser(ListView):
    model = Evento
    template_name = 'eventos/listar_form.html'
    def get_context_data(self, **kwargs):
        context = super(ListarEventoUser, self).get_context_data(**kwargs)
        context['evento'] = Evento.objects.filter(user=self.request.user)
        return context



class RegistrarEvento(LoginRequiredMixin ,CreateView):
    model = Evento
    form_class = EventoForm
    template_name = 'eventos/registro_form.html'
    login_url = '/'
    success_url = '/'

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST, self.request.FILES)
        if form.is_valid():
            evento = form.save(commit=False)
            evento.user = request.user
            if request.user.is_superuser:
                evento.autorizado=True
                evento.save()
            else:
                evento.save()
                noti = NotificacionEvento.objects.create(evento=evento)
                noti.save()
            return render(request, 'home/index_user.html')
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