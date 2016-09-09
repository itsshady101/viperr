from django.conf.urls import include, url
from . import views
app_name = 'music'

urlpatterns = [
	# /music/
	url(r'^$', views.index, name='index'),

	# /music/712/
	url(r'^(?P<album_id>[0-9]+)/$', views.detail, name='detail'),

	# /music/712/favorite
	url(r'^(?P<album_id>[0-9]+)/favourite/$', views.favourite, name='favourite'),
]