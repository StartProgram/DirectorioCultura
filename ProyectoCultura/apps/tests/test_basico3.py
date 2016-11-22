from django.test import TestCase
from django.contrib.auth.models import User

from apps.artistas.models import Artista, Categoria, Departamento
from apps.eventos.models import Evento, Resenia

class SimpleTest(TestCase):

	def setUp(self):
		departamento = Departamento.objects.create(nombre='Quetzaltenango')
		categoria = Categoria.objects.create(nombre='Musica')
		for x in range(0,5):
			user = User.objects.create(username='Juancho%s' % x, email='juancho%s@email.com'%x,
					password='juancho')
			artista = Artista.objects.create(user=user,genero=True, departamento=departamento,
											fecha_nacimiento='1993-04-20', categoria=categoria, 
											descripcion='Es un artista', telefono='77611908', autorizado=True)

			for i in range(0,5):
				evento = Evento.objects.create(user=user, titulo='titulo%s%s'%(x,i),categoria=categoria
												, horario='2017-01-05 12:00:00')

		for e in range(0,2):
			evento = Evento.objects.get(titulo='titulo0%s'%e)

			for n in range(0,3):
				user = User.objects.get(username='Juancho%s' %n)

				for m in range(0,2):
					resenia = Resenia.objects.create(user=user, evento=evento, contenido='comentario %s'%m)


	def test_save_user(self):
		user = User.objects.get(username="Juancho1")

		self.assertEqual(user.username, 'Juancho1')

		self.assertEqual(User.objects.count(), 5)

		
	def test_save_events(self):

		self.assertEqual(Evento.objects.count(), 25)

	def test_save_res(self):

		self.assertEqual(Resenia.objects.count(), 12)