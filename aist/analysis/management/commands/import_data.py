# management/commands/import_data.py
import csv
from django.core.management.base import BaseCommand
from analysis.models import MVP, Player, Team

class Command(BaseCommand):
    help = 'Import data from CSV files'

    def add_arguments(self, parser):
        parser.add_argument('mvps_csv', type=str)
        parser.add_argument('players_csv', type=str)
        parser.add_argument('teams_csv', type=str)

    def handle(self, *args, **kwargs):
        mvps_csv = kwargs['mvps_csv']
        players_csv = kwargs['players_csv']
        teams_csv = kwargs['teams_csv']

        model_default_values = {
            'MVP': {
                'Rank': 'Rank',
                'Player': 'Unknown Player',
                'Age': 0,
                'Tm': 'Unknown Team',
                'First': 0,
                'Pts_Won': 0,
                'Pts_Max': 0,
                'Share': 0.0,
                'G': 0,
                'MP': 0.0,
                'PTS': 0.0,
                'TRB': 0.0,
                'AST': 0.0,
                'STL': 0.0,
                'BLK': 0.0,
                'FG_percent': 0.0,
                'ThreeP_percent': 0.0,
                'FT_percent': 0.0,
                'WS': 0.0,
                'WS_per_48': 0.0,
                'Year': 0
            },
            'Player': {
                'Rk': 0,
                'Player': 'Unknown Player',
                'Pos': 'Unknown',
                'Age': 0,
                'Tm': 'Unknown Team',
                'G': 0,
                'GS': 0,
                'MP': 0.0,
                'FG': 0.0,
                'FGA': 0.0,
                'FG_percent': 0.0,
                'ThreeP': 0.0,
                'ThreePA': 0.0,
                'ThreeP_percent': 0.0,
                'TwoP': 0.0,
                'TwoPA': 0.0,
                'TwoP_percent': 0.0,
                'eFG_percent': 0.0,
                'FT': 0.0,
                'FTA': 0.0,
                'FT_percent': 0.0,
                'ORB': 0.0,
                'DRB': 0.0,
                'TRB': 0.0,
                'AST': 0.0,
                'STL': 0.0,
                'BLK': 0.0,
                'TOV': 0.0,
                'PF': 0.0,
                'PTS': 0.0,
                'Year': 0
            },
            'Team': {
                'Team': 'Unknown Team',
                'W': 0,
                'L': 0,
                'WL_percent': 0.0,
                'GB': 0.0,
                'PS_per_game': 0.0,
                'PA_per_game': 0.0,
                'SRS': 0.0,
                'Year': 0
            }
        }

        # Import data for MVP model
        with open(mvps_csv, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            next(reader)  # Skip header row
            for row in reader:
                try:
                    MVP.objects.create(
                        **{field.name: row[i] if row[i] else model_default_values['MVP'][field.name] for i, field in enumerate(MVP._meta.get_fields()) if field.name != 'id'}
                    )
                except ValueError as e:
                    self.stderr.write(f'Error in row {row}: {e}')

        # Import data for Player model
        with open(players_csv, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            next(reader)  # Skip header row
            for row in reader:
                try:
                    Player.objects.create(
                        **{field.name: row[i] if row[i] else model_default_values['Player'][field.name] for i, field in enumerate(Player._meta.get_fields()) if field.name != 'id'}
                    )
                except ValueError as e:
                    self.stderr.write(f'Error in row {row}: {e}')

        # Import data for Team model
        with open(teams_csv, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            for row in reader:
                try:
                    Team.objects.create(
                        **{field.name: row[i] if row[i] else model_default_values['Team'][field.name] for i, field in enumerate(Team._meta.get_fields()) if field.name != 'id'}
                    )
                except ValueError as e:
                    self.stderr.write(f'Error in row {row}: {e}')

        self.stdout.write(self.style.SUCCESS('Data imported successfully'))
