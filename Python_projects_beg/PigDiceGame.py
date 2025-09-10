from random import randint

#Pig Dice Game: Two playes take turns to roll a dice

def roll_dice():
    dice = randint(2,6)
    print(f"You rolled a {dice}")
    return dice

def results(points, players, current_player):
        print(f"\nYou scored {points[players[current_player]]} points")
        print(f"Current scores: Player 1:{points['player1']} Player 2:{points['player2']}")

def check_answer(points, players, current_player):
    dice = roll_dice()
    if dice != 1:
        points[players[current_player]]+=dice
        answer = input("Roll again? (y/n): ").lower()
    else:
        points[players[current_player]] = 0
        answer = 'n'
    return answer

def game(points, players, current_player):
    while points['player1'] < 100 and points['player2'] < 100:
        if check_answer(points, players, current_player) == 'y':
            continue
        else:  
            results(points, players, current_player)
            current_player = 1 if current_player == 0 else 0

        print(f"\nPlayer {players[current_player]} turn")
    print(f"{players[current_player] } WON!!!")    

def main():
    points = {'player1': 0, 'player2': 0}
    players = list(points.keys())
    current_player = 0
    print(f"Player {players[current_player]} turn")
    game(points, players, current_player)
    
if __name__ == "__main__":
    main()
