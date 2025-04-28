from django.shortcuts import render
from django.http import HttpResponse

from .models import Service, Category


# Create your views here.
def index(request):
    list_service = Service.objects.all()

    context = {
        "title": "BlueZapus",
        "service": list_service,
    }

    return render(request, "service/index.html", context)


def detail(request, slug_serv):
    detail_serv = Service.objects.get(slug_serv=slug_serv)
    context = {
        "title": "BlueZapus",
        "detail_serv": detail_serv,
    }

    return render(request, "service/detail.html", context)
