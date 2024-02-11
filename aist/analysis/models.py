from django.db import models

class MVP(models.Model):
    id = models.AutoField(primary_key=True)
    Rank = models.CharField(max_length=10, default='Rank')
    Player = models.CharField(max_length=100, default='Unknown Player')
    Age = models.FloatField(default=0.0)
    Tm = models.CharField(max_length=100, default='Unknown Team')
    First = models.FloatField(default=0.0)
    Pts_Won = models.FloatField(default=0.0)
    Pts_Max = models.FloatField(default=0.0)
    Share = models.FloatField(default=0.0)
    G = models.FloatField(default=0.0)
    MP = models.FloatField(default=0.0)
    PTS = models.FloatField(default=0.0)
    TRB = models.FloatField(default=0.0)
    AST = models.FloatField(default=0.0)
    STL = models.FloatField(default=0.0)
    BLK = models.FloatField(default=0.0)
    FG_percent = models.FloatField(default=0.0)
    ThreeP_percent = models.FloatField(default=0.0)
    FT_percent = models.FloatField(default=0.0)
    WS = models.FloatField(default=0.0)
    WS_per_48 = models.FloatField(default=0.0)
    Year = models.FloatField(default=0.0)

    def __str__(self):
        return self.Player
    
    class Meta:
        app_label = 'analysis'

class Player(models.Model):
    id = models.AutoField(primary_key=True)
    Rk = models.FloatField(default=0.0)
    Player = models.CharField(max_length=100, default='Unknown Player')
    Pos = models.CharField(max_length=50, default='Unknown')
    Age = models.FloatField(default=0.0)
    Tm = models.CharField(max_length=100, default='Unknown Team')
    G = models.FloatField(default=0.0)
    GS = models.FloatField(default=0.0)
    MP = models.FloatField(default=0.0)
    FG = models.FloatField(default=0.0)
    FGA = models.FloatField(default=0.0)
    FG_percent = models.FloatField(default=0.0)
    ThreeP = models.FloatField(default=0.0)
    ThreePA = models.FloatField(default=0.0)
    ThreeP_percent = models.FloatField(default=0.0)
    TwoP = models.FloatField(default=0.0)
    TwoPA = models.FloatField(default=0.0)
    TwoP_percent = models.FloatField(default=0.0)
    eFG_percent = models.FloatField(default=0.0)
    FT = models.FloatField(default=0.0)
    FTA = models.FloatField(default=0.0)
    FT_percent = models.FloatField(default=0.0)
    ORB = models.FloatField(default=0.0)
    DRB = models.FloatField(default=0.0)
    TRB = models.FloatField(default=0.0)
    AST = models.FloatField(default=0.0)
    STL = models.FloatField(default=0.0)
    BLK = models.FloatField(default=0.0)
    TOV = models.FloatField(default=0.0)
    PF = models.FloatField(default=0.0)
    PTS = models.FloatField(default=0.0)
    Year = models.FloatField(default=0.0)

    def __str__(self):
        return self.Player
    
    class Meta:
        app_label = 'analysis'

class Team(models.Model):
    id = models.AutoField(primary_key=True)
    Team = models.CharField(max_length=100, default='Unknown Team')
    W = models.FloatField(default=0.0)
    L = models.FloatField(default=0.0)
    WL_percent = models.FloatField(default=0.0)
    GB = models.FloatField(default=0.0)
    PS_per_game = models.FloatField(default=0.0)
    PA_per_game = models.FloatField(default=0.0)
    SRS = models.FloatField(default=0.0)
    Year = models.FloatField(default=0.0)

    def __str__(self):
        return self.Team
    
    class Meta:
        app_label = 'analysis'

