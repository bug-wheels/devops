# Create your views here.
import paramiko
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render

from asset.models import Asset
from task.models import TaskHistory


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
    if not asset.system_user:
        return JsonResponse({"code": 200, "msg": "该资产未绑定登录用户，请修改"}, safe=False)

    ssh = paramiko.SSHClient()

    # 这行代码的作用是允许连接不在know_hosts文件中的主机。
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(asset.network_ip, port=asset.port, username=asset.system_user.username,
                    password=asset.system_user.password)
    except Exception as e:
        TaskHistory.objects.create(host_name=asset.hostname, ip=asset.network_ip, shell=shell,
                                   operation_name=request.user.username, operation_id=1)
        return JsonResponse({"code": 200, "msg": e.args[0]}, safe=False)
    stdin, stdout, stderr = ssh.exec_command(shell)

    err_list = stderr.readlines()

    result = ""
    if len(err_list) > 0:
        result = 'ERROR:' + err_list[0]

    for item in stdout.readlines():
        result = result + item
    ssh.close()
    TaskHistory.objects.create(host_name=asset.hostname, ip=asset.network_ip, shell=shell,
                               operation_name=request.user.username, operation_id=1)
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
def historys(request):
    results = TaskHistory.objects.values().all()
    return JsonResponse({"code": 200, "records": list(results)}, safe=False)


@login_required
def details(request):
    return render(request, "task/details.html")
