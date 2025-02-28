#Function 4 group project
#Ethan Carn
#Generates random scores and stores wins and losses in a dictionary 
import random

def fnPlayGame(szHomeTeam, szOpponent):
    # Generate random scores, ensuring no ties
    iHomeScore, iAwayScore = random.randint(0, 10), random.randint(0, 10)
    while iHomeScore == iAwayScore:
        iHomeScore, iAwayScore = random.randint(0, 10), random.randint(0, 10)
    
    # Determine win/loss
    sResult = "W" if iHomeScore > iAwayScore else "L"
    return sResult