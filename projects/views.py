from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'projects/index.html')


def detail(request):
    return render(request, 'projects/project_detail.html')
