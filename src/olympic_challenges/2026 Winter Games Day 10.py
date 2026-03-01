** start of main.py **

def get_hill_rating(drop, distance, hill_type):

    stepness = drop / distance
    if hill_type == 'Downhill':
        adj_stepness = stepness * 1.2
    elif hill_type == 'Slalom':
        adj_stepness = stepness * 0.9
    else:
        adj_stepness = stepness * 1.0

    if adj_stepness <= 0.1:
        return "Green"
    elif adj_stepness <= 0.25:
        return "Blue"
    else:
        return "Black"
    

** end of main.py **

