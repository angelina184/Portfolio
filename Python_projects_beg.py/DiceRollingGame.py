from random import randint
question=input("Roll the dice? (y/n):")

while question!='n':

    if question == 'y': 
        first = randint(1,6)
        second = randint(1,6)
        print(second,first) 
    
    else:
        print("Invalid choice!")
        
    question = input("Roll the dice? (y/n):")

print("Thanks for playing")
