# leon Kohlhaußen

# rock paper scissors

# import modules
import time
import os
from colorama import *          # colorama module to print colors in the terminal
# there is no need of reset every color effekt in the code duo this setting
init(autoreset=True)


def main():
    os.system('cls')
    print("Welcome to rock paper scissors")
    print("1. Play against the computer")
    print("2. Play against a friend")
    print("3. Back to the main menu")
    print("4. Exit the game collection")
    answer = input(">>> ")
    try:
        answer = int(answer)
        if answer == 1:
            playAgainstComputer()
        elif answer == 2:
            playAgainstFriend()
        elif answer == 3:
            mainScreen.mainMenu()
        elif answer == 4:
            exit()
    except ValueError:
        print("Please enter a number!")
        main()

    def playAgainstComputer():
        os.system('cls')
        print("Welcome to rock paper scissors against the computer")
        print("1. Rock")
        print("2. Paper")
        print("3. Scissors")
        print("4. Back to the main menu")
        print("5. Exit the game collection")
        answer = input(">>> ")
        try:
            answer = int(answer)
            if answer == 1:
                rock()
            elif answer == 2:
                paper()
            elif answer == 3:
                scissors()
            elif answer == 4:
                main()
            elif answer == 5:
                exit()
        except ValueError:
            print("Please enter a number!")
            playAgainstComputer()
