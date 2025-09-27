import random

def file_words():
    try:
        with open('Portfolio\Python_projects_beg\words.txt', 'r') as file:
            content = file.read().splitlines()
        return content
    except FileNotFoundError:
        print("words.txt doesn't exist")
        return []
    
def words_sheet():
    file = file_words()
    if not file:
        print("No words in the file")
        return
    right_word = random.choice(file).lower()
    print(right_word)
    fill_in_sheet = ['_']*len(right_word)
    print(''.join(fill_in_sheet))
    return right_word, fill_in_sheet

def words_validator(checked):
    while True:
        try:
            letter = input("Enter a letter: ")
            if len(letter) !=1 :
                raise ValueError("Enter only one letter")
            if not letter.isalpha():
                raise ValueError("Enter only letters from a-z")
            break
        except ValueError as e:
            print(e) 
    if letter in checked:
        print("You already guessed that letter")
    checked.add(letter)
    return letter

def display_word(attempts, checked,words):
    found = False
    while attempts > 0:
        letter = words_validator(checked)
        for index, element in enumerate(words[0]):
            if letter == element and words[1][index] == '_':
                found = True
                words[1][index] = letter
                
        if found:
            print("Good guess")
            found = False

        if '_' not in words[1]:
            print("Congrats") 
            attempts = 0
            break

        if letter not in words[1]:    
            print("Wrong guess")
            attempts-=1       
        print(''.join(words[1]))
        
    if '_' in words[1]:
        print(f"Game over! The word was {words[0]}")
    
def main():
    words = words_sheet()
    attempts = 6
    checked = set()
    display_word(attempts,checked,words)

if __name__ == '__main__':
    main()