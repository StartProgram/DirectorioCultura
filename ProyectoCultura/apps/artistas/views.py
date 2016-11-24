from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic import DetailView, CreateView, ListView, UpdateView
from django.http import HttpResponse

from braces.views import LoginRequiredMixin

from .models import Artista
from .forms import ArtistaForm, UserCreateForm, ArtistaUpdateForm, UserUpdateForm

class PerfilArtista(DetailView):

	model = Artista
	template_name = 'artistas/perfil_detail.html'
	

class RegistroArtista(CreateView):
	form_class = ArtistaForm
	second_form_class = UserCreateForm 
	template_name = 'artistas/registro_form.html'
	success = "/"

	#Metodo para ver si esta dibujado los forms en el html
	def get_context_data(self, **kwargs):
		context = super(RegistroArtista, self).get_context_data(**kwargs)
		if 'form' not in context:
			context['form'] = self.form_class(self.request.GET)
		if 'form2' not in context:
			context['form2'] = self.second_form_class(self.request.GET)
		return context

	#Metodo que toma el metodo post que el formulario envia,
	#Verfica si son validos, guarda el primer formulario, para 
	#conseguir al usuario y lo vincula con artista
	def post(self, request, *args, **kwargs):
		self.object = self.get_object
		form = self.form_class(request.POST, request.FILES)
		form2 = self.second_form_class(request.POST)
		if form.is_valid() and form2.is_valid():
			artista = form.save(commit=False)
			artista.user = form2.save()
			artista.save()
			return render(request, 'home:index')
		else:
			return self.render_to_response(self.get_context_data(form=form, form2= form2))


class EditarArtista(LoginRequiredMixin ,UpdateView):

	model = User
	second_model = Artista
	template_name = "artistas/editar_form.html"
	form_class = ArtistaUpdateForm
	second_form_class = UserUpdateForm
	login_url= '/'

	def get_context_data(self, **kwargs):
		context = super(EditarArtista, self).get_context_data(**kwargs)
		pk = self.kwargs.get('pk', 0)
		usuario = self.model.objects.get(id=pk)
		artista = self.second_model.objects.get(user = usuario.id)
		context['artista'] = artista
		if 'form' not in context:
			context['form'] = self.form_class()
		if 'form2' not in context:
			context['form2'] = self.second_form_class(instance=usuario)
		return context

	def post(self, request, *args, **kwargs):
		self.object = self.get_object()
		pk = kwargs['pk']
		artista = self.model.objects.get(id=pk)
		usuario = self.second_model.objects.get(id = artista.user_id)
		form = self.form_class(request.POST, request.FILES, instance=artista)
		form2 = self.second_form_class(request.POST, instance=usuario)
		if form.is_valid() and form2.is_valid():
			form.save()
			form2.save()
			return HttpResponse("Se modifico correctamente")
		else:
			return self.render_to_response(self.get_context_data(form=form, form2= form2))

class ListarArtista(ListView):
	#General
	model = Artista
	template_name = 'artistas/listar_form.html'

