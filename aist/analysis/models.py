from django.db import models

class MVP(models.Model):
    name = models.CharField(max_length=100)
    year = models.IntegerField()
    team = models.ForeignKey('Team', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    class Meta:
        app_label = 'analysis'

class Player(models.Model):
    name = models.CharField(max_length=100)
    team = models.ForeignKey('Team', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    class Meta:
        app_label = 'analysis'

class Team(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    class Meta:
        app_label = 'analysis'
