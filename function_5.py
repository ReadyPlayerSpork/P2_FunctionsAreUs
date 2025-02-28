# Brinley Gregory
# Section 004

# 5. Display the final record for a team. Receive the home team data and display information.
# Using parameters, print final record
# calculate whether the team needs to practice

def results(homeTeamName, totalWins, totalLosses):
    print(f"Final season record: {homeTeamName} {totalWins}-{totalLosses}") # printing results
    # printing whether or not the team needs to practice
    if totalWins >= (totalWins+totalLosses) * .75: 
        print("Qualified for the NCAA Women's Soccer Tournament")
    elif totalWins >= (totalWins+totalLosses) * .5:
        print("You had a good season")
    else:
        print("Your team needs to practice!")
