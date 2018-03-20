from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name="projects/index"),
    url(r'^detail$', views.detail, name="projects/detail"),
]