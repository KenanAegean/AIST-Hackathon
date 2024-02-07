from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('team-analysis/', views.team_based_analysis, name='team_analysis'),
    path('player-analysis/', views.player_based_analysis, name='player_analysis'),
    path('match-analysis/', views.match_analysis, name='match_analysis'),
]
