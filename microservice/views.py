from xml.etree import ElementTree

import requests
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render

from devops.mail import send_mail
from microservice.models import EurekaManager


@login_required
def index(request):
    """
    微服务：服务管理首页，根据 eureka 地址拉取最新的服务信息，其中 eureka 可能无法访问
    :param request:
    :return:
    """
    return render(request, "microservice/index.html")


@login_required
def setting(request):
    """
    微服务：服务管理首页，根据 eureka 地址拉取最新的服务信息，其中 eureka 可能无法访问
    :param request:
    :return:
    """
    return render(request, "microservice/setting.html")


@login_required
def monitor(request):
    """
    微服务：服务管理首页，根据 eureka 地址拉取最新的服务信息，其中 eureka 可能无法访问
    :param request:
    :return:
    """
    return render(request, "microservice/monitor.html")


@login_required
def overview(request):
    eurekas = list(EurekaManager.objects.values().all())

    application_size = 0
    instance_size = 0

    for eureka in eurekas:
        application_request = requests.get(f'{eureka.get("eureka_url")}/eureka/apps')
        if application_request.status_code == 404:
            print("f{eureka.eureka_url}无法访问")
            mail = {
                'subject': f'eureka {eureka.get("app")} 地址无法访问!',
                'content': f'{eureka.get("eureka_url")} 无法访问, 负责人{eureka.get("manager")}'
            }
            send_mail(eureka.get("email"), mail)
            continue
        try:
            root = ElementTree.fromstring(application_request.text)
        except Exception as e:
            mail = {
                'subject': 'eureka 无法正常解析!',
                'content': f'f{eureka.get("eureka_url")}无法访问, 负责人{eureka.get("manager")}'
            }
            send_mail(eureka.get("email"), mail)
            continue
        list_application = root.getiterator("application")

        eureka_application_size = 0
        for application in list_application:
            eureka_application_size = eureka_application_size + 1
            print('\t application:', application.find('name').text)
            instance_list = application.getiterator('instance')
            for instance in instance_list:
                instance_size = instance_size + 1
                # print('\t |- instanceId', instance.find('instanceId').text)
                # print('\t |- hostName', instance.find('hostName').text)
                # print('\t |- app', instance.find('app').text)
                # print('\t |- ipAddr', instance.find('ipAddr').text)
                # print('\t |- status', instance.find('status').text)
                # print('\t |- statusPageUrl', instance.find('statusPageUrl').text)
                # print('\t |- healthCheckUrl', instance.find('healthCheckUrl').text)
        eureka['application_size'] = eureka_application_size
        application_size = application_size + eureka_application_size
    context = {
        "records": eurekas,
        "applications": application_size,
        "instances": instance_size
    }
    return JsonResponse({"code": 200, "records": context}, safe=False)


@login_required
def add(request):
    project_name = request.POST.get("projectName")
    project_url = request.POST.get("projectURL")
    manager = request.POST.get("manager")
    email = request.POST.get("email")

    # 判断该链接是不是euraka链接
    eureka_url = project_url + "/eureka/apps"
    try:
        eureka_request = requests.get(eureka_url)
    except:
        return JsonResponse({"code": 100, "msg": "项目地址访问出现异常"}, safe=False)
    if eureka_request.status_code == 200:
        print(eureka_request.headers)
        if eureka_request.text.startswith("<applications>") and eureka_request.headers:
            apps = list(EurekaManager.objects.filter(eureka_url=project_url).all())
            if apps is not None and len(apps) == 0:
                EurekaManager.objects.create(app=project_name,
                                             eureka_url=project_url,
                                             manager=manager,
                                             email=email)
                mail = {
                    'subject': 'devops添加成功!',
                    'content': f'添加成功 项目名称{project_name} 负责人{manager} 项目地址{eureka_url}'
                }

                send_mail(email, mail)
                return JsonResponse({"code": 200, "msg": "添加成功"}, safe=False)
            return JsonResponse({"code": 100, "msg": "该项目地址已经存在"}, safe=False)
    return JsonResponse({"code": 100, "msg": "项目地址不能访问"}, safe=False)


@login_required
def project_list(request):
    eurekas = list(EurekaManager.objects.all())
    return JsonResponse({"code": 200, "data": eurekas}, safe=False)
