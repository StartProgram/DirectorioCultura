from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth.views import login, logout_then_login

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
    # Examples:
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('apps.artistas.urls', namespace="artista"),),
    url(r'^', include('apps.eventos.urls', namespace="evento"),),
    url(r'^', include('apps.home.urls', namespace="home")),
    url(r'^', include('apps.adm.urls', namespace="adm")),
    url(r'^login/$', login, {'template_name': 'usuarios/login.html'},name="login"),
    url(r'^logout/$', 'django.contrib.auth.views.logout',{'next_page': '/'}, name="logout"),
    url(r'^$', 'django.contrib.auth.views.login',{'next_page': 'home/base_user.html'}),
    #url(r'^logout/',logout_then_login, name="logout"),
)	+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)