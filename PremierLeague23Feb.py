class Team:
    def __init__(self, name:str, stadium:str, city:str, ):
        self.name = name
        self.stadium = stadium
        self.city = city

    def __repr__(self):
        return f"{self.name},{self.stadium},{self.city}"


def parseTeamData(data):
    data1 = data.split(":")
    club = data1[0]
    data2 = data1[1].split("-")
    stadium = data2[0]
    area = data2[1]
    return Team(club, stadium, area)


def load_teams_fr_file():
    try:
        teams = []
        my_file = open("epl.txt", "r")
        for line in my_file:
            teams.append(parseTeamData(line))
    except FileNotFoundError:
        print("Please save the file in the project folder!")
    finally:
        my_file.close()
        return teams


ts = load_teams_fr_file()
print(ts)
print()
print()

# Open the text file of top three players
with open('top_players.txt', 'r') as f:
    top_three_data = f.readlines()

# Parse the top three player data and create a list
top_players = [player.strip() for player in top_three_data]


import random

# Define the teams in the Premier League
teams = ["Arsenal", "Aston Villa", "Brentford", "Brighton & Hove Albion",
         "Burnley", "Chelsea", "Crystal Palace", "Everton", "Leeds United",
         "Leicester City", "Liverpool", "Manchester City", "Manchester United",
         "Newcastle United", "Norwich City", "Southampton", "Tottenham Hotspur",
         "Watford", "West Ham United", "Wolverhampton Wanderers"]

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
print("*" * 43)
print("       Premier League Table 2022/23    ")
print("*" * 43)
print("Pos\t Team\t\t           Pt\tW\tD\tL")
for i, team in enumerate(sorted_teams):
    print(f"{i+1}\t{team.ljust(20)}\t{points[team]}\t{wins[team]}\t{draws[team]}\t{losses[team]}")

# Print top players
print("\nThe top three Premier League players this season are:")
for i, player in enumerate(top_players):
    print(f"{i+1}. {player}")


# Ask if the user wants to relegate the bottom team
relegate = input("\nDo you want to relegate the bottom team? (yes/no): ")
if relegate.lower() == "yes":
    bottom_team = sorted_teams[-1]
    print("\n{} has been relegated.".format(bottom_team[0:]))
    sorted_teams = sorted_teams[:-1]

# Print the winner of the season
print("\nThe winner of the 2022/23 season is {}!".format(sorted_teams[0][0:]))
