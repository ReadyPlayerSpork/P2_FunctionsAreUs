"""
Luke Miller, Brinley Gregory, Ethan Carn, Madi Diefenbach, Seth Mortenson, Sydney Trojahn Hedges
IS303 Section 004 Group 12
Tracks a women's soccer season based on user input. Uses multiple functions collaborated together with GitHub.
"""

# Luke Miller & Brinley Gregory
# Main program file

# Imports functions from group members

from function1and2 import *
from function_4 import *
from function_5 import *
from function3Final import *

# Cleans terminal screen based on operating system

import os
import platform
import random

def clear_screen():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

clear_screen()

# INTRO
# Displays a welcome message and gets the user's name

name = intro()

# Creates a list to track W-L record for selected home team
seasonRecord = [0, 0]

# Determines the number of teams to create.
# Forces the user to input more than 1 team.
numTeams = int(input("Enter the number of teams in your region: "))
while numTeams < 2:
    print("Must enter an integer greater than 1\n")
    numTeams = int(input("Enter the number of teams in your region: "))

# Creates a list of teams based on user input.
# Asks for team names based on total number of teams in the region.
teams = []
for count in range(numTeams):
    teamName = str(input(f"Enter the name of team {count + 1}: "))
    teams.append(teamName)

# Defines variables to be used in the menu.
menuChoice = 0
homeTeam = None
oppTeam = None


# MAIN MENU
# Displays a menu based on user input. Menu loops until user chooses to exit.
while menuChoice != 4:

    # Displays menu information and gets choice from user
    menuChoice = menu()

    # CHOOSE A TEAM
    # Asks the user to select a home team and opposing team.
    if menuChoice == 1 :

        while homeTeam == None:
            print("\nPlease first select a home team\n")
            homeTeam = chooseTeam(teams,homeTeam,oppTeam,1,teams)

        print("\nPlease select an opposing team\n")
        oppTeam = chooseTeam(teams,homeTeam,oppTeam,2,teams)

        print(f"You chose\nHome Team: {homeTeam}\nOpposing Team: {oppTeam}")

    # PLAY A GAME
    # Geterates game information based on the teams selected.
    elif menuChoice == 2:
        if homeTeam and oppTeam is None:
            print("\nYou must select a home team and an opposing team in order to play a game.\n")
        if homeTeam and oppTeam != None:
            gameResult = fnPlayGame(homeTeam, oppTeam)
            if gameResult == "W":
                seasonRecord[0] = seasonRecord[0] + 1
                print(f"{homeTeam} Won!")
            elif gameResult == "L":
                seasonRecord[1] = seasonRecord[1] + 1
                print(f"{homeTeam} Lost...")

    # FINAL RECORD
    # Displays W-L record for selected home team after games are played.
    elif menuChoice == 3:
        if homeTeam == None and seasonRecord[0] < 1 or seasonRecord[1] < 1:
            print("\nYou must select a home team and play games in order to display a season record.\n")
        if homeTeam != None and seasonRecord[0] > 0 or seasonRecord[1] > 0:
            finalSeason = results(homeTeam, seasonRecord[0], seasonRecord[1])
    elif menuChoice != 4:
        print("\nInvalid input. Please enter a selection between 1-4.\n")

print("Exiting...")