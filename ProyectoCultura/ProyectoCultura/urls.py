from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth.views import login

urlpatterns = patterns('',
    # Examples:
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),	
    url(r'^', include('apps.artistas.urls', namespace="artista"),),
    url(r'^', include('apps.eventos.urls', namespace="evento"),),
    url(r'^', include('apps.home.urls', namespace="home")),
    url(r'^', login, {'template_name': 'home/login.html'},name="login")
)
