import random
from typing import List,Tuple
#SECRET = "9243"
print("I have generated a 4-digit number with unique digits. Try to guess it!")

def generate_secret_number() -> str:
    "Function to generate secret number"
    digits: List[int] = list(range(10))
    random.shuffle(digits)
    secret = ''.join(str(digit) for digit in digits[:4])
    print(secret) # for testing
    return secret

def check_guess() -> str:
    "Function checks if number is valid"
    while True:
        try:
            guess = input("Guess: ")
            if len(guess)!= 4 or len(set(guess))!=4 or not guess.isdigit():
                raise ValueError
            break
        except ValueError:
            print("Invalid input")
            continue
    return guess

def calculate_cows_bulls(guess: str,secret: str) -> Tuple[int,int]:
    "Function for game itself. Calculates cows and bulls"
    #cows = is correct digit but in wrong place
    cows: int = sum([ 1 for i in range(4) if guess[i] in secret[i]])-bulls
    #bull digit is correct and in correct position
    bulls: int = sum([ 1 for i in range(4) if guess[i] == secret[i]]) 

    return cows, bulls # returns a tuple
"""
    for index1, digit1 in enumerate(guess):
        for index2, digit2 in enumerate(secret):
            if digit1 == digit2 and index1 != index2:
                cows += 1
            elif digit1 == digit2 and index1 == index2:
                bulls += 1
"""


def main() -> None:
    secret = generate_secret_number()
    while True:
        guess = check_guess()
        cows,bulls = calculate_cows_bulls(guess, secret)
        print(f"{cows} cows, {bulls} bulls")
        if bulls == 4:
            print("Congrats! You guessed the number!")
            break

if __name__ == "__main__":
    main()

