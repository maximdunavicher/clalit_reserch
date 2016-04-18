__author__ = 'max'

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^details/$', views.detail, name='detail'),
]