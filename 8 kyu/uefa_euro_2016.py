def uefa_euro_2016(teams, scores):
    first, second = teams
    if scores[0] > scores[1]:
        winner = first + " won!"
    elif scores[0] < scores[1]:
        winner = second + " won!"
    else:
        winner = "teams played draw."
    return f"At match {first} - {second}, {winner}" 
        
