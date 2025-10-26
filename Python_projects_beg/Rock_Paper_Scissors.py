import random
ROCK = 'r'
SCISSORS = 's'
PAPER = 'p'
choices = ROCK,PAPER,SCISSORS

def choice_validator(func):
    def wrapper(*args, **kwargs):
        while True:
            try:
                user_choice = func(*args, **kwargs)
                if user_choice.isdigit() or user_choice not in choices:
                    raise ValueError
                return user_choice
            except ValueError:
                print(f"Invalid choice"\
                "\nLet's start again")
    return wrapper

@choice_validator
def user_input():
    return input("Rock,Paper or Scissor? (r/p/s): ").lower()

def user_game():
    user_choice = user_input()
    if user_choice == ROCK:
        print("Your choice is: rock 🗻")
        return ROCK
    if user_choice == PAPER:
        print("Your choice is: paper 📃")
        return PAPER
    if user_choice == SCISSORS:
        print("Your choice is: scissors ✂️")
        return SCISSORS
            

def computer():
    # can be improved by writing random.randint(choices) and adding dictionary
    rand = random.randint(1,3)
    match rand:
        case 1:
            print("Computer choice is: rock 🗻")
            return ROCK
        case 2:
            print("Computer choice is: paper 📃")
            return PAPER
        case 3:
            print("Computer choice is: scissors ✂️")
            return SCISSORS

def fight(user,computer):
    if computer == user:
        print("The game ended in a draw")
    elif user == ROCK and computer == SCISSORS:
        print("You won")
    elif user == SCISSORS and computer == PAPER:
        print("You won")
    elif user == PAPER and computer == ROCK:
        print("You won")
    else:
        print("Computer won")

    try:
        continue_game=(input("Continue the game?(y/n):"))
        if continue_game == 'y':
            return new_game()
        elif continue_game == 'n':
            return False
        else:
            raise ValueError
    except ValueError:
        print("You must answer y(yes) or n(no)!!!/" \
        "\nLet's start again")
        return new_game()
        

def new_game():
    fight(user = user_game(),computer=computer())

new_game()

#line 4 can be iproved by adding a list of valid choices and  check if user choice in
# list of choices


#line 37 : elif((user == 'r' and computer == 's') or
#             (user == 's' and computer == 'p') or
#             (user == 'p' and computer == 'r' )):
#              print("You won")