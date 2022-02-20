"""
This section contains all imports
"""
import sys
import random
from words import easy_selection
from words import hard_selection


def get_name():
    """
    Welcome message and get name from user
    """
    print("************************")
    print("       Hangman")
    print("Guess the word to win!")
    print("************************\n")

    while True:
        name_data = input("\033[0;36mEnter your name here: ")

        if validate_data(name_data):
            print(f"\033[0;36mWelcome {name_data} \n")
            break


def validate_data(name):
    """
    Validates user input for name
    """
    try:
        if name == "":
            raise ValueError("\033[0;31mPlease input a name \n")

    except ValueError as error:
        print(f"\033[0;31mTry again. {error}")
        return False

    return True


def menu():
    print("Main Menu: \n")
    print("1. Instructions")
    print("2. Start Game")
    print("3. Exit \n")

    while True:
        player_choice = input("\033[0;36mPlease choose from the above menu: ")

        if player_choice == '1':
            instructions()
        elif player_choice == '2':
            choose_word()
        elif player_choice == '3':
            exit()
        else:
            print("\033[0;31mOoops, Please choose a valid option from the menu!")
            

def instructions():
    """
    This option shows the user the basic game instructions
    """
    print(
        "\n"
        "\033[0;32mHow to Play: \n\n"
        "The aim is to make the correct word by guessing "
        "the letters one at a time. \n\n1. To guess, "
        "type a letter of your choice and hit enter. \n2. If you "
        "are right the letter will appear on screen. \n3. If you "
        "are wrong the hangman will start to appear. \n4. You have "
        "6 attempts to guess correctly or its Game Over!! "
    )
    #Give option to play or return to menu.
    print("Are you ready to play Hangman?")

    #Test for valid selection made
    while True:
        lets_go = input("\033[0;36mPress 1 for Yes or 2 for No: ")

        if lets_go == '1':
            choose_word()
        elif lets_go == '2':
            menu()
        else:
            print("Please make a valid choice.")


def exit():
    print("\033[0;36mThanks for playing Goodbye!")
    sys.exit()


def choose_word():
    """
    Generates a random word from the easy or hard selection lists. 
    """
    level_selection = ("\033[0;36mPlease choose a difficulty level: \n")
    #Test for valid selection made
    while True:
        difficulty = input("Press 1 for Easy and 2 for Hard: ")

        if difficulty == '1':
            word = random.choice(easy_selection)
            start_game(word)
        elif difficulty == '2':
            word = random.choice(hard_selection)
            start_game(word)
        else:
            print("Please make a valid choice.")


def start_game(word):
    """
    Using words from words.py, choose a random word and promt the user to guess letters. 
    """
    attempts = 6
    letters = set(word)
    guesses = []
    #


def game():
    get_name()
    menu()

game()