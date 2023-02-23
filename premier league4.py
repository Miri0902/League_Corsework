import random
from collections import defaultdict

# Read in the Premier League teams from a text file
with open("epl.txt", "r") as f:
    teams = [team.strip() for team in f.readlines()]

# Define the number of matches in a season
num_matches = 38

# Initialize the points, wins, draws, losses, goals scored, and goals conceded for each team
points = defaultdict(int)
wins = defaultdict(int)
draws = defaultdict(int)
losses = defaultdict(int)
goals_for = defaultdict(int)
goals_against = defaultdict(int)

# Initialize the list of players for each team
players = defaultdict(list)

# Simulate the matches
for i in range(num_matches):
    # Shuffle the teams to simulate a random match order
    random.shuffle(teams)

    # Keep track of the man of the match for each match
    man_of_match = ""

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

        # Pick a man of the match for the home team and the away team
        home_player = random.choice(players[home_team]) if players[home_team] else ""
        away_player = random.choice(players[away_team]) if players[away_team] else ""
        if home_score > away_score:
            man_of_match = home_player
        elif home_score < away_score:
            man_of_match = away_player
        else:
            man_of_match = "No man of the match"

        # Print the match result and the man of the match
        print(f"{home_team} {home_score} - {away_score} {away_team}: {man_of_match} is the man of the match")

    # Sort the teams by points, goal difference, and goals scored to generate the league table
    league_table = sorted(teams,
                          key=lambda team: (-points[team], goals_for[team] - goals_against[team], goals_for[team]),
                          reverse=True)

    # Print the league table

