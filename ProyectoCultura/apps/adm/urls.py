from django.contrib import admin
from django.conf.urls import patterns, url

from .views import ListarNotificacion,AutorizacionUsuario, AutorizacionEvento


urlpatterns = patterns('',

	url(r'^adm/notificacion/$', ListarNotificacion.as_view(), name="notificacion"),
	url(r'^autorizar/user/(?P<pk>\d+)/$', AutorizacionUsuario.as_view(), name='autorizacion_artista'),
	url(r'^autorizar/evento/(?P<pk>\d+)/$', AutorizacionEvento.as_view(), name='autorizacion_evento'),
)