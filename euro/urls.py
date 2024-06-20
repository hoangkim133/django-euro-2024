from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.getGroup),
    path('matches', views.getMatches),
    path('matches/<str:matchid>/', views.getMatchDetail),
    path('braket', views.getBraketview),
    path('teams', views.getTeam),
    path('stats', views.getStats),
] + static(settings.STATIC_ROOT, document_root=settings.STATIC_ROOT)
