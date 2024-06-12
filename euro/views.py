from django.shortcuts import render
from django.http import HttpResponse
from . import service

# Create your views here.


def getGroup(request):
    groups = service.getEuroGroup()

    return render(request, 'group.html', {'groups': groups})


def getMatches(request):
    matches = service.getEuroMatches()
    print(matches[0].get("kickOffTime").get("dateTime"))
    for match in matches:
        value = service.convert_time_between_offsets(
            match.get("kickOffTime").get("dateTime"))
        match["kickOffTime"]["dateTime"] = value.strftime("%a, %B %d")
        match["kickOffTime"]["time"] = value.strftime("%H:%M")

    return render(request, 'matches.html', {'matches': matches})
