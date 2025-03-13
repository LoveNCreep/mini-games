gameboard = ['0','0','0','0','0','0','0','0','0']

player1_input = ""
player2_input = ""

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

def user_input():
    input_p1 = input("Put your character")
    gameboard[5] = input_p1

display_gameboard()
user_input()
display_gameboard()
print(board_scanner())

"""
1 2 3 
4 5 6
7 8 9

1 4 7
2 5 8
3 6 9

1 5 9
3 5 7
"""