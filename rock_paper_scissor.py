import random
from colorama import Fore, Back, Style

def choice_list (mylist):
    computer_choice = random.choice(mylist)
    return computer_choice

def user_guess ():
    guess = ''
    while guess not in ['r', 'p', 's']:
        guess = input('Select one: r, p, or s: ')
        if guess == 'r' or guess == 's' or guess == 'p':
            return guess
        else:
            print("Please try with 'r', 's' or 'p' ")
             
def check_guess(computer_choice, guess):

    if (computer_choice == 'r' and guess == 's') or\
        (computer_choice == 'p' and guess == 'r')or\
        (computer_choice == 's' and guess == 'p'):
        print(Fore.RED + 'You lose!')
        print(Style.RESET_ALL)
        return -1
        
    elif (guess == 'r' and computer_choice == 's') or\
        (guess == 'p' and computer_choice == 'r')or\
        (guess == 's' and computer_choice == 'p'):
        print(Fore.GREEN + 'You win!')
        print(Style.RESET_ALL)
        return 1
    elif (guess == 'r' and computer_choice == 'r') or\
        (guess == 'p' and computer_choice == 'p')or\
        (guess == 's' and computer_choice == 's'):
        print(Fore.YELLOW +'Draw!')
        print(Style.RESET_ALL)
        return 0

def game():
    count_computer = 0
    count_player = 0
            
    while True:
        result_computer = choice_list(['r', 'p', 's'])
        theguess = user_guess()
        print(f'The computer chose {result_computer}')
        result = check_guess(result_computer, theguess)
        if result == -1:
            count_computer += 1
        if result == 1:
            count_player += 1
        replay = input('Continue (yes or no): ')
        if replay == 'yes':
            continue 
        else:
            print(f'Computer score: {count_computer} \nPlayer score: {count_player}')
            break      
game()      