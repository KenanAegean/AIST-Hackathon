from django.contrib import admin
from .models import MVP, Player, Team

@admin.register(MVP)
class MVPAdmin(admin.ModelAdmin):
    list_display = ('id', 'Player', 'Rank', 'Age', 'Tm', 'First', 'Pts_Won', 'Pts_Max', 'Share', 'G', 'MP', 'PTS', 'TRB', 'AST', 'STL', 'BLK', 'FG_percent', 'ThreeP_percent', 'FT_percent', 'WS', 'WS_per_48', 'Year')

@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ('id', 'Player', 'Rk', 'Pos', 'Age', 'Tm', 'G', 'GS', 'MP', 'FG', 'FGA', 'FG_percent', 'ThreeP', 'ThreePA', 'ThreeP_percent', 'TwoP', 'TwoPA', 'TwoP_percent', 'eFG_percent', 'FT', 'FTA', 'FT_percent', 'ORB', 'DRB', 'TRB', 'AST', 'STL', 'BLK', 'TOV', 'PF', 'PTS', 'Year')

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('id', 'Team', 'W', 'L', 'WL_percent', 'GB', 'PS_per_game', 'PA_per_game', 'SRS', 'Year')
