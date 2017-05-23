from django.conf.urls import url
from django.contrib.auth.views import login
from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^git/$', views.git, name='git'),
	url(r'^ss/$', views.ss, name='ss'),
	url(r'^new_token/$', views.new_token, name='new_token'),
	url(r'^logout/$', views.logout_d, name='logout'),
	url(r'^login/$', login, {'template_name': 'evedb/login.html'}, name='login'),
]