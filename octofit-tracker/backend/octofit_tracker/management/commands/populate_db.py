from django.core.management.base import BaseCommand
from octofit_app.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data.'

    def handle(self, *args, **kwargs):
        # Users
        user1 = User.objects.create(email='alice@example.com', name='Alice', password='alicepass')
        user2 = User.objects.create(email='bob@example.com', name='Bob', password='bobpass')
        user3 = User.objects.create(email='carol@example.com', name='Carol', password='carolpass')

        # Teams
        team1 = Team.objects.create(name='Team Alpha', members=[user1.id, user2.id])
        team2 = Team.objects.create(name='Team Beta', members=[user3.id])

        # Activities
        Activity.objects.create(user_id=user1.id, activity_type='run', duration=30, date='2025-05-01')
        Activity.objects.create(user_id=user2.id, activity_type='walk', duration=60, date='2025-05-02')
        Activity.objects.create(user_id=user3.id, activity_type='cycle', duration=45, date='2025-05-03')

        # Leaderboard
        Leaderboard.objects.create(user_id=user1.id, score=100)
        Leaderboard.objects.create(user_id=user2.id, score=80)
        Leaderboard.objects.create(user_id=user3.id, score=120)

        # Workouts
        Workout.objects.create(user_id=user1.id, workout_type='cardio', details='30 min run', date='2025-05-01')
        Workout.objects.create(user_id=user2.id, workout_type='strength', details='pushups and squats', date='2025-05-02')
        Workout.objects.create(user_id=user3.id, workout_type='yoga', details='morning yoga routine', date='2025-05-03')

        self.stdout.write(self.style.SUCCESS('Test data populated successfully.'))
