from django.urls import path
from . import views

urlpatterns = [
    path('group', views.getGroup),
    path('matches', views.getMatches),
    path('matches/<str:matchid>/', views.getMatchDetail),
    path('', views.getBraketview),
    path('teams', views.getTeam),
    path('stats', views.getStats),
    path('send_data', views.send_gg),
    path('get_data', views.get_request_gg),
]
