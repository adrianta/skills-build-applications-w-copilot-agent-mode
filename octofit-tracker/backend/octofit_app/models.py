
from django.db import models

# MongoDB models for users, teams, activity, leaderboard, and workouts
class User(models.Model):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=128)

class Team(models.Model):
    name = models.CharField(max_length=100)
    members = models.JSONField(default=list)  # List of user IDs

class Activity(models.Model):
    user_id = models.CharField(max_length=100)
    activity_type = models.CharField(max_length=100)
    duration = models.IntegerField()
    date = models.DateField()

class Leaderboard(models.Model):
    user_id = models.CharField(max_length=100)
    score = models.IntegerField()

class Workout(models.Model):
    user_id = models.CharField(max_length=100)
    workout_type = models.CharField(max_length=100)
    details = models.TextField()
    date = models.DateField()
