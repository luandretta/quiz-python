import gspread
from google.oauth2.service_account import Credentials
import os

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD.open('quiz_python')

questions = SHEET.worksheet('questions')
data = questions.get_all_values()

# Initial text
print("FREE PYTHON QUIZ FOR NEWBIES")
print("----------------------------")
print("It's a fun way to check your learning progress.")
print("Are you ready to test your skills? Please follow the steps bellow:")

def clear():
    """
    Clears the terminal
    """
    os.system("cls" if os.name == "nt" else "clear")


def get_username():
    """
    Get username input from the user before starting the quiz
    """
    while True:
        username = input("Please type your name and press enter: \n")
        if username.isalpha():
            print("----------------------------")
            print("Hello " + username + ", good luck!")
            new_question()
            break
        print(f"{username} is not valid, try again.")

 
def new_question():
    """
    Run the questions propertly
    """
    
    question = SHEET.worksheet("questions")
    correct_answers = SHEET.worksheet("answers")
    guesses = []
    
    for i in range(2,12):
        row = question.row_values(i)
        print("----------------------------")
        print(*row, sep='\n')
        print("----------------------------" '\n')
        #guess = ()
        #clear()
        guesses.append(verify_input())
            
        
        
    print(guesses)
    #display score


def verify_input():
    

    while True:
        guess = input("Enter a, b, c or d : \n").lower()
        choices = ["a", "b", "c", "d"]
        if guess in choices:
            return guess
        print(f"Try again, {guess} is not valid. \n")


def main():
    """
    Run all programs function
    """
    username = get_username()
    #new_row = username + guesses
    #update_worksheet(new_row, "answers")

main()