class Team:
    """
    This is a class Team from epl.txt
    """

    def __init__(self, name: str, stadium: str, city: str):
        """
     Team constructor
     :param name:  name of the football team
     :param stadium: teams home ground
     :param city: team's home city
     """
        self.name = name
        self.stadium = stadium
        self.city = city

    def __repr__(self):
        """
        :return: this function creates a list containing the teams' details
        """
        return f"{self.name},{self.stadium},{self.city}"


def parseTeamData(data):
    """
    This function will sort class Team's data and split itT
    :param data:
    :return: will return sorted class Team list
    """
    data1 = data.split(":")
    team = data1[0]
    data2 = data1[1].split("-")
    stadium = data2[0]
    area = data2[1]
    return Team(team, stadium, area)


def load_teams_fr_file():
    try:
        teams = []
        with open("epl.txt", "r") as my_file:
            for line in my_file:
                teams.append(parseTeamData(line))
    except FileNotFoundError:
        print("Please save the file!")
    except Exception as e:
        print("There was an error reading file:", e)
    else:
        return teams
    finally:
        my_file.close()
        return teams


ts = load_teams_fr_file()
print(" WELCOME TO THE ENGLISH PREMIER LEAGUE 2022/23 SEASON")
print("=" * 55)
print("\t\t" + "\t" + "The EPL teams:")
print("")
print("\t\t" + "=" * 10 + "*" * 8)
print("")

print("")
print(ts)
print("")
print("=" * 43)

print("  Premier League Clubs and their manager:")
print("=" * 43)
print("  CLUB\t                     MANAGER\t\t")
print("")


class Managers:

    def __init__(self, club: str, manager: str):
        self.club = club
        self.manager = manager

    def __repr__(self):
        return f"{self.club}, {self.manager}"


def parseManagersData(data):
    data1 = data.split(":")
    club = data1[0]
    manager = data1[1]
    return Managers(club, manager)


def load_managers_fr_file():
    try:
        managers = []
        with open("epl.managers.txt", "r") as my_file:
            for line in my_file:
                managers.append(parseManagersData(line))
    except FileNotFoundError:
        print("File is not found!")
    except Exception as e:
        print("There was an error reading file:", e)
    else:
        return managers
    finally:
        my_file.close()


mg = load_managers_fr_file()

if mg:
    for m in mg:
        print(f"{m.club.ljust(25)}\t{m.manager}", end='')  # I have used the end= as this was printing empty line
        # between rows

# Open the text file of top three players
with open("top_players.txt", "r") as f:
    top_three_data = f.readlines()

# Parse the top three player data and create a list
top_players = [player.strip() for player in top_three_data]

# This imports random module, which provides functions for generating random numbers
import random

# Read team names from file
with open('epl.txt') as f:
    teams = [line.strip() for line in f]

# Define constants
NUM_MATCHES = 38
WIN_POINTS = 3
DRAW_POINTS = 1

# Initialize dictionaries to keep track of points, wins, draws, and losses
points = {team: 0 for team in teams}
wins = {team: 0 for team in teams}
draws = {team: 0 for team in teams}
losses = {team: 0 for team in teams}

# Simulate matches
for i in range(NUM_MATCHES):
    for home_team in teams:
        away_team = random.choice(teams)
        while away_team == home_team:
            away_team = random.choice(teams)
        home_score = random.randint(0, 4)
        away_score = random.randint(0, 4)
        if home_score > away_score:
            points[home_team] += WIN_POINTS
            wins[home_team] += 1
            losses[away_team] += 1
        elif home_score < away_score:
            points[away_team] += WIN_POINTS
            wins[away_team] += 1
            losses[home_team] += 1
        else:
            points[home_team] += DRAW_POINTS
            points[away_team] += DRAW_POINTS
            draws[home_team] += 1
            draws[away_team] += 1

# Sort teams based on points
sorted_teams = sorted(teams, key=lambda x: (-points[x], -wins[x], -draws[x], x))

# Print the final league table
print(f"\n{'=' * 55}\n\t\t{'Premier League Table 2022/23':^43}\n{'=' * 55}\n")

print("Pos\t Team\t\t             Pt\t\tW\t\tD\t\tL")
for i, team in enumerate(sorted_teams):
    team_name = team.split(":")[0].split("-")[0].strip()  # split by ":" or "-" and select first element
    print(f"{i+1}\t{team_name.ljust(20)}\t{points[team]}\t\t{wins[team]}\t\t{draws[team]}\t\t{losses[team]}")
print("=" * 55)
 #Print top three players form a list
print("\nThe top three Premier League players this season are:")
print("=" * 55)
for i, player in enumerate(top_players):  # enumerate is a function that keeps track of a position
    print(f"{i+1}. {player}")

# Ask if the user wants to relegate the bottom team
relegate = input("\nDo you want to relegate the bottom team? (y/n):")
if relegate.lower() == "y":
    bottom_team = sorted_teams[-1]
    print("\n{} has been relegated.".format(bottom_team))
    sorted_teams = sorted_teams[:-1]

# Print the winner of the season
print("\nThe winner of the 2022/23 season is {}!".format(sorted_teams[0]))
