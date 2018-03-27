import logging

import requests
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.shortcuts import render, HttpResponseRedirect

from .forms import *

logger = logging.getLogger(__name__)


@login_required
def index(request):
    return render(request, "index.html")


def gitosc(request):
    code = request.GET.get("code")
    print(f"code: {code}")
    client_id = '2493eceb4bd49ed51e744ac3a6817e39567f140a539c2c6d3a3c2208454760a2'
    client_secret = '4d25bec9ca69db6797948108c00764351e5d57893b57235e3f83e35779f04dd6'
    redirect_uri = 'http://devops777.ngrok.xiaomiqiu.cn/gitosc/callback'
    git_response = requests.post(
        f"https://gitee.com/oauth/token?grant_type=authorization_code&code={code}&client_id={client_id}&redirect_uri={redirect_uri}&client_secret={client_secret}")
    print(git_response)
    return HttpResponseRedirect('/')


def login(request):
    if request.method == 'GET':
        form = LoginForm()
        return render(request, 'login.html', {'form': form})
    else:
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST.get('username', '')
            password = request.POST.get('password', '')
            user = auth.authenticate(username=username, password=password)
            if user and user.is_active:
                auth.login(request, user)
                logger.info("+" * 100)
                logger.info(f"({username}) 登陆了")
                logger.info("+" * 100)
                return HttpResponseRedirect('/')
            else:
                logger.error("x" * 100)
                logger.error(f"({username}) 尝试登录，输入了错误的密码({password})")
                logger.error("x" * 100)
                return render(request, 'login.html', {'form': form, 'error_msg': "用户名或密码错误"})
        else:
            return render(request, 'login.html', {'form': form})


@login_required
def logout(request):
    logger.info("-" * 100)
    logger.info(f"({request.user.username}) 登出了")
    logger.info("-" * 100)
    auth.logout(request)
    return HttpResponseRedirect("login")


@login_required
def changepwd(request):
    if request.method == 'GET':
        form = ChangepwdForm()
        return render(request, 'chameleon/changepwd.html', {'form': form})
    else:
        form = ChangepwdForm(request.POST)
        if form.is_valid():
            username = request.user.username
            oldpassword = request.POST.get('oldpassword', '')
            user = auth.authenticate(username=username, password=oldpassword)
            if user is not None and user.is_active:
                newpassword = request.POST.get('newpassword1', '')
                if oldpassword == newpassword:
                    logger.error('x' * 100)
                    logger.error(f"({username}) 尝试修改密码，旧密码和新密码不能相同({oldpassword})({newpassword})")
                    logger.error('x' * 100)
                    return render(request, 'chameleon/changepwd.html', {'form': form, 'error_msg': "旧密码和新密码不能相同"})
                try:
                    validate_password(newpassword)
                except ValidationError as e:
                    return render(request, 'chameleon/changepwd.html', {'form': form, 'error_msg': e})
                logger.info('ok ' * 100)
                logger.info(f"({username}) 修改了密码，原密码({oldpassword}),新密码({newpassword})")
                logger.info('ok ' * 100)
                user.set_password(newpassword)
                user.save()
                return render(request, 'chameleon/index.html', {'changepwd_success': True})
            else:
                logger.error('x' * 100)
                logger.error(f"({username}) 尝试修改密码，输入了错误的密码({oldpassword})")
                logger.error('x' * 100)
                return render(request, 'chameleon/changepwd.html', {'form': form, 'error_msg': "原密码不正确"})
        else:
            return render(request, 'chameleon/changepwd.html', {'form': form})
