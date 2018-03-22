from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from member.models import Member

__author__ = 'yunan.zhang zyndev@gmail.com'


def index(request):
    return render(request, "member/index.html")


def members(request):
    """
    Search members by name or telephone.
    Todo: 此处需要添加公司限制
    :param request:
    :return:
    """
    search_param = request.GET.get("searchParam", None)
    if not search_param:
        result = Member.objects.values().all()
    else:
        result = Member.objects.filter(name__icontains=search_param).values().all()
    return JsonResponse({"code": 200, "records": list(result)}, safe=False)


def add(request):
    """
    add a member.
    TODO: 此处需要添加公司限制和给予登录权限
    :param request:
    :return:
    """
    name = request.POST.get("name")
    email = request.POST.get("email")
    phone = request.POST.get("phone")
    Member.objects.create(name=name, email=email, phone=phone)
    return JsonResponse({"code": 200}, safe=False)


def modify(request):
    """
    modify member's info.
    :param request:
    :return:
    """
    id = request.POST.get("id")
    name = request.POST.get("name")
    email = request.POST.get("email")
    phone = request.POST.get("phone")
    Member.objects.filter(id=id).update(name=name, email=email, phone=phone)
    return JsonResponse({"code": 200}, safe=False)


def remove(request):
    """
    remove a member.
    :param request:
    :return:
    """
    id = request.POST.get("id")
    Member.objects.filter(id=id).delete()
    return JsonResponse({"code": 200}, safe=False)
