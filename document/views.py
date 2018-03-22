from django.shortcuts import render


# Create your views here.


def index(request):
    return render(request, 'document/index.html')


def detail(request):
    return render(request, 'document/document_detail.html')


def write(request):
    return render(request, 'document/full.html')
