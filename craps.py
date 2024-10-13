import tkinter as tk
import random

class Player:
    def __init__(self):
        self.roll = ""
        self.rolls_count = 0
        self.first_roll = False
        self.winner = False
        self.loser = False
        self.point = None  # Attribute to hold the point value

    def rollDice(self):
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        self.roll = f"{die1}, {die2}"
        self.rolls_count += 1
        
        total = die1 + die2
        self.updateGameState(total)
        return total

    def updateGameState(self, total):
        if not self.first_roll:
            self.first_roll = True
            # Handle the first roll logic
            if total in [7, 11]:
                self.winner = True
            elif total in [2, 3, 12]:
                self.loser = True
            else:
                self.point = total  # Establish the point
        else:
            # Handle subsequent rolls
            if self.winner or self.loser:
                return  # No further rolls can change the outcome

            if total == 7:
                self.loser = True
            elif total == self.point:  # if the established point is rolled again
                self.winner = True

    def getRollsCount(self):
        return self.rolls_count

    def isWinner(self):
        return self.winner

    def isLoser(self):
        return self.loser


class CrapsGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Craps Game")

        self.player = Player()

        # Create UI components
        self.dice_label = tk.Label(master, text="Dice: ", font=("Helvetica", 18))
        self.dice_label.pack()

        self.result_label = tk.Label(master, text="", font=("Helvetica", 18))
        self.result_label.pack()

        self.roll_button = tk.Button(master, text="Roll", command=self.roll_dice, font=("Helvetica", 14))
        self.roll_button.pack(pady=20)

        self.new_game_button = tk.Button(master, text="New Game", command=self.new_game, font=("Helvetica", 14))
        self.new_game_button.pack(pady=20)

    def roll_dice(self):
        total = self.player.rollDice()
        self.dice_label.config(text=f"Dice: {self.player.roll} (Total = {total})")
        
        if self.player.isWinner():
            self.result_label.config(text="You win!")
            self.roll_button.config(state=tk.DISABLED)
        elif self.player.isLoser():
            self.result_label.config(text="You lose!")
            self.roll_button.config(state=tk.DISABLED)

    def new_game(self):
        self.player = Player()  # Reset the player
        self.result_label.config(text="")
        self.roll_button.config(state=tk.NORMAL)
        self.dice_label.config(text="Dice: ")


if __name__ == "__main__":
    root = tk.Tk()
    game = CrapsGame(root)
    root.mainloop()
