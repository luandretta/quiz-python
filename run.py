"""
A FREE PYTHON QUIZ FOR NEWBIES
autor: Lucimeri Andretta
"""
import os
import time
import pyfiglet
import gspread
import colorama
from colorama import Fore, Back
from google.oauth2.service_account import Credentials
colorama.init(autoreset=True)


SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD.open("quiz_python")

question = SHEET.worksheet("questions")
answers = SHEET.worksheet("answers").get("B1:K1")
correct_answers = answers[0]
choices = ["a", "b", "c", "d"]

def clear():
    """
    Clears the terminal
    """
    #os.system("cls" if os.name == "nt" else "clear")
    print('\033c')


def get_username():
    """
    Get the username input from the user
    Run a while loop to collect a valid alpha username of data from user
    via the terminal. The loop will repeatedly request data, until it is valid
    When the username is valid, then the quiz function will be called
    """
    while True:
        print("Please type your name and press enter:")
        username = input("Only letters allowed \n").strip()
        if username.isalpha():
            print(Fore.GREEN+"----------------------------")
            print(f"Hello {Fore.GREEN}{username},")
            print(f"Each question has four choices {Fore.GREEN}(a, b, c or d).")
            print("Read the question, type your choice and hit enter.\n")
            print("Good luck!\n")
            time.sleep(8)
            clear()
            quiz(username)
            break
        print(f"{Fore.RED}{username} is not valid. Try again.")


def quiz(username):
    """
    Runs the quiz questions appropriately
    Calls the  verify_input function to validate the user's choice
    Each user choice will be check as right or wrong
    For each right answer increases the score by 1
    Displays score when the quiz is over
    Updates the worksheet
    """
    worksheet_to_update = SHEET.worksheet("answers")
    guesses = []
    current_question_i = 0
    score = 0
    for question_row in range(2, 12):
        row = question.row_values(question_row)
        print(Fore.GREEN+"----------------------------")
        print(*row, sep='\n')
        print(Fore.GREEN+"----------------------------\n")
        user_guesses = verify_input()
        guesses.append(user_guesses)
        if correct_answers[current_question_i] == guesses[current_question_i]:
            print(f"{Fore.GREEN}You are right, well done!\n")
            score += 1
        else:
            print(f"{Fore.RED}Nope, wrong answer :/ \n")
        time.sleep(1.5)
        current_question_i += 1
        clear()

    # Displays the user's score
    print(f"{Fore.GREEN}Calculating your score...\n")
    time.sleep(1)
    print(f"You got {Fore.GREEN}{score}{Fore.RESET} out of 10!")
    if score >= 7:
        print("Your result was great, congratulations!\n")
    else:
        print("Learn more and try again!\n")
    print(Fore.GREEN+"----------------------------")

    # Updates the worksheet
    guesses.insert(0, username)
    worksheet_to_update.append_row(guesses)


def verify_input():
    """
    Verifies if the input of user's choice is valid
    Executes a loop until the input is a, b, c or d
    """
    while True:
        guess = input("Enter a, b, c or d : \n").lower().strip()
        if guess in choices:
            return guess
        print(f"{Fore.RED}Try again, {guess} is not valid.\n")
        time.sleep(1)


def play_again():
    """
    Offers the user to attempt the quiz again.
    If user enters Y, the game starts.
    if user enters N, thank you message is displayed and the program exits
    """
    while True:
        print("Do you want to attempt the quiz again?\n")
        choice = input("Choose Y or N and press enter: \n").upper().strip()
        if choice == "Y":
            try_again = pyfiglet.figlet_format("Let's try it again\n")
            print(f"{Fore.GREEN} {try_again}")
            time.sleep(2)
            clear()
            return True
        elif choice == "N":
            print(f"{Fore.GREEN}Thank you for attempting the quiz!\n")
            game_over = pyfiglet.figlet_format("Game over")
            print(f"{Fore.RED} {game_over}")
            time.sleep(1)
            exit()
        else:
            print(Fore.RED+"Please choose Y or N.")


def main():
    """
    Prints initial text
    Calls the get_username fuction
    """
    # Initial text
    title = (pyfiglet.figlet_format("PYTHON QUIZ"))
    print(f"{Fore.GREEN} {title}")
    print("A FREE PYTHON QUIZ FOR NEWBIES")
    print(Fore.GREEN+"-------------------------------\n")
    print("It's a fun way to check your learning progress.\n")
    print("Are you ready to test your skills?\n")
    print("Please follow the steps bellow:\n")

    get_username()

    while play_again():
        get_username()


if __name__ == "__main__":
    # Execute main Python function
    main()
