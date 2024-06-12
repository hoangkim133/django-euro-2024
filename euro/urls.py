from django.urls import path
from . import views

urlpatterns = [
    path('', views.getGroup),
    path('matches', views.getMatches),
]
