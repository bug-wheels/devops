"""devops URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^member/', include('member.urls')),  # 成员管理
    url(r'^project/', include('projects.urls')),  # 项目管理
    url(r'^asset/', include('asset.urls')),  # 资产管理
    url(r'^task/', include('task.urls')),  # 任务管理
    url(r'^document/', include('document.urls')),  # 文档协作
    url(r'^gitosc/callback/', views.gitosc),  # 文档协作
    url(r'^$', views.index, name='index'),
    url(r'^login$', views.login, name='login'),
    url(r'^logout$', views.logout, name='logout'),
]

urlpatterns += staticfiles_urlpatterns()