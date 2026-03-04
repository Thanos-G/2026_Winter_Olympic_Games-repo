# 2026 Winter Olympic Games - Daily Challenges Python

FreeCodeCamp Olympic Winter Games challenges

#
Day 3: Given an array of integers, where each value represents the number of targets hit in a single round of a biathlon, return the total penalty distance the athlete must ski.

Each round consists of 5 targets.
Each missed target results in a 150 meter penalty loop.
#
Day 6: Given an array of judge scores and optional penalties, calculate the final score for a figure skating routine.

The first argument is an array of 10 judge scores, each a number from 0 to 10. Remove the highest and lowest judge scores and sum the remaining 8 scores to get the base score.

Any additional arguments passed to the function are penalties. Subtract all penalties from the base score to get the final score.
#
Day 7: Given two arrays representing the lap times (in seconds) for two speed skaters, return the lap number where the difference in lap times is the largest.

The first element of each array corresponds to lap 1, the second to lap 2, and so on.
#
Day 10: Given a ski hill's vertical drop, horizontal distance, and type, determine the difficulty rating of the hill.

To determine the rating:

Calculate the steepness of the hill by taking the drop divided by the distance.
Then, calculate the adjusted steepness based on the hill type:
"Downhill" multiply steepness by 1.2,
"Slalom": multiply steepness by 0.9,
"Giant Slalom": multiply steepness by 1.0

Return:
"Green" if the adjusted steepness is less than or equal to 0.1,
"Blue" if the adjusted steepness is greater than 0.1 and less than or equal to 0.25,
"Black" if the adjusted steepness is greater than 0.25
#
Day 14: Given the snow depth and slope of a mountain, determine if there's an avalanche risk.

The snow depth values are "Shallow", "Moderate", or "Deep".
Slope values are "Gentle", "Steep", or "Very Steep".

Return "Safe" or "Risky" based on this table:
|                  | "Shallow" | "Moderate" | "Deep"  |
|------------------|:---------:|:----------:|:-------:|
| "Gentle"         | Safe      | Safe       | Safe    |
| "Steep"          | Safe      | Risky      | Risky   |
| "Very Steep"     | Safe      | Risky      | Risky   |
#
Day 15: Given a trick name consisting of two words, determine if it is a valid freestyle skiing trick name.

A trick is valid if the first word is in the list of valid first words, and the second word is in the list of valid second words.

The two words will be separated by a single space.
Valid first words: ["Misty", "Ghost", "Thunder", "Solar", "Sky", "Phantom", "Frozen", "Polar"]
Valid second words: ["Twister", "Icequake", "Avalanche", "Vortex", "Snowstorm", "Frostbite", "Blizzard", "Shadow"]
