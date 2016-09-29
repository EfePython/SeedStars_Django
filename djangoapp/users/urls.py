from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^list/$', views.list_users, name='list_users'),
    url(r'^add/$', views.add_user, name='add_user'),
]
