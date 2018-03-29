from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from asset.models import Asset, SystemUser


def index(request):
    return render(request, 'asset/index.html')


def assets(request):
    result = Asset.objects.values().all()
    return JsonResponse({"code": 200, "records": list(result)}, safe=False)


@login_required
def add(request):
    hostname = request.POST.get("hostname")
    network_ip = request.POST.get("network_ip")
    inner_ip = request.POST.get("inner_ip")
    port = request.POST.get("port")
    remark = request.POST.get("remark")
    Asset.objects.create(hostname=hostname, network_ip=network_ip, inner_ip=inner_ip, port=port, remark=remark)
    return JsonResponse({"code": 200, "msg": "添加成功"}, safe=False)


@login_required
def modify(request):
    id = request.POST.get("id")
    hostname = request.POST.get("hostname")
    network_ip = request.POST.get("network_ip")
    inner_ip = request.POST.get("inner_ip")
    port = request.POST.get("port")
    remark = request.POST.get("remark")
    Asset.objects.filter(id=id).update(hostname=hostname, network_ip=network_ip, inner_ip=inner_ip, port=port,
                                       remark=remark)
    return JsonResponse({"code": 200, "msg": "修改成功"}, safe=False)


@login_required
def sys_user_index(request):
    return render(request, 'asset/sys_index.html')


@login_required
def sys_user_list(request):
    result = SystemUser.objects.values().all()
    return JsonResponse({"code": 200, "records": list(result)}, safe=False)


@login_required
def sys_user_add(request):
    name = request.POST.get("name")
    password = request.POST.get("password")
    remark = request.POST.get("remark")
    SystemUser.objects.create(name=name, password=password, remark=remark)
    return JsonResponse({"code": 200, "msg": "保存成功"}, safe=False)


@login_required
def sys_user_modify(request):
    name = request.POST.get("name")
    password = request.POST.get("password")
    remark = request.POST.get("remark")
    id = request.POST.get("id")
    SystemUser.objects.filter(id=id).update(name=name, password=password, remark=remark)
    return JsonResponse({"code": 200, "msg": "修改成功"}, safe=False)
