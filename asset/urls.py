from django.urls import path

from . import views

urlpatterns = [
    path(r'', views.index, name="asset/index"),
    path(r'list', views.assets, name="asset/list"),
    path(r'add', views.add, name="asset/add"),
    path(r'modify', views.modify, name="asset/modify"),

    path(r'sys_user', views.sys_user_index, name="sys/user"),
    path(r'sys_user_list', views.sys_user_list, name="sys/user/list"),
    path(r'sys_user_add', views.sys_user_add, name="sys/user/add"),
    path(r'sys_user_modify', views.sys_user_modify, name="sys/user/modify"),
]
