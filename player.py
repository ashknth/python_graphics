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
        return die1, die2

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

def playOneGame():
    player = Player()
    while not player.isWinner() and not player.isLoser():
        input("Press Enter to roll the dice...")
        roll = player.rollDice()
        print(f"You rolled: {player.roll}")
        
        if player.isWinner():
            print("You win!")
        elif player.isLoser():
            print("You lose!")
    
    print(f"Total Rolls: {player.getRollsCount()}")

def playManyGames(num_games):
    for game in range(num_games):
        print(f"\nPlaying Game {game + 1}:")
        playOneGame()

if __name__ == "__main__":
    num_games = int(input("Enter the number of games to play: "))
    playManyGames(num_games)
