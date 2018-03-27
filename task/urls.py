from django.urls import path

from . import views

urlpatterns = [
    path(r'', views.index, name="task/index"),
    path(r'inadd', views.inadd, name="task/inadd"),
    path(r'inaddshell', views.inadd_shell, name="task/inaddshell"),
    path(r'once', views.once, name="task/once"),
    path(r'invoke_shell', views.invoke_shell, name="task/invoke_shell"),
    path(r'history', views.history, name="task/history"),
    path(r'details', views.details, name="task/details"),
]
