from django.http import JsonResponse
from django.shortcuts import render

from projects.models import Project
# Create your views here.
from projects.models import ProjectTags


def index(request):
    return render(request, 'projects/index.html')


def dashboard(request):
    return render(request, 'projects/dashboard.html')


def analysis(request):
    return render(request, 'projects/analysis.html')


def detail(request):
    return render(request, 'projects/project_detail.html')


def project_task(request):
    return render(request, 'projects/project_task.html')


def tags(request):
    return render(request, 'projects/project_tags.html')


def tags_list(request):
    tag_name = request.GET.get("tag_name")
    result = ProjectTags.objects
    if tag_name:
        result = result.filter(name__icontains=tag_name)
    result = result.values().all()
    return JsonResponse({"code": 200, "records": list(result)}, safe=False)


def tags_add(request):
    name = request.POST.get("name")
    color = request.POST.get("color")
    ProjectTags.objects.create(name=name, color=color)
    return JsonResponse({"code": 200}, safe=False)


def project_list(request):
    project_name = request.GET.get("project_name")
    result = Project.objects
    if project_name:
        result = result.filter(name__icontains=project_name)
    result = result.values().all()
    return JsonResponse({"code": 200, "records": list(result)}, safe=False)


def add(request):
    name = request.POST.get("name")
    remark = request.POST.get("remark")
    Project.objects.create(name=name, remark=remark, company_id=1, status=0)
    return JsonResponse({"code": 200}, safe=False)
