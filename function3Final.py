# Display list of all teams and allow the user to choose a team using a menu. 
# Call the function again to let the user choose the opponent but do not display the team they chose previously. 
# Remove that team from the list.

#show the list of Teams function
def showTeams (teams,homeTeam,oppTeam,available_teams) :
    # set available teams list = to the teams list
    available_teams = teams
    print("Choose a team: ")
    # if both teams haven't been selected then print full list of teams
    if homeTeam is None and oppTeam is None :
        for iCount in range(len(teams)) :
            print(f'{iCount +1}. {teams[iCount]}')
    # if either team has been choosen enter this loop
    else :
        # set the available teams list equal to the list of teams minus the team that has been chosen
        available_teams = [team for team in teams if team != homeTeam and team != oppTeam]
        # print available teams list
        for iCount in range(len(available_teams)) :
            print(f"{iCount + 1}. {available_teams[iCount]}")
    # return the available teams list
    return available_teams

#choose team function
def chooseTeam (teams,homeTeam,oppTeam, userChoice,available_teams):
    #call show list of teams function
    available_teams = showTeams(teams,homeTeam,oppTeam , available_teams)
    try:
        # get user input for which team they want to select
        userChoiceTeam = int(input("Pick a team number: "))  
        # set user team to team in available teams list
        userTeam = available_teams[userChoiceTeam - 1]
        # return the value
        return userTeam
    except ValueError:
            print("Invalid input. Please enter a number.") 

# code for main file of code 
# create teams list, set up variables
# teams = ["BYU", "UVU" , "USU"]
# homeTeam = None 
# oppTeam = None
# userChoice = 0
# available_teams = teams
# # run until both a home team and a opposing team have been choosen
# while homeTeam == None or oppTeam == None:
#     try : 
#         # display choices
#         print ("Input 1 to select the home team")
#         print ("Input 2 to select the opposing team")
#         # get input for choice
#         userChoice = int(input("Enter your input:"))
#         # if 1st option then assign the team they choose to home team
#         if userChoice == 1 : 
#             # home team  = return of they team of choice
#             homeTeam = chooseTeam(teams,homeTeam,oppTeam,userChoice,available_teams)
#         # if 2nd option then assign the team they choose to oppposing team
#         elif userChoice == 2 :
#             # opposing team  = return of they team of choice
#             oppTeam = chooseTeam(teams,homeTeam,oppTeam,userChoice,available_teams)
#         else :
#             # if a number is entered other than 1 or 2 print error
#             print("Please enter a 1 or 2.")
#     except ValueError : 
#         # if the input is not an integer then print error
#         print ("Please enter a number, 1 or 2.")
