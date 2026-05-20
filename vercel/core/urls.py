from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('roster/', views.roster, name='roster'),
    path('history/', views.history, name='history'),
    path('arena/', views.arena, name='arena'),
]
