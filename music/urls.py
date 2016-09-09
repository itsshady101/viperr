from django.conf.urls import include, url
from . import views
app_name = 'music'

urlpatterns = [
	# /music/
	url(r'^$', views.IndexView.as_view(), name='index'),

	# /music/712/
	url(r'^(?P<album_id>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
]