from django.shortcuts import render
from .models import MVP, Player, Team

def main_page(request):
    return render(request, 'main_page.html')

def team_based_analysis(request):
    teams = Team.objects.all()
    years = MVP.objects.values_list('year', flat=True).distinct()

    selected_team = request.GET.get('team', '')
    selected_year = request.GET.get('year', '')

    if not teams.exists() or not years:
        # Handle the case when the database is empty
        teams = []
        years = []

    selected_team_data = None
    selected_year_data = None

    try:
        selected_team_int = int(selected_team)
        selected_year_int = int(selected_year)

        selected_team_data = Team.objects.get(id=selected_team_int)
        selected_year_data = selected_year_int if selected_year_int in years else years[0]
    except ValueError:
        pass

    # Your analysis logic here based on selected_team_data and selected_year_data

    return render(request, 'team_based_analysis.html', {
        'teams': teams,
        'years': years,
        'selected_team': selected_team,
        'selected_year': selected_year,
        'selected_team_data': selected_team_data,
        'selected_year_data': selected_year_data,
    })

def player_based_analysis(request):
    teams = Team.objects.all()
    years = MVP.objects.values_list('year', flat=True).distinct()

    selected_team = request.GET.get('team', '')
    selected_year = request.GET.get('year', '')

    if not teams.exists() or not years:
        # Handle the case when the database is empty
        teams = []
        years = []

    selected_team_data = None
    selected_year_data = None

    try:
        selected_team_int = int(selected_team)
        selected_year_int = int(selected_year)

        selected_team_data = Team.objects.get(id=selected_team_int)
        selected_year_data = selected_year_int if selected_year_int in years else years[0]
    except ValueError:
        pass

    players = Player.objects.none()  # Empty queryset by default
    if selected_team_data and selected_year_data:
        players = Player.objects.filter(team=selected_team_data, mvp__year=selected_year_data)

    return render(request, 'player_based_analysis.html', {
        'teams': teams,
        'years': years,
        'players': players,
        'selected_team': selected_team,
        'selected_year': selected_year,
        'selected_team_data': selected_team_data,
        'selected_year_data': selected_year_data,
    })