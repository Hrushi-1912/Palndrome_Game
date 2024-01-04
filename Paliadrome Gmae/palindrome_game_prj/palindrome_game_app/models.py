from django.db import models

# Create your models here.

class UserProfile(models.Model):
    username = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=30)  

class Game(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    game_id = models.CharField(max_length=30, unique=True)
    string_value = models.CharField(max_length=30)
