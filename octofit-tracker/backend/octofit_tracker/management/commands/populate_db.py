from django.core.management.base import BaseCommand
from octofit_tracker.test_data import test_data
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from django.utils.dateparse import parse_datetime

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data.'

    def handle(self, *args, **kwargs):
        # Users
        user_objs = {}
        for user in test_data['users']:
            obj, _ = User.objects.get_or_create(email=user['email'], defaults={
                'name': user['name'],
                'password': user['password']
            })
            user_objs[user['email']] = obj
        # Teams
        team_objs = {}
        for team in test_data['teams']:
            members = [user_objs[email].email for email in team['members'] if email in user_objs]
            obj, _ = Team.objects.get_or_create(name=team['name'], defaults={"members": members})
            if not obj.members:
                obj.members = members
                obj.save()
            team_objs[team['name']] = obj
        # Activities
        for activity in test_data['activities']:
            user = user_objs.get(activity['user'])
            if user:
                Activity.objects.get_or_create(
                    user=user,
                    activity_type=activity['activity_type'],
                    duration=activity['duration'],
                    date=parse_datetime(activity['date'])
                )
        # Leaderboard
        for lb in test_data['leaderboard']:
            team = team_objs.get(lb['team'])
            if team:
                Leaderboard.objects.get_or_create(
                    team=team,
                    points=lb['points']
                )
        # Workouts
        for workout in test_data['workouts']:
            user = user_objs.get(workout['user'])
            if user:
                Workout.objects.get_or_create(
                    user=user,
                    workout_type=workout['workout_type'],
                    details=workout['details'],
                    date=parse_datetime(workout['date'])
                )
        self.stdout.write(self.style.SUCCESS('Test data populated successfully.'))
