from django.shortcuts import render
from django.http import HttpResponse
from . import service

# Create your views here.


def getGroup(request):
    groups = service.getEuroGroup()

    return render(request, 'group.html', {'groups': groups})
