from django.shortcuts import render
from .models import MVP, Player, Team
from .utils import predict_player_performance, compare_players, predict_match_outcome

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

def match_analysis_old(request):
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


def player_analysis(request):
    if request.method == 'POST':
        player_name = request.POST.get('player_name')
        
        # Predict player performance
        predicted_performance = predict_player_performance(player_name)
        
        # Compare players
        comparison_results = compare_players(player_name)
        
        # Retrieve additional player details for display
        player_details = Player.objects.get(Player=player_name)
        
        return render(request, 'player_based_analysis.html', {
            'player_name': player_name,
            'predicted_performance': predicted_performance,
            'comparison_results': comparison_results,
            'player_details': player_details
        })
    return render(request, 'player_based_analysis.html')

def match_analysis(request):
    teams = Team.objects.all()
    
    if request.method == 'POST':
        team1_name = request.POST.get('team1')
        team2_name = request.POST.get('team2')
        
        # Predict match outcome
        match_prediction = predict_match_outcome(team1_name, team2_name)
        
        return render(request, 'match_analysis.html', {
            'teams': teams,
            'team1_name': team1_name,
            'team2_name': team2_name,
            'match_prediction': match_prediction
        })
    
    return render(request, 'match_analysis.html', {'teams': teams})