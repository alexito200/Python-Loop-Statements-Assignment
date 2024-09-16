# Task 1 Your Mood Today
# Write a program that prints off different moods for each day of the week. Use the range() function

import random

moods = ['Happy', 'Sad', 'Energetic', 'Calm']
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

for day in days:
    mood = random.choice(moods)
    print(f"'On {random.choice(days)}, you were feeling {random.choice(moods)}'")