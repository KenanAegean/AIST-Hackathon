from .models import Player, MVP, Team
import numpy as np
from sklearn.linear_model import LinearRegression, LogisticRegression

def predict_player_performance(player_name):
    # Retrieve player data from the database
    player = Player.objects.get(Player=player_name)
    
    # Perform some advanced analysis (e.g., use machine learning model to predict performance)
    # For demonstration purposes, let's assume we're using linear regression to predict points scored
    X = np.array(player[['Age', 'G', 'GS', 'MP', 'FG%', '3P%', 'FT%', 'TRB', 'AST', 'STL', 'BLK', 'PTS']])
    y = np.array(player['PTS'])
    
    # Train a linear regression model
    model = LinearRegression()
    model.fit(X, y)
    
    # Make prediction
    predicted_performance = model.predict([X.mean(axis=0)])  # Predict based on average player statistics
    
    return predicted_performance

def compare_players(player_name):
    # Retrieve player data from the database
    player = Player.objects.get(Player=player_name)
    
    # Get MVPs data for comparison
    other_players = MVP.objects.exclude(Player=player_name)
    
    comparison_results = {}
    for other_player in other_players:
        # Perform comparison based on advanced metrics (e.g., Player Efficiency Rating - PER)
        player_stats = np.array(player[['PTS', 'TRB', 'AST', 'STL', 'BLK', 'TOV']])
        other_player_stats = np.array(other_player[['PTS', 'TRB', 'AST', 'STL', 'BLK', 'TOV']])
        
        player_per = np.sum(player_stats) / player['MP']
        other_player_per = np.sum(other_player_stats) / other_player['MP']
        
        comparison_results[other_player.Player] = {
            'player_per': player_per,
            'other_player_per': other_player_per,
            'comparison': 'higher' if player_per > other_player_per else 'lower'
        }
    
    return comparison_results

def predict_match_outcome(team1_name, team2_name):
    # Retrieve team data from the database
    team1 = Team.objects.get(Team=team1_name)
    team2 = Team.objects.get(Team=team2_name)
    
    # Get team statistics
    team1_stats = [team1.WL_percent, team1.PS_per_game, team1.PA_per_game, team1.SRS]
    team2_stats = [team2.WL_percent, team2.PS_per_game, team2.PA_per_game, team2.SRS]
    
    # Perform some advanced analysis (e.g., use logistic regression to predict match outcome)
    # For demonstration purposes, let's assume we're predicting based on team statistics
    X = np.array([team1_stats, team2_stats])
    
    # Train a logistic regression model
    model = LogisticRegression()
    model.fit(X, [1, 0])  # Labels should be passed directly, not in array
    
    # Make prediction
    match_prediction = model.predict_proba(X.mean(axis=0).reshape(1, -1))
    
    return match_prediction

def predict_team_performance(team_name):
    # Retrieve team data from the database
    team = Team.objects.get(Team=team_name)
    
    # Perform some advanced analysis (e.g., use linear regression to predict performance)
    # For demonstration purposes, let's assume we're predicting based on historical team statistics
    X = np.array([team[['Year', 'W/L%', 'PS/G', 'PA/G', 'SRS']]])
    y = np.array(team[['W']])
    
    # Train a linear regression model
    model = LinearRegression()
    model.fit(X, y)
    
    # Make prediction for the next year
    next_year = team['Year'] + 1
    performance_prediction = model.predict([[next_year, team['W/L%'], team['PS/G'], team['PA/G'], team['SRS']]])
    
    return performance_prediction