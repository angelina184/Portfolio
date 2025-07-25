from random import randint
question = input("Roll the dice? (y/n):").lower()
if question == 'y':
    times=int(input("How many dice you want to roll?(number):"))
count_times=0
rolled_dice=0
while question!='n':
    if question == 'y':
        rolled_dice+=1
        while count_times<times: 
            first = randint(1,6)
            second = randint(1,6)
            print(second,first) 
            count_times+=1
            
    else:
        print("Invalid choice!")
        question = input("Roll the dice? (y/n):").lower()

    count_times=0
    question = input("Roll the dice? (y/n):").lower()
    times=int(input("How many dice you want to roll?(number):"))
print(f"You rolled the dice {rolled_dice:*^11d} times")
print("Thanks for playing")
