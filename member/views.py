from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from member.models import Member


def index(request):
    return render(request, "member/index.html")


def members(request):
    search_param = request.GET.get("searchParam", None)
    if not search_param:
        result = Member.objects.values().all()
    else:
        result = Member.objects.filter(name__icontains=search_param).values().all()
    return JsonResponse({"code": 200, "records": list(result)}, safe=False)
