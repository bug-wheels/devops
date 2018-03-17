# Create your views here.
import paramiko
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render

from asset.models import Asset, SystemUser


@login_required
def index(request):
    return render(request, "task/index.html")


@login_required
def once(request):
    assets = Asset.objects.all()
    return render(request, "task/once.html", {"assets": assets})


@login_required
def invoke_shell(request):
    asset_id = request.POST.get("assetId")
    shell = request.POST.get("shell")
    asset = Asset.objects.filter(id=asset_id).first()
    system_user = SystemUser.objects.filter(id=asset.user_id).first()

    ssh = paramiko.SSHClient()

    # 这行代码的作用是允许连接不在know_hosts文件中的主机。
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(asset.network_ip, port=asset.port, username=system_user.username, password=system_user.password)
    stdin, stdout, stderr = ssh.exec_command(shell)

    err_list = stderr.readlines()

    result = ""
    if len(err_list) > 0:
        result = 'ERROR:' + err_list[0]

    for item in stdout.readlines():
        result = result + item
    ssh.close()
    return JsonResponse({"code": 200, "msg": result}, safe=False)


@login_required
def inadd(request):
    return render(request, "task/add.html")


@login_required
def inadd_shell(request):
    return render(request, "task/add_shell.html")


@login_required
def history(request):
    return render(request, "task/history.html")


@login_required
def details(request):
    return render(request, "task/details.html")
