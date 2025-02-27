#displays intro to the games, explains rules, and gets players name
def intro ():
    print("Welcome to the 2025 Women's Soccer Season")
    print("In this game, you will manage a women's soccer team, play games, and strive to win the championship! ")
    name = input("What is your name? ")
    print(f"Welcome {name}! Get ready to lead your team to victory!")
    return name 

#displays menu which provides the users options 
def menu ():
    print("/nMenu")
    print("1. Choose a team")
    print("2. Play a game")
    print("3. Final record")
    print("4. Quit")
    choice = input("Enter a choice (1-4): ")
    return choice 

    
