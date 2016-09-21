from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^(?P<szemely_id>[0-9]+)/$', views.detail, name='detail'),
	url(r'^delete/(?P<szemely_id>[0-9]+)/$', views.delete, name='delete'),
]