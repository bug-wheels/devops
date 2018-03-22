from django.urls import path

from . import views

urlpatterns = [
    path(r'', views.index, name="projects/index"),
    path(r'list', views.project_list, name="projects/list"),
    path(r'detail', views.detail, name="projects/detail"),
    path(r'add', views.add, name="projects/add"),
]