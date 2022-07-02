import random
import time

RED = '\033[91m'
YELLOW = '\033[93m'
GREEN = '\033[92m'
WHITE = '\033[0m'
BOLD = '\033[1m'

ROCK = 1
PAPER = 2
SCISSORS = 3
WEAPONS = {ROCK: 'Rock', PAPER: 'Paper', SCISSORS: 'Scissors'}
PLAY_AGAIN = {1: True, 2: False}

def play():
    while True:
        print(f'{BOLD}{YELLOW}Please choose from the following options:')
        print(f'{WHITE}{BOLD} [1] - Play against the computer.')
        print(f' [2] - Play against another player.')
        print(f' [3] - Quit.')

        try:
            choice = input(f'{YELLOW}{BOLD}What\'s your choice? {WHITE}')

            if choice.isdigit():
                choice = int(choice)

                if choice not in WEAPONS:
                    raise ValueError('Choice is not valid!')
                
                break
            else:
                raise ValueError('Choice is not a number!')
        except ValueError as error:
            print(f'{RED}{BOLD}Error: {WHITE}{BOLD}{error}')
        except Exception as error:
            print(f'{RED}{BOLD}Error: {WHITE}{BOLD}{error}')

    menu(choice)

def menu(choice: int) -> None:
    if choice == 1:
        play_against_computer()
    elif choice == 2:
        print(f'{GREEN}{BOLD}COMING REAL SOON!{WHITE}')
    elif choice == 3:
        quit_game()

def quit_game():
    print(f'{WHITE}{BOLD}OK. Quitting in {GREEN}3 {WHITE}', end = '')
    loading()

    print(f'{YELLOW}{BOLD} 2 {WHITE}', end = '')
    loading()

    print(f'{RED}{BOLD} 1 {WHITE}', end = '')
    loading()

    raise KeyboardInterrupt

def loading():
    time.sleep(0.333)
    print('.', end = '')
    time.sleep(0.333)
    print('.', end = '')
    time.sleep(0.333)
    print('.', end = '')

def play_against_computer():
    print(f'{BOLD}{GREEN}You have chosen to play against the computer!')

    while True:
        print(f'{BOLD}{YELLOW}Please choose from the following options:')
        print(f'{WHITE}{BOLD} [1] - Rock.')
        print(f'{WHITE}{BOLD} [2] - Paper.')
        print(f'{WHITE}{BOLD} [3] - Scissors.')

        try:
            weapon = input(f'{BOLD}{GREEN}Please choose a weapon: {WHITE}')

            if weapon.isdigit():
                weapon = int(weapon)

                if weapon not in WEAPONS:
                    raise ValueError('Choice is not valid!')
                
                break
            else:
                raise ValueError('Choice is not a number!')
        except ValueError as error:
            print(f'{RED}{BOLD}Error: {WHITE}{BOLD}{error}')
        except Exception as error:
            print(f'{RED}{BOLD}Error: {WHITE}{BOLD}{error}')
        
    computer_weapon = random.choice(list(WEAPONS))

    if weapon == computer_weapon:
        print(f'{WHITE}{BOLD}You chose {GREEN}{BOLD}{WEAPONS[weapon]}{WHITE}{BOLD}, and the computer chose {GREEN}{BOLD}{WEAPONS[computer_weapon]}{WHITE}{BOLD} too!')
        print(f'{BOLD}{YELLOW}It\'s a tie!')
    else:
        print(f'{WHITE}{BOLD}You chose {GREEN}{BOLD}{WEAPONS[weapon]}{WHITE}{BOLD}, but the computer chose {GREEN}{BOLD}{WEAPONS[computer_weapon]}{WHITE}{BOLD}.')

        if weapon == ROCK and computer_weapon == PAPER:
            print(f'{BOLD}{RED}You lose!')
        elif weapon == ROCK and computer_weapon == SCISSORS:
            print(f'{BOLD}{GREEN}You win!')
        elif weapon == PAPER and computer_weapon == ROCK:
            print(f'{BOLD}{GREEN}You win!')
        elif weapon == PAPER and computer_weapon == SCISSORS:
            print(f'{BOLD}{RED}You lose!')
        elif weapon == SCISSORS and computer_weapon == ROCK:
            print(f'{BOLD}{RED}You lose!')
        elif weapon == SCISSORS and computer_weapon == PAPER:
            print(f'{BOLD}{GREEN}You win!')
    
    time.sleep(1.5)
    
    play_again()

def play_again():
    while True:
        print(f'{BOLD}{GREEN}Would you like to play again? {WHITE}')
        print(f'{YELLOW}{BOLD} [1] - Yes.')
        print(f'{YELLOW}{BOLD} [2] - No.')

        try:
            play_again = input(f'{BOLD}{GREEN}What\'s your choice? {WHITE}')

            if play_again.isdigit():
                play_again = int(play_again)

                if play_again not in PLAY_AGAIN:
                    raise ValueError('Choice is not valid!')

                break
            else:
                raise ValueError('Choice is not a number!')
        except ValueError as error:
            print(f'{RED}{BOLD}Error: {WHITE}{BOLD}{error}')
        except Exception as error:
            print(f'{RED}{BOLD}Error: {WHITE}{BOLD}{error}')

    if play_again == 1:
        play()
    else:
        quit_game()
    

def main():
    print(f'{BOLD}{GREEN}Welcome to Rock, Paper, Scissors!')
    
    play()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print(f'{RED}{BOLD}\nGoodbye!{WHITE}')
    except Exception as error:
        print(f'{RED}{BOLD}\nError: {WHITE}{BOLD}{error}')