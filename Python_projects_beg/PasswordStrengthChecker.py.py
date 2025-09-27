import re
def check_password_strength(password: str, *patterns) -> str:
    """Function checks password strength"""
    strength = sum(1 if re.search(pattern,password) and len(password)>=8 else 0 for pattern in patterns)
    strength_val = {0:"Very weak",
                    1:"Weak",
                    2:"Medium",
                    3:"Strong",
                    4:"Very strong"}
    return strength_val[strength]

def main() -> None:
    password = input(("Enter a password :"))

    num = r'[0-9]'
    upper_let =r'[A-Z]'
    lower_let = r'[a-z]'
    special_char = r'[ !@#$%^&*()_+{}":;\']'
    patterns = [num, upper_let,lower_let,special_char]

    print(check_password_strength(password, *patterns))

if __name__ == "__main__":
    main()