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

def match_analysis(request):
    teams = Team.objects.all()

    selected_home_team = request.GET.get('team', '')
    selected_guest_team = request.GET.get('team', '')

    if not teams.count == 0 or not teams:
        # Handle the case when the database is empty
        teams = []

    selected_home_team_data = None
    selected_guest_team_data = None

    try:
        selected_home_team_int = int(selected_home_team)
        selected_guest_team_int = int(selected_guest_team)
        selected_home_team_data = Team.objects.get(id=selected_home_team_int)
        selected_guest_team_data = Team.objects.get(id=selected_guest_team_int)
    except ValueError:
        pass
    
    # Your analysis logic here 

    return render(request, 'match_analysis.html', {
        'teams': teams,
        'selected_home_team': selected_home_team,
        'selected_guest_team': selected_guest_team,
        'selected_home_team_data': selected_home_team_data,
        'selected_guest_team_data': selected_guest_team_data,
    })