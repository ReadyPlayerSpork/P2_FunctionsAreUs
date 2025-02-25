#displays intro to the games, explains rules, and gets players name
def intro ():
    print("Welcome to the 2025 Women's Soccer Season")
    print("In this game, you will manage a women's soccer team, play games, and strive to win the championships! ")
    name = input("What is your name? ")
    print(f"Welcome {name}! Get ready to lead your team to victory!")
    return name 

#displays menu which provides the users options 
def menu ():
    print("/nMenu")
    print("1. Play a game")
    print("2. Final record")
    print("3.Quit")

    choice = input("Choose a number (1-3): ")
    return choice
