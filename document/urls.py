from django.urls import path

from . import views

urlpatterns = [
    path(r'', views.index, name="document/index"),
    path(r'detail', views.detail, name="document/detail"),
    path(r'write', views.write, name="document/write"),

]
