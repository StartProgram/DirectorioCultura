from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from django import forms



from .models import Artista


class ArtistaForm(forms.ModelForm):

	class Meta:
		model = Artista
		fields = [
				'genero',
				'fecha_nacimiento',
				'imagen',
				'departamento',
				'telefono',
				'categoria',
				'descripcion',
			]

class UserCreateForm(UserCreationForm):

	class Meta:
		model = User
		fields = [
				'first_name',
				'last_name',
				'username',
				'email',
				'password1',
				'password2',
		]


class ArtistaUpdateForm(forms.ModelForm):

	class Meta:
		model = Artista
		fields = [
				'imagen',
				'telefono',
				'descripcion',
		]

class UserUpdateForm(forms.ModelForm):

	class Meta:
		model = User
		fields = [
				'username',
				'first_name',
				'last_name',
				'email',
		]