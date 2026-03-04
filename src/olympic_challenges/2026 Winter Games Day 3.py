** start of main.py **

def calculate_penalty_distance(rounds):
    total_missed = sum(5 - hits for hits in rounds)
    return total_missed * 150

** end of main.py **

