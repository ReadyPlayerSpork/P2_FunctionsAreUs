# Display list of all teams and allow the user to choose a team using a menu. 
# Call the function again to let the user choose the opponent but do not display the team they chose previously. 
# Remove that team from the list.

#Sydney (Trojahn) Hedges

#show the list of Teams function
def showTeams (teams) :
    print("Choose a team: ")

    for iCount in range(len(teams)) :
        print(f'{iCount +1}. {teams[iCount]}')

#choose team function
def chooseTeam (teams):
    #call show list of teams function
    showTeams(teams)

    #valid int input (from class example using while True)
    while True:
        try:
            userChoice = int(input("Pick a team number: "))  #can reword input option
            
            # if a # is inputted but not on the list
            if 1 <= userChoice <= len(teams): 
                return teams.pop(userChoice -1) #since team location is -1 of choice input
            else: 
                print("Number not listed. Please pick a team's number from the list. ")
        
        except ValueError:
            print("Invalid input. Please enter a number.") 
