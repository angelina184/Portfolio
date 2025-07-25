#Guess the number betwee 1  and 100
import random
def guess_number(right_number):
    guess = input("Guess the number betwee 1  and 100:")
    while guess.isalpha():
        print("Enter the valid number")
        guess = input("Guess the number betwee 1  and 100:")

    while guess!=right_number:
        if int(guess) == right_number:
            print ("You guessed the number")
            return False
        
        if int(guess) > right_number:
            print("Too high")
            guess = input("Guess the number betwee 1  and 100:")
            
        else:
            print("Too low")
            guess = input("Guess the number betwee 1  and 100:")

random_right_number = random.randint(1,100)
guess_number(random_right_number)