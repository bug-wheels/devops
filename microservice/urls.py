from django.urls import path

from . import views

urlpatterns = [
    path(r'', views.index, name="microservice/index"),
    path(r'add', views.add, name="microservice/add"),
]
