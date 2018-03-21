from django.urls import path
from . import views

urlpatterns = [
    path(r'', views.index, name="member/index"),
    path(r'members', views.members, name="member/members"),
]