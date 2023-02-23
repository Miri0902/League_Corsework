import random

# Define the teams in the Premier League
teams = ["Arsenal", "Aston Villa", "Brentford", "Brighton & Hove Albion", "Burnley", "Chelsea", "Crystal Palace", "Everton", "Leeds United", "Leicester City", "Liverpool", "Manchester City", "Manchester United", "Newcastle United", "Norwich City", "Southampton", "Tottenham Hotspur", "Watford", "West Ham United", "Wolverhampton Wanderers"]

# Define the number of matches in a season
num_matches = 38

# Initialize the points, wins, draws, and losses for each team
points = {team: 0 for team in teams}
wins = {team: 0 for team in teams}
draws = {team: 0 for team in teams}
losses = {team: 0 for team in teams}

# Simulate the matches
for i in range(num_matches):
    random.shuffle(teams)  # Shuffle the teams to simulate a random match order
    for j in range(0, len(teams), 2):
        home_team = teams[j]
        away_team = teams[j+1]
        home_score = random.randint(0, 4)
        away_score = random.randint(0, 4)
        if home_score > away_score:
            points[home_team] += 3
            wins[home_team] += 1
            losses[away_team] += 1
        elif home_score < away_score:
            points[away_team] += 3
            wins[away_team] += 1
            losses[home_team] += 1
        else:
            points[home_team] += 1
            points[away_team] += 1
            draws[home_team] += 1
            draws[away_team] += 1

# Sort the teams by their points, wins, and goal difference
sorted_teams = sorted(teams, key=lambda x: (points[x], wins[x], points[x]-wins[x]), reverse=True)

# Print the final league table
print("       Premier League Table 2022/23    ")
print("*" * 43)
print("Pos\t Team\t\t          Pt\t W\t D\t L")
for i, team in enumerate(sorted_teams):
    print(f"{i+1}\t{team.ljust(20)}\t{points[team]}\t{wins[team]}\t{draws[team]}\t{losses[team]}")
