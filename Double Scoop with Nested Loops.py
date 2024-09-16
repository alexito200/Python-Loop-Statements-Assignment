# Task 1 Your Mood Tracker
# Simulate a mood tracker that records your mood at three different times of the day (morning, afternoon, evening)
# for each day of the week.

import random

moods = ['Happy', 'Sad', 'Energetic', 'Calm']
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
time_of_days = ['morning', 'afternoon', 'evening']

for day in days:
    for time_of_day in time_of_days:
        print(f"'on {day} {time_of_day} you were feeling {random.choice(moods)}'")