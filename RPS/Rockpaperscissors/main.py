import random


class RockPaperScissor:

    #Choices

    #Sets the probability of computer; losing is 5 out of 10, 2 out of 10 for draw, and 3 out of 10 in winning
    easy_rock =  [3, 1, 2, 3, 2, 1, 3, 3, 2, 3]
    easy_paper = [1, 2, 1, 3, 1, 2, 3, 1, 1, 3]
    easy_scissors = [2, 3, 2, 1, 2, 1, 2, 1, 2, 3]

    #Sets the probability of computer; losing 1 in 10, 5 out of 10 for draw, and 4 out of 10 in winning
    hard_rock = [3, 1, 2, 1, 2, 1, 2, 2, 1, 1]
    hard_paper = [1, 2, 3, 2, 3, 2, 2, 2, 3, 3]
    hard_scissors = [2, 3, 1, 1, 3, 1, 3, 1, 3, 3]

    #function for computer choices
    def get_computer_choice(self):
        return random.randint(0,9)

    #function for player input
    def get_player_input(self):
         while True:
            try:
                player_input = int(input("SELECT\n 1. ROCk\n 2. PAPER\n 3. SCISSORS \n Your pick: "))
                if player_input in [1, 2, 3]:
                    return player_input
                else:
                    print("Invalid input! Please select 1, 2, or 3.")
            except ValueError:
                print("Invalid input! Please enter a number.")
    
    #Easy Logic    
    def easy_difficulty(self, player_choice):
        temp = self.get_computer_choice()
        if player_choice == 1: #Rock
            computer_choice = self.easy_rock[temp]
        elif player_choice == 2: #Paper
            computer_choice = self.easy_paper[temp]
        elif player_choice == 3: #Scissors
            computer_choice = self.easy_scissors[temp]
        else:
            computer_choice = 0
        return computer_choice
    
        #Hard Logic    
    def hard_difficulty(self, player_choice):
        temp = self.get_computer_choice()
        if player_choice == 1: #Rock
            computer_choice = self.hard_rock[temp]
        elif player_choice == 2: #Paper
            computer_choice = self.hard_paper[temp]
        elif player_choice == 3: #Scissors
            computer_choice = self.hard_scissors[temp]
        else:
            computer_choice = 0
        return computer_choice

    def match_results(self, player_choice, computer_choice):
        if player_choice == computer_choice:
            print(f"Draw!\n Player Picks: {player_choice}, Computer Picks: {computer_choice}")
        elif (player_choice == 1 and computer_choice == 3) or (player_choice == 2 and computer_choice == 1) or (player_choice == 3 and computer_choice == 2):
            print(f"Player wins!\n Player Picks: {player_choice}, Computer Picks: {computer_choice}")
        else:
            print(f"Computer wins!\n Player Picks: {player_choice}, Computer Picks: {computer_choice}")


class easy_difficulty_cl:
    def __init__(self):
        self.game = RockPaperScissor()

    def display_game(self):
        player_choice = self.game.get_player_input()
        computer_choice = self.game.easy_difficulty(player_choice)
        
        self.game.match_results(player_choice, computer_choice)


game_begins = easy_difficulty_cl()
game_begins.display_game()