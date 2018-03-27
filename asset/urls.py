from django.urls import path

from . import views

urlpatterns = [
    path(r'', views.index, name="asset/index"),
    path(r'list', views.assets, name="asset/list"),
    path(r'add', views.add, name="asset/add"),
    path(r'modify', views.modify, name="asset/modify"),









]
