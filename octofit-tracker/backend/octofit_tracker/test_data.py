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
        {"user": "alice@example.com", "score": 100},
        {"user": "bob@example.com", "score": 80},
        {"user": "carol@example.com", "score": 90}
    ],
    "workouts": [
        {"name": "Pushups", "description": "Pushups and squats"},
        {"name": "Treadmill", "description": "Treadmill cardio"}
    ]
}
