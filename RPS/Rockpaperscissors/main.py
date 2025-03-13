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
    
    #function for difficulty input
    def get_difficulty_input(self):
        while True:
            try:
                difficulty_input = input("SELECT\n e. Easy\n h. Hard \n Your pick: ")
                if difficulty_input in ['E', 'e', 'H', 'h']:
                    return difficulty_input
                else:
                    print("Invalid input! Please select E, e, h or H.")
            except ValueError as e:
                print("Invalid input! Please select E, e, h or H.")

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

class game_cl:
    def __init__(self):
        self.game = RockPaperScissor()
        self.player_score = 0
        self.computer_score = 0

    def match_results(self, player_choice, computer_choice):
        if player_choice == computer_choice:
            print(f"Draw!\n Player Picks: {player_choice}, Computer Picks: {computer_choice}")
            print(f"\nPlayer Score: {self.player_score}, Computer Score: {self.computer_score}")
        elif (player_choice == 1 and computer_choice == 3) or (player_choice == 2 and computer_choice == 1) or (player_choice == 3 and computer_choice == 2):
            self.player_score += 1
            print(f"Player wins!\n Player Picks: {player_choice}, Computer Picks: {computer_choice}")
            print(f"\nPlayer Score: {self.player_score}, Computer Score: {self.computer_score}")
        else:
            self.computer_score += 1
            print(f"Computer wins!\n Player Picks: {player_choice}, Computer Picks: {computer_choice}")
            print(f"\nPlayer Score: {self.player_score}, Computer Score: {self.computer_score}")

    def display_game(self):
        difficulty_choice = self.game.get_difficulty_input()
        if difficulty_choice == 'E' or difficulty_choice == 'e':
            while self.player_score != 3 or self.computer_score != 3:
                if self.player_score == 3 or self.computer_score == 3:
                    break
                else:
                    player_choice = self.game.get_player_input()
                    computer_choice = self.game.easy_difficulty(player_choice)
                    self.match_results(player_choice, computer_choice)
        else:
            player_choice = self.game.get_player_input()
            computer_choice = self.game.hard_difficulty(player_choice)
            self.match_results(player_choice, computer_choice)
            while self.player_score != 3 or self.computer_score != 3:
                if self.player_score == 3 or self.computer_score == 3:
                    break
                else:
                    player_choice = self.game.get_player_input()
                    computer_choice = self.game.easy_difficulty(player_choice)
                    self.match_results(player_choice, computer_choice)


game_begins = game_cl()
game_begins.display_game()


