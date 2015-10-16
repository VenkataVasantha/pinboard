from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^page/(?P<page>[1-3])/$', views.load_page, name='loadpage')
]