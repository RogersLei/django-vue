from django.conf.urls import url

from . import views

urlpatterns = [
    # url('', views.index, name = 'index'),
    url('create/', views.create, name = 'create'),
    url('read', views.read, name = 'read'),
    url('update/', views.update, name = 'update'),
    url('delete/', views.delete, name = 'delete'),
    url('search', views.search, name = 'search')
]