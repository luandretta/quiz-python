import gspread
from google.oauth2.service_account import Credentials
import os
import time

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD.open('quiz_python')

question = SHEET.worksheet("questions")
answers = SHEET.worksheet("answers").get("B1:K1")
correct_answers = answers[0]


# Initial text
print("FREE PYTHON QUIZ FOR NEWBIES\n")
print("----------------------------\n")
print("It's a fun way to check your learning progress.\n")
print("Are you ready to test your skills? Please follow the steps bellow:\n")


def clear():
    """
    Clears the terminal
    """
    os.system("cls" if os.name == "nt" else "clear")


def get_username():
    """
    Get username input from the user before starting the quiz
    Check if the user enters a valid alpha username
    """
    while True:
        username = input("Please type your name and press enter: \n")
        if username.isalpha():
            print("----------------------------")
            print(f"Hello {username},")
            print("Each question has four choices(a, b, c or d).")
            print("Read the question, type your choice and hit enter.\n")
            print("Good luck!\n")
            time.sleep(4)
            clear()
            quiz(username)
            break
        print(f"{username} is not valid, try again.")

 
def quiz(username):
    """
    Run the quiz questions propertly
    Call the function verify_input 
    Display score
    Update the worksheet
    """
    worksheet_to_update = SHEET.worksheet("answers")
    guesses = []
    j = 0
    score = 0
    for i in range(2,12):
        row = question.row_values(i)
        print("----------------------------")
        print(*row, sep='\n')
        print("----------------------------\n")
        guesses.append(verify_input())
        if correct_answers[j] == guesses[j]:
            print("You are right, well done!\n")
            score += 1
        else:
            print("Nope, wrong answer :/ \n")
        time.sleep(1)
        j += 1
        clear()
    
    # Display user's score
    print("Calculating your score...\n")
    time.sleep(2)
    print(f"You got {score} out of 10 questions right.\n")
    if score >= 8:
        print("Your result was great, congratulations!\n")
    else:
        print("Learn more and try again!\n")
    print("----------------------------")
    
    # Update the worksheet
    guesses.insert(0, username)
    worksheet_to_update.append_row(guesses)

  
def verify_input():
    """
    Verify if the input from user choice is valid
    """
    while True:
        guess = input("Enter a, b, c or d : \n").lower()
        choices = ["a", "b", "c", "d"]
        if guess in choices:
            return guess
        print(f"Try again, {guess} is not valid. \n")
        time.sleep(1)

def play_again():
    while True:
        print("Do you want to attempt the quiz again?\n")
        choice = input("Please choose Y or N and press enter: \n").upper()
        if choice == "Y":
            print(f"Let's try again\n")
            time.sleep(1)
            clear()
            return True
        elif choice == "N":
            print("Thank you for attempting the quiz!\n")
            time.sleep(1)
            exit()
        else:
            print("Please choose Y or N.")


get_username()

while play_again():
    get_username()