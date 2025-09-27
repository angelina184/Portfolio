import random
import string

def letters_generator():
    upercase = input("Include uppercase letters? (y/n): ").lower()
    if upercase == 'y':
        return True
    return False

def numbers_generator():
    num = input("Include numbers? (y/n): ").lower()
    if num == 'y':
        return True
    return False

def special_chars_generator():
    char = input("Include special characters? (y/n): ").lower()
    if char == 'y':
        return True
    return False
    
def password_generator(length, special_chars_gen, numbers_gen, letters_gen):
    # if 3 times True than length<3
    if length < (special_chars_gen + numbers_gen + letters_gen):
        raise ValueError('Password is too short')
    
    password = []
    # filling in the remaining space
    characters = string.ascii_lowercase
    if special_chars_gen:
        password.append(random.choice(string.punctuation))
        characters  += string.punctuation
    if letters_gen:
        password.append(random.choice(string.ascii_uppercase))
        characters  +=  string.ascii_uppercase
    if numbers_gen:
        password.append(random.choice(string.digits))
        characters  +=  string.digits

    password_elements  = [random.choice(characters) for _ in range(length-len(password))]
    password.extend(password_elements)
    random.shuffle(password)
    return ''.join(password)

def main():
    length = int(input("Enter the password length:"))
    special_chars_gen = special_chars_generator()
    numbers_gen = numbers_generator()
    letters_gen = letters_generator()
    try:
        print(password_generator(length, special_chars_gen, numbers_gen, letters_gen))
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()