from django.conf.urls import url

from . import views

urlpatterns = [
  url(r'^$', views.index, name='index'),
  url(r'^test/$', views.test, name='test'),
  url(r'^index/$', views.index2, name='index'),
  url(r'^base/$', views.base, name='base'),
  url(r'^restaurantes/$', views.restaurantes, name='restaurantes'),
]
