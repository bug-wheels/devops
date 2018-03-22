from django.urls import path

from . import views

urlpatterns = [
    path(r'', views.index, name="member/index"),
    path(r'members', views.members, name="member/members"),
    path(r'members/add', views.add, name="member/add"),
    path(r'members/modify', views.modify, name="member/modify"),
    path(r'member/remove', views.remove, name="member/remove"),

    path(r'departments', views.departments, name="department/list"),
    path(r'department/add', views.department_add, name="department/add"),
]