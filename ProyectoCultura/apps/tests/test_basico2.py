from django.test import TestCase
from django.contrib.auth.models import User

from apps.artistas.models import Artista, Categoria, Departamento
from apps.eventos.models import Evento

class SimpleTest(TestCase):

	def setUp(self):
		departamento = Departamento.objects.create(nombre='Quetzaltenango')
		categoria = Categoria.objects.create(nombre='Musica')
		user = User.objects.create(username='Juancho', email='juancho@email.com',
									password='juancho')
		artista = Artista.objects.create(user=user,genero=True, departamento=departamento
										,fecha_nacimiento='1993-08-20'
										, categoria=categoria, descripcion='Soy un artista'
										, telefono='77611908')

	def test_save_user(self):
		usuario = User.objects.get(username='Juancho')
		self.assertEqual(usuario.email, 'juancho@email.com')


	def test_save_event(self):
		usuario = User.objects.get(username='Juancho')
		evento = Evento.objects.create(user=usuario, titulo='Recaudacion', descripcion='Recaudar viveres.'
										,horario='2017-01-05 12:00:00')

		self.assertEqual(evento.user.username,'Juanco')

		