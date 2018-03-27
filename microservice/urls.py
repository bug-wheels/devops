from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name="microservice/index"),
    url(r'^add$', views.add, name="microservice/add"),
]
