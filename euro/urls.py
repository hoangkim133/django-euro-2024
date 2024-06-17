from django.urls import path
from . import views

urlpatterns = [
    path('', views.getGroup),
    path('matches', views.getMatches),
    path('braket', views.getBraketview),
    path('teams', views.getTeam),
    path('stats', views.getStats),
]
