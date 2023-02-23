import itertools
import random

# Define the list of Premier League teams
teams = ["Arsenal", "Aston Villa", "Brentford", "Brighton", "Burnley", "Chelsea",
         "Crystal Palace", "Everton", "Leeds United", "Leicester City", "Liverpool",
         "Manchester City", "Manchester United", "Newcastle United", "Norwich City",
         "Southampton", "Tottenham Hotspur", "Watford", "West Ham United", "Wolverhampton Wanderers"]

# Define the number of rounds in the season
num_rounds = len(teams) - 1

# Generate the schedule for the season using a round-robin algorithm
schedule = []
for i in range(num_rounds):
    # Generate a list of all possible pairings for this round
    pairings = list(itertools.combinations(teams, 2))

    # Shuffle the pairings to randomize the order
    random.shuffle(pairings)

    # Add the pairings to the schedule for this round
    schedule.append(pairings)

    # Rotate the list of teams so that each team plays against a different set of opponents in each round
    teams.append(teams.pop(1))

# Simulate each match in the schedule and keep track of the scores for each team
scores = {}
for round_num, round_schedule in enumerate(schedule):
    print(f"Round {round_num + 1}:")
    for matchup in round_schedule:
        home_team, away_team = matchup
        home_score = 0
        away_score = 0
        # Simulate the match between the two teams using your preferred method
        # For example, you could use a rule-based simulation or a scoring system based on team strength
        # For simplicity, let's assume that each team scores one goal in every match
        home_score += 1
        away_score += 1
        print(f"{home_team} {home_score} - {away_score} {away_team}")

        # Update the scores for each team based on the result of the match
        if home_team not in scores:
            scores[home_team] = 0
        if away_team not in scores:
            scores[away_team] = 0
        if home_score > away_score:
            scores[home_team] += 3
        elif home_score == away_score:
            scores[home_team] += 1
            scores[away_team] += 1
        else:
            scores[away_team] += 3

# Sort the teams by their total scores and print the Premier League table
table = sorted(scores.items(), key=lambda x: x[1], reverse=True)
print("\nPremier League table:")
for i, (team, score) in enumerate(table):
    print(f"{i + 1}. {team}: {score} points")
