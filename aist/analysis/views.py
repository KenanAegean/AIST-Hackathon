from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import MVP, Player, Team
from .utils import predict_player_performance, compare_players, predict_match_outcome, predict_team_performance


def main_page(request):
    return render(request, 'main_page.html')


def player_analysis(request):
    teams = Player.objects.values_list('Tm', flat=True).distinct()  # Fetch distinct teams
    filtered_players = []
    player_details = None
    predicted_performance = None
    comparison_results = None

    if request.method == 'POST':
        team = request.POST.get('team')
        year = request.POST.get('year')

        # Filter players by team and year
        filtered_players = Player.objects.filter(Tm=team, Year=year)

        if 'player_id' in request.POST:
            player_id = request.POST.get('player_id')

            # Get the selected player's details
            selected_player = Player.objects.get(id=player_id)

            # Predict player performance
            predicted_performance = predict_player_performance(player_id)

            # Compare players
            comparison_results = compare_players(player_id)

            player_details = selected_player

    return render(request, 'player_based_analysis.html', {
        'teams': teams,
        'filtered_players': filtered_players,
        'player_details': player_details,
        'predicted_performance': predicted_performance,
        'comparison_results': comparison_results,
    })

def match_analysis(request):
    teams = Team.objects.all()
    match_prediction = None
    
    if request.method == 'POST':
        team1_name = request.POST.get('team1')
        team2_name = request.POST.get('team2')
        
        dummy = Team.objects.all()

        # Predict match outcome
        match_prediction = predict_match_outcome(team1_name, team2_name)
        
        # Extract relevant information from prediction probabilities
        probability_team1_win = match_prediction[0][1]
        probability_team2_win = match_prediction[0][0]
        probability_team1_win_hundered = probability_team1_win * 100
        probability_team2_win_hundered = probability_team2_win * 100
        
        # Pass relevant information to the template
        return render(request, 'match_analysis.html', {
            'dummy': dummy,
            'teams': teams,
            'team1_name': team1_name,
            'team2_name': team2_name,
            'match_prediction': match_prediction,
            'probability_team1_win': probability_team1_win,
            'probability_team2_win': probability_team2_win,
            'probability_team1_win_hundered': probability_team1_win_hundered,
            'probability_team2_win_hundered': probability_team2_win_hundered,
        })
    
    return render(request, 'match_analysis.html', {'teams': teams, 'match_prediction': match_prediction})

def team_analysis(request):
    teams = Team.objects.all()
    
    if request.method == 'POST':
        team_name = request.POST.get('team_name')
        
        # Predict team performance
        performance_prediction = predict_team_performance(team_name)
        
        return render(request, 'team_based_analysis.html', {
            'teams': teams,
            'team_name': team_name,
            'performance_prediction': performance_prediction
        })
    
    return render(request, 'team_based_analysis.html', {'teams': teams})

def dummy(request):
    return render(request, 'dummy.html')