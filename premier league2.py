import random
from collections import defaultdict

# Define the teams in the Premier League
teams = ["Arsenal", "Aston Villa", "Brentford", "Brighton & Hove Albion", "Burnley", "Chelsea", "Crystal Palace",
         "Everton", "Leeds United", "Leicester City", "Liverpool", "Manchester City", "Manchester United",
         "Newcastle United", "Norwich City", "Southampton", "Tottenham Hotspur", "Watford", "West Ham United",
         "Wolverhampton Wanderers"]

# Define the number of matches in a season
num_matches = 38

# Initialize the points, wins, draws, losses, goals scored, and goals conceded for each team
points = defaultdict(int)
wins = defaultdict(int)
draws = defaultdict(int)
losses = defaultdict(int)
goals_for = defaultdict(int)
goals_against = defaultdict(int)

# Simulate the matches
for i in range(num_matches):
    # Shuffle the teams to simulate a random match order
    random.shuffle(teams)

    # Keep track of the top scorer for each match
    top_scorer = ("", 0)

    for j in range(0, len(teams), 2):
        home_team = teams[j]
        away_team = teams[j + 1]

        # Generate a random score for the home team and the away team
        home_score = random.randint(0, 4)
        away_score = random.randint(0, 4)

        # Update the points, wins, draws, losses, goals scored, and goals conceded variables for each team
        points[home_team] += 3 if home_score > away_score else 1 if home_score == away_score else 0
        points[away_team] += 3 if away_score > home_score else 1 if away_score == home_score else 0
        wins[home_team] += 1 if home_score > away_score else 0
        wins[away_team] += 1 if away_score > home_score else 0
        draws[home_team] += 1 if home_score == away_score else 0
        draws[away_team] += 1 if away_score == home_score else 0
        losses[home_team] += 1 if home_score < away_score else 0
        losses[away_team] += 1 if away_score < home_score else 0
        goals_for[home_team] += home_score
        goals_for[away_team] += away_score
        goals_against[home_team] += away_score
        goals_against[away_team] += home_score

        # Update the top scorer if a player scored more goals than the previous top scorer
        if home_score > top_scorer[1]:
            top_scorer = (home_team, home_score)
        if away_score > top_scorer[1]:
            top_scorer = (away_team, away_score)

        print(
            f"{home_team} {home_score} - {away_score} {away_team}: {top_scorer[0]} "
            f"is the top scorer with {top_scorer[1]} goals")

# Sort the teams by their points, wins, and goal difference
sorted_teams = sorted(teams, key=lambda x: (points[x], wins[x], goals_for[x] - goals_against[x]), reverse=True)

# Relegate the bottom team
relegated_team = sorted_teams
