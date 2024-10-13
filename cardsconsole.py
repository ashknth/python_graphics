class Card:
    def __init__(self, rank: str, suit: str) -> None:
        """Initializes a new Card object with a rank and suit."""
        self.rank = rank       # The rank of the card (e.g., "Ace", "2", "King")
        self.suit = suit       # The suit of the card (e.g., "Hearts", "Spades")
        self.faceup = False    # Card is face down by default

    def turn(self) -> None:
        """Turns the card over, changing its faceup status."""
        self.faceup = not self.faceup  # Flip the faceup status

    def __str__(self) -> str:
        """Returns a string representation of the card."""
        faceup_status = "Face up" if self.faceup else "Face down"
        return f"{self.rank} of {self.suit} - {faceup_status}"

# Example usage of the Card class
if __name__ == "__main__":
    card = Card("Ace", "Hearts")
    print(card)  # Should show: Ace of Hearts - Face down

    card.turn()
    print(card)  # Should show: Ace of Hearts - Face up

    card.turn()
    print(card)  # Should show: Ace of Hearts - Face down
