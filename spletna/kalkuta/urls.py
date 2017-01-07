from . import views
from django.conf.urls import url
from django.contrib.auth import views as auth_views

urlpatterns = [
	url(r'^$', views.landing, name='landing'),
	url(r'pregled', views.dash, name='dash'),
	url(r'polog', views.prilivi, name='prilivi'),
	url(r'strosek', views.odlivi, name='odlivi'),
	url(r'cilji', views.cilji, name='cilji'),


	url(r'^login/$', auth_views.login, name='login'),
	url(r'^logout/$', auth_views.logout, name='logout'),
	url(r'^register/$', views.register, name='register'),

]
