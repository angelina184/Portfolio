PLAYER1 = "X"
PLAYER2 = "Y"
ROWS = 3
COLUMNS = 3
SIGN1 = 'X'
SIGN2 = 'Y'
SEPARETOR = "---+---+---"
from termcolor import colored
#clean_sheet = [[' '] * COLUMNS for _ in range(ROWS)]
clean_sheet = [
        #[0] [1] [2]
        [' ',' ',' '], 
        [' ',' ',' '], 
        [' ',' ',' ']
        ]

def board_sheet(clean_sheet):
    print(SEPARETOR)
    for row in clean_sheet:
    #if i didn't use sign already lower:
    #print(f" {colored_signs(row[0])} | {colored_signs(row[1])} | {colored_signs(row[2])}") 
    #row = 0 ->   [0][0]     [0][1]     [0][2]
        print(f" {row[0]} | {row[1]} | {row[2]}")
        print(SEPARETOR)

def colored_signs(mark):
    color = 'red' if mark == SIGN1 else 'green'
    return colored(mark,color)
    """less elegant
    if mark == SIGN1:
        return colored(mark, 'red')
    return colored(mark, 'green')
    """
# another vertion of creating the board
"""
for r in range(0,ROWS):
        for c in  range(0,COLUMNS):
            if c == 2: 
                print(f"{clean_sheet[r][c]:2}",end="")
            else:
                print(f"{clean_sheet[r][c]:2}|",end="")
        print("\n--+--+--")
"""
# bad version of chacking the winer
"""
        # checks rows,columns and diagonals
        if ((clean_sheet[0][0] == clean_sheet[0][1] ==  clean_sheet[0][2] != ' ') or \
            (clean_sheet[1][0] == clean_sheet[1][1] == clean_sheet[1][2] != ' ') or \
            (clean_sheet[2][0] == clean_sheet[2][1] ==  clean_sheet[2][2] != ' ')) or \
            ((clean_sheet[0][0] == clean_sheet[0][1] == clean_sheet[0][2] != ' ') or \
            (clean_sheet[1][0] == clean_sheet[1][1] == clean_sheet[1][2] != ' ') or \
            (clean_sheet[2][0] == clean_sheet[2][1] == clean_sheet[2][2] != ' ')) or \
            ((clean_sheet[0][0] == clean_sheet[1][1] == clean_sheet[2][2] != ' ') or \
            (clean_sheet[0][2] == clean_sheet[1][1] == clean_sheet[2][0] != ' ')):
            if now_plays == PLAYER2:
                print(f"Player {PLAYER2} won")
                break
            else:
                print(f"Player {PLAYER1} won")
                break
    # checks if board is full  
    if (clean_sheet[0][0] != ' ' and clean_sheet[0][1] != ' ' and clean_sheet[0][2] != ' ' and
        clean_sheet[1][0] != ' ' and clean_sheet[1][1] != ' ' and clean_sheet[1][2] != ' ' and
        clean_sheet[2][0] != ' ' and clean_sheet[2][1] != ' ' and clean_sheet[2][2] != ' '):
        print("Board is full")
"""

def is_full(clean_sheet):
    for row in clean_sheet:
        if ' ' in row:
            return False
        
    return True


def check_winner(clean_sheet):
    #check rows
    for row in clean_sheet:
        if row[0] == row[1] == row[2] != ' ':
            return True
        
    #check columns    
    for column in range(COLUMNS):
        if clean_sheet[0][column] == clean_sheet[1][column] == clean_sheet[2][column] != ' ':
            return True
        
    #check diagonals
    if clean_sheet[0][0] == clean_sheet[1][1] == clean_sheet[2][2] != ' ' or \
        clean_sheet[0][2] == clean_sheet[1][1] == clean_sheet[2][0] != ' ':
        return True
    
    return False

def get_row_column_position(prompt):
    while True:
        try:
            position = int(input(prompt))
            if position<0 or position>2:
                raise ValueError
            return position
        except ValueError:
            print("Invalid input!")

def player_move(now_plays,sign):
    print(f"Player {now_plays}'s turn")
    while True:
        row_step = get_row_column_position("Enter row (0-2): ")
        column_step = get_row_column_position("Enter column (0-2): ")

        if clean_sheet[row_step][column_step] == ' ':
            clean_sheet[row_step][column_step] = sign
            break 

        print("This spot is already taken")

def main():
    board_sheet(clean_sheet)

    now_plays = PLAYER1
    sign = SIGN1
    
    while True:  
        player_move(now_plays,colored_signs(sign))
        board_sheet(clean_sheet)
        
        if check_winner(clean_sheet):
            print(f"Player {now_plays} won")
            break
        
        if is_full(clean_sheet):
            print("The sheet is fully filed")
            break

        now_plays = PLAYER2 if now_plays == PLAYER1 else PLAYER1
        sign = SIGN2 if sign == SIGN1 else SIGN1


if __name__ == '__main__':
    main()

'''
while steps_numer:
    if now_plays == PLAYER2:
        print(f"Player {PLAYER2}'s turn")
        while True:
            try:
                row_step = int(input("Enter row (0-2): "))
                if row_step<0 or row_step>=ROWS:
                        raise ValueError  
                column_step = int(input("Enter column (0-2): "))      
                if row_step<0 or row_step>=COLUMNS:
                    raise ValueError
                if clean_sheet[row_step][column_step] != ' ':
                    print("This spot is already taken")
                else:
                    break
            except ValueError:
                    print("Invalid input!")
        clean_sheet[row_step][column_step] = SIGN2
        now_plays = PLAYER1        

    else:
        print(f"Player {PLAYER1}'s turn")
        while True:
            try:
                row_step = int(input("Enter row (0-2): "))
                if row_step<0 or row_step>=ROWS:
                        raise ValueError  
                column_step = int(input("Enter column (0-2): "))      
                if row_step<0 or row_step>=COLUMNS:
                    raise ValueError
                if clean_sheet[row_step][column_step] != ' ':
                    print("This spot is already taken")
                else:
                    break
            except ValueError:
                    print("Invalid input!")
        clean_sheet[row_step][column_step] = SIGN2
        now_plays = PLAYER2
'''