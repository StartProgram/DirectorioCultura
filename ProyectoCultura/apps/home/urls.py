from django.conf.urls import patterns, include, url
from .views import IndexView, IndexViewUser

urlpatterns = patterns('',
	url(r'^$', IndexView.as_view(), name="index"), 
	url(r'^$', IndexViewUser.as_view(), name="home_user"), 

)
