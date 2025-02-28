import function1and2
import function3Part1
import function_4
import function_5
from function3Final import chooseTeam , showTeams

name = function1and2.intro()
print(name)

menuChoice = function1and2.menu()
print(menuChoice)

# if user input is choose teams then enter team choice function
if menuChoice == 1 :
    # code for main file of code 
    # create teams list, set up variables
    teams = ["BYU", "UVU" , "USU"]
    homeTeam = None 
    oppTeam = None
    userChoice = 0
    available_teams = teams
    # run until both a home team and a opposing team have been choosen
    while homeTeam == None or oppTeam == None:
        try : 
            # display choices
            print ("Input 1 to select the home team")
            print ("Input 2 to select the opposing team")
            # get input for choice
            userChoice = int(input("Enter your input:"))
            # if 1st option then assign the team they choose to home team
            if userChoice == 1 : 
                # home team  = return of they team of choice
                homeTeam = chooseTeam(teams,homeTeam,oppTeam,userChoice,available_teams)
            # if 2nd option then assign the team they choose to oppposing team
            elif userChoice == 2 :
                # opposing team  = return of they team of choice
                oppTeam = chooseTeam(teams,homeTeam,oppTeam,userChoice,available_teams)
            else :
                # if a number is entered other than 1 or 2 print error
                print("Please enter a 1 or 2.")
        except ValueError : 
            # if the input is not an integer then print error
            print ("Please enter a number, 1 or 2.")
    print(f"You chose\nHome Team: {homeTeam}\nOpposing Team: {oppTeam}")