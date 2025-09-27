import random
import logging
logging.basicConfig(level=logging.DEBUG, filename="log.log",
                    format = "%(asctime)s - %(levelname)s -%(message)s")
def get_user_balance():
    while True:
        try:
            balance = int(input("Enter your starting balance: $"))
            if balance <= 0:
                logging.info("Balance must be a positive number")
            else:
                return balance
        except ValueError:
            logging.error("Enter valid number",exc_info=True)


def get_user_bet(current_balance):
    while True:
        try:
            bet = int(input("Enter your bet amount: $"))
            if bet <= 0 or bet > current_balance:
                logging.info(f"Invalid bet amount. You can bet between {bet} and {current_balance}")
            else:
                return bet
        except ValueError:
            logging.error("Enter valid number for the bet amount",exc_info=True)

def display_slot_machine():
    figures = ['🍒','🍓' ,'🍉','🍊','🍋','🍌','🥑','🥝','🍍','🍇','🍐']
    spin_reels = [] 
    for i in range(3):
        spin_reels.append(random.choice(figures))
        print(f"{spin_reels[i]}|", end = "") 
    return spin_reels

def payout(spin_reels,current_balance, bet_amount):
    if spin_reels[0] == spin_reels[1] == spin_reels[2]:
        bingo = 10*bet_amount
        current_balance += (bingo-bet_amount)
        print(f"\nYou won ${bingo}!")
        

    elif spin_reels[0] == spin_reels[1] or spin_reels[0] == spin_reels[2] or spin_reels[1]==spin_reels[2]:
        win_amount = 2*bet_amount
        current_balance+=(win_amount-bet_amount)
        bet_amount = 0
        print(f"\nYou won ${win_amount}!")

    else:
        current_balance-=bet_amount
        bet_amount = 0
        print("\nYou lost!")
    return current_balance

def main():
    start_balance = get_user_balance()

    print("\nWelcome to the Slot Machine Game!")
    print(f"You start with a balance of {start_balance}")
    
    bet_amount = get_user_bet(start_balance)
    spin_reels = display_slot_machine()
    current_balance = payout(spin_reels,start_balance,bet_amount)

    while current_balance>0:
        game = input("Do you want continue playing? (y/n)").lower()
        if game == 'y':
            print("\nCurrent balance:",current_balance)
            bet_amount = get_user_bet(current_balance)
            spin_reels = display_slot_machine()
            current_balance = payout(spin_reels,current_balance,bet_amount)
        else:
            break

    if current_balance <= 0:
        logging.info("You are out of money! Game over.")



if __name__ == '__main__':
    main()