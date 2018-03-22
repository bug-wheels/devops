from django.urls import path

from . import views

urlpatterns = [
    path(r'', views.index, name="member/index"),
    path(r'members', views.members, name="member/members"),
    path(r'members/add', views.add, name="member/add"),
    path(r'members/modify', views.modify, name="member/modify"),
]