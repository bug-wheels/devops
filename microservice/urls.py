from django.urls import path

from . import views

urlpatterns = [
    path(r'', views.index, name="microservice/index"),
    path(r'setting', views.setting, name="microservice/setting"),
    path(r'monitor', views.monitor, name="microservice/monitor"),
    path(r'add', views.add, name="microservice/add"),
    path(r'overview', views.overview, name="microservice/overview"),
]
