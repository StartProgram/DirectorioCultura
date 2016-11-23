from django.conf.urls import  patterns, url

from .views import ListarEvento, RegistrarEvento, EditarEvento


urlpatterns = patterns('',
	
    url(r'^listar/evento/$', ListarEvento.as_view(), name='listar'),
    url(r'^registro/evento/$', RegistrarEvento.as_view(), name='crear'),
    url(r'^editar/evento/(?P<pk>\d+)/$',EditarEvento.as_view(), name='editar'),
)
