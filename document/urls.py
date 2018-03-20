from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name="document/index"),
    url(r'^detail$', views.detail, name="document/detail"),

]
