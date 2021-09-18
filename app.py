import random
from pyautogui import *

options = ["Rock","Paper","Scissors"]

def get_computer_pick(list):
    randChoice = random.choice(list)
    return randChoice

def get_user_pick():

    user_pick = prompt(title='Pick',text='Choose between, Rock - Paper - Scissors')
    return user_pick

def exec():
    computer_choice = get_computer_pick(options)
    user_choice = get_user_pick()
    computer_choice = computer_choice.upper()
    user_choice = user_choice.upper()
    #paper>rock, paper<scissor, rock>scissors, 
    if user_choice==computer_choice:
        alert(title='Rock & Paper & Scissors', text=f"Draw! {computer_choice} VS {user_choice}")
    elif user_choice=="ROCK" and computer_choice == "PAPER":
        alert(title='Rock & Paper & Scissors', text=f'Computer wins! {computer_choice} VS {user_choice}')
    elif user_choice=="PAPER" and computer_choice == "ROCK":
        alert(title='Rock & Paper & Scissors', text=f'Player wins! {computer_choice} VS {user_choice}')
    elif computer_choice=="SCISSORS" and user_choice=="PAPER":
        alert(title='Rock & Paper & Scissors', text=f'Computer wins! {computer_choice} VS {user_choice}')
    elif user_choice=="SCISSORS" and computer_choice == "PAPER":
        alert(title='Rock & Paper & Scissors', text=f'Player wins! {computer_choice} VS {user_choice}')
    elif computer_choice=="ROCK" and user_choice=="SCISSORS":
        alert(title='Rock & Paper & Scissors', text=f'Computer wins! {computer_choice} VS {user_choice}')
    elif user_choice=="ROCK" and computer_choice=="SCISSORS":
        alert(title='Rock & Paper & Scissors', text=f'Player wins! {computer_choice} VS {user_choice}')
    else:
        alert(title='Rock & Paper & Scissors', text=f'What did the user write? {computer_choice} VS {user_choice}')

while True:
    exec()
