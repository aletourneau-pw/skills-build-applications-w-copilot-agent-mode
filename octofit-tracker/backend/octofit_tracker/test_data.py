# Test data for OctoFit Tracker
# This file contains sample data for users, teams, activities, leaderboard, and workouts collections.

test_data = {
    "users": [
        {"email": "alice@example.com", "name": "Alice", "password": "testpass1"},
        {"email": "bob@example.com", "name": "Bob", "password": "testpass2"},
        {"email": "carol@example.com", "name": "Carol", "password": "testpass3"}
    ],
    "teams": [
        {"name": "Team Alpha", "members": ["alice@example.com", "bob@example.com"]},
        {"name": "Team Beta", "members": ["carol@example.com"]}
    ],
    "activities": [
        {"user": "alice@example.com", "activity_type": "running", "duration": 30, "date": "2025-05-01T10:00:00Z"},
        {"user": "bob@example.com", "activity_type": "walking", "duration": 45, "date": "2025-05-01T11:00:00Z"},
        {"user": "carol@example.com", "activity_type": "cycling", "duration": 60, "date": "2025-05-01T12:00:00Z"}
    ],
    "leaderboard": [
        {"team": "Team Alpha", "points": 100},
        {"team": "Team Beta", "points": 80}
    ],
    "workouts": [
        {"user": "alice@example.com", "workout_type": "strength", "details": "Pushups and squats", "date": "2025-05-01T13:00:00Z"},
        {"user": "bob@example.com", "workout_type": "cardio", "details": "Treadmill", "date": "2025-05-01T14:00:00Z"}
    ]
}
