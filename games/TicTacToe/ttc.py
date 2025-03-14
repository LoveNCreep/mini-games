gameboard = [' ',' ',' ',' ',' ',' ',' ',' ',' ']

def board_scanner():
    temp = 0
    for i in range(len(gameboard)):
        if(gameboard[i] != 0):
            temp = 1
        else:
            temp = 0
    return temp

def display_gameboard():
    for i in range(0, len(gameboard), 3):
        print(gameboard[i:i+3])

def user_input1():
    input_p1 = input("Put your character: ")
    column_player1 = int(input("put the column number: "))
    gameboard[column_player1-1] = input_p1

def user_input2():
    input_p2 = input("Put your character: ")
    column_player2 = int(input("put the column number: "))
    gameboard[column_player2-1] = input_p2

def game_logic():
    winner = 0
    win_conditions = [
        (0, 1, 2), #row 1
        (3, 4, 5), #row 2
        (6, 7, 8), #row 3

        (0, 3, 6), #column 1
        (1, 4, 7), #column 2
        (2, 5, 8), #column 3

        (0, 4, 8), #diagonal 1
        (2, 4, 6), #diagonal 2
    ]

    for a, b, c in win_conditions:
        if gameboard[a] == 'x' and gameboard[b] == 'x' and gameboard[c] == 'x':
            print("Player 1 wins")            
            return
        elif gameboard[a] == 'o' and gameboard[b] == 'o' and gameboard[c] == 'o':
            print("Player 2 wins")            
            return
    print("No winner yet")            

temp = board_scanner()
while temp == 1:

    display_gameboard()
    user_input1()
    display_gameboard()
    game_logic()

    user_input2()
    display_gameboard()
    game_logic()
    if temp == 0:
        break