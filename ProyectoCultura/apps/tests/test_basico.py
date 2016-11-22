from django.test import TestCase
from django.contrib.auth.models import User

from apps.artistas.models import Artista, Categoria, Departamento

class SimpleTest(TestCase):

	def test_save_user(self):
		user = User.objects.create(username='Juancho',first_name='Juan'
									, last_name='Mejia', email='juancho@email.com'  
									, password='juancho')
		departamento = Departamento.objects.create(nombre='Quetzaltenango')
		categoria = Categoria.objects.create(nombre='Musica')
		artista = Artista.objects.create(user=user,genero=True, departamento=departamento,
										fecha_nacimiento='1993-08-20', categoria=categoria, descripcion='Es un artista'
										, telefono='77635464')

		self.assertEqual(artista.user.username, 'Juao')