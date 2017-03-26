from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^reddit$', views.reddit, name='reddit'),
	url(r'^inshorts$', views.inshorts, name='inshorts'),
]