class ATM:
    def __init__(self):
        self.balance = 0
        #there is no sense save information about withdraw or diposit it is dinamic

    def check_balance(self):
        return self.balance 
    
    def deposit(self,amount):
        if amount <= 0:
            raise ValueError("Deposite amount must be positive")
        self.balance += amount


    def withdraw(self,amount):
        if amount <= 0:
            raise ValueError("Withdraw value must be positive.")
        if amount > self.balance:
            raise ValueError("Insufficient funds.")
        self.balance -= amount
#the UI of ATM (inside we have ATM object -> self.atm)
class ATMUI:
    def __init__(self):
        self.atm = ATM()
    def get_number(self, value):
        while True: 
            try:
                return float(input(value))
            except ValueError:
                print("Please enter a valid number")
    def display_menu(self):
        print("")
        print("Welcome to the ATM!")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4.Exit")
    
    def display_balance(self):
        print(f"Your current balance is ${self.atm.check_balance()}")
    
    def deposit_processing(self):
        while True:
            try:
                amount = self.get_number("Enter the amount to deposit:")
                # because we need ATM()deposit() --> deposit from ATM class
                self.atm.deposit(amount)
                print(f"Successfuly deposited ${amount}")
                break
            except ValueError as error:
                print(error)   

    def withdraw_processing(self):
        while True:
            try: 
                amount = self.get_number("Enter the amount to withdraw:")
                # when in this class we call function of another class
                self.atm.withdraw(amount)
                print(f"Successfully withdrew ${amount}")
                break
            except ValueError as error:
                print(error)

    def run(self):
        while True:
            self.display_menu()
            option = input("Pleace choose an option:")
            match option:
                case "1":
                    #when in this class we call functions in class
                    self.display_balance()
                case "2":
                    self.deposit_processing()
                case "3":
                    self.withdraw_processing()
                case "4":
                    print("Thank you for using ATM")
                    break

# UI code 
def main():
    atm = ATMUI()
    atm.run() 
    
if __name__ == "__main__":
    main()