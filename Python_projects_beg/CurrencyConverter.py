from time import sleep

def get_user_amount():
    while True:
        try:
            user_amount = float(input("Enter the amount: "))
            if user_amount<=0:
                print("Invalid amount")
            else:
                #instead of break better use return
                return user_amount              
        except ValueError:
            print("It must be a number!!")

def get_currency(text):
    available_currency = ["USD","EUR","PLN"]
    while True:
        try:
            currency = input(f"{text} currency in (USD/EUR/PLN): ").upper()
            if currency not in available_currency:
                raise ValueError
            else:
                return  currency
        except ValueError:
            print("Invalid amount")

def show_result(initial_currency, convert_into_currency,user_amount):

    currencies = {
    "USD": {"PLN": 4.2, "EUR":0.19},
    "EUR" : {"PLN":4.5 , "USD":1.1},
    "PLN" : {"USD":0.24 , "EUR":0.22}
    }

    if initial_currency == convert_into_currency:
        print("Converting your money....")
        sleep(1.5)
        return user_amount

    converted = user_amount * currencies[initial_currency][convert_into_currency]
    print("Converting your money....")
    sleep(1.5)
    return converted
        

#better not to call it separately; better to encapsulate it in a main() function and call it in one line
def main():
    amount = get_user_amount()
    initial_currency = get_currency("Initial")
    convert_into_currency = get_currency("Converted into")
    converted = show_result(initial_currency,convert_into_currency,amount)
    print(f"Your {amount:*^10} {initial_currency} is equal to {converted:.2f} in {convert_into_currancy}")

# to run it when we execute the code directly
if __name__ == "__main__":
    main()