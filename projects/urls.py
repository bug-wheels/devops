from django.urls import path

from . import views

urlpatterns = [
    path(r'', views.index, name="projects/index"),
    path(r'dashboard', views.dashboard, name="projects/dashboard"),
    path(r'analysis', views.analysis, name="projects/analysis"),

    path(r'list', views.project_list, name="projects/list"),
    path(r'task', views.project_task, name="projects/task"),
    path(r'detail', views.detail, name="projects/detail"),
    path(r'add', views.add, name="projects/add"),
    path(r'tags', views.tags, name="projects/tags"),
    path(r'tags_list', views.tags_list, name="projects/tags_list"),
    path(r'tags_add', views.tags_add, name="projects/tags_add"),
]