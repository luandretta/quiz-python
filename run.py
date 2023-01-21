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
    This function clears the terminal
    """
    os.system("cls" if os.name == "nt" else "clear")


clear()
lu

def get_username():
    """
    Get username input from the user before starting the quiz
    """
    while True:
        username = input("Please type your name and press enter: \n")
        if username.isalpha():
            print("Hello " + username + ", good luck!")
            new_question()
            break
        print(f"{username} is not valid, try again.")

 
def new_question():
    """
    Run the questions propertly
    """
    question = SHEET.worksheet("questions").get_all_values()
    question_row = question[1]
    print("----------------------------")
    print(*question_row,sep='\n')
    guesses = []
    guesses = input("Enter your answer: \n")

def clear():
    """
    This function clears the terminal
    """
    os.system("cls" if os.name == "nt" else "clear")


clear()


def main():
    """
    Run all programs function
    """
    username = get_username()
    #new_row = username + guesses
    #update_worksheet(new_row, "answers")



main()