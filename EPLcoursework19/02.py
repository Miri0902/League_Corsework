import random

# Open the text file of Premier League teams
with open("epl1.txt", "r") as f:
    team_data = f.readlines()

# Parse the team data and create a list of dictionaries
teams = []
for team in team_data:
    team_info = team.strip().split(',')
    teams.append({
        'name': team_info[0],
        'home_ground': team_info[1],
        'city': team_info[2],
        'manager': team_info[3]
    })

# Open the text file of top three players
with open('top_three_players.txt', 'r') as f:
    top_three_data = f.readlines()

# Parse the top three player data and create a list
top_three_players = [player.strip() for player in top_three_data]

# Simulate matches
for team in teams:
    team['points'] = 0
    team['goal_difference'] = 0
    team['goals_for'] = 0
    team['goals_against'] = 0

for i in range(len(teams)):
    for j in range(i + 1, len(teams)):
        home_team = teams[i]
        away_team = teams[j]
        home_goals = random.randint(0, 5)
        away_goals = random.randint(0, 5)

        home_team['goals_for'] += home_goals
        away_team['goals_for'] += away_goals
        home_team['goals_against'] += away_goals
        away_team['goals_against'] += home_goals
        home_team['goal_difference'] += home_goals - away_goals
        away_team['goal_difference'] += away_goals - home_goals

        if home_goals > away_goals:
            home_team['points'] += 3
        elif home_goals == away_goals:
            home_team['points'] += 1
            away_team['points'] += 1
        else:
            away_team['points'] += 3

# Sort the teams by points, goal difference, goals for, and team name
sorted_teams = sorted(teams, key=lambda t: (-t['points'], -t['goal_difference'], -t['goals_for'], t['name']))

# Print the league table
print("Final League Table:\n")
print("{:<4} {:<20} {:<10} {:<10} {:<10} {:<10}".format("POS", "TEAM", "PTS", "GF", "GA", "GD"))
for i, team in enumerate(sorted_teams):
    print("{:<4} {:<20} {:<10} {:<10} {:<10} {:<10}".format(i+1, team['name'], team['points'], team['goals_for'], team['goals_against'], team['goal_difference']))

# Ask if the user wants to relegate the bottom team
relegate = input("\nDo you want to relegate the bottom team? (yes/no): ")
if relegate.lower() == "yes":
    bottom_team = sorted_teams[-1]
    print("\n{} has been relegated.".format(bottom_team['name']))
    sorted_teams = sorted_teams[:-1]

# Print the winner of the season
print("\nThe winner of the 2022/23 season is {}!".format(sorted_teams[0]['name']))


