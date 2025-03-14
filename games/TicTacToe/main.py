class TictacToe:
    def __init__(self):
        #Variables
        self.gameboard = [" "] * 9
        self.temp = self.winner = 0
        self.player1, self.player2 = 1, 2
        self.user_input = ""

    #Function that displays the gameboard
    def displays_gameboard(self):
        for i in range(0, len(self.gameboard), 3):
            print(self.gameboard[i:i+3])
    
    #Function that returns 1 if the board is full
    def board_scanner(self):
        for i in range(len(self.gameboard)):
            if (self.gameboard[i] != 0):
                self.temp = 1
            else:
                self.temp = 0
        return self.temp
    
    #Game Logic
    def game_logic(self):
        self.temp = 0
        win_conditions = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8), #row 1, 2, 3
            (0, 3, 6), (1, 4, 7), (2, 5, 8), #column 1, 2, 3
            (0, 4, 8), (2, 4, 6), #diagonal 1, 2
        ]
        for a, b, c in win_conditions:
            if self.gameboard[a] == 'x' and self.gameboard[b] == 'x' and self.gameboard[c] == 'x':
                self.temp = 1
            elif self.gameboard[a] == 'o' and self.gameboard[b] == 'o' and self.gameboard[c] == 'o':
                self.temp = 2
        
        return self.temp
    
    #functions that get user's prompt
    def get_player1_input(self):
        while True:
            try:
                column_number = int(input("Enter the column number: "))
                player_input = input("Prompt x or X: ")
                
                if column_number > 9 or column_number < 1:
                    print("Error! Column out of range!")
                    continue

                if player_input not in ['x', 'X']:
                    print("Invalid Input!")
                    continue

                if self.gameboard[column_number-1] == " ":
                    self.gameboard[column_number-1] = player_input
                    break

                else:
                    print("Error! Column was occupied")

            except ValueError:
                print("Invalid Input!")

    def get_player2_input(self):
        while True:
            try:
                column_number = int(input("Enter the column number: "))
                player_input = input("Prompt o or O: ")
                
                if column_number > 9 or column_number < 1:
                    print("Error! Column out of range!")
                    continue

                if player_input not in ['o', 'O']:
                    print("Invalid Input!")
                    continue

                if self.gameboard[column_number-1] == " ":
                    self.gameboard[column_number-1] = player_input
                    break

                else:
                    print("Error! Column was occupied")

            except ValueError:
                print("Invalid Input!")

class game_begins:
    def __init__(self):
        self.game = TictacToe()
        self.temp = 1
        self.winner = 0
        
    def game_loop(self):
        while self.temp != 0 or (self.winner != 1 or self.winner != 2):

            #displays the board
            self.game.displays_gameboard()

            self.game.get_player1_input()
            self. winner = self.game.game_logic()
            print(self.winner)
            self.temp = self.game.board_scanner()

            self.game.displays_gameboard()

            self.game.get_player2_input()
            self.winner = self.game.game_logic()
            print(self.winner)
            self.temp = self.game.board_scanner()






game = game_begins()
game.game_loop()

        