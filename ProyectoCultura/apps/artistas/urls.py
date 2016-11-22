from django.conf.urls import patterns, url
from .views import RegistroArtista, PerfilArtista, EditarArtista, ListarArtista

urlpatterns = patterns('',
	 url(r'^registro/artista/$', RegistroArtista.as_view(), name="registro"),
     url(r'^usuario/(?P<pk>\d+)/$', PerfilArtista.as_view(), name="perfil"),
     url(r'^editar/(?P<pk>\d+)/$', EditarArtista.as_view(), name='editar'),
     url(r'^listar/artista/$', ListarArtista.as_view(), name='listar'),
)
