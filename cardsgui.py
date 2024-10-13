import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import random
import os

# Card class to represent individual cards
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

    def get_image(self) -> str:
        """Returns the image filename associated with the card."""
        if self.faceup:
            # Mapping ranks to filenames (1-13 for Ace-King)
            rank_map = {'Ace': '1', '2': '2', '3': '3', '4': '4', '5': '5',
                        '6': '6', '7': '7', '8': '8', '9': '9', '10': '10',
                        'Jack': '11', 'Queen': '12', 'King': '13'}
            rank_number = rank_map[self.rank]
            suit_map = {'Hearts': 'h', 'Diamonds': 'd', 'Clubs': 'c', 'Spades': 's'}
            suit_letter = suit_map[self.suit]
            return f"DECK/{rank_number}{suit_letter}.png"  # Path to card image
        else:
            return "DECK/b.png"  # Path to the back image


# Deck class to manage deck operations
class Deck:
    def __init__(self) -> None:
        """Initializes a new deck of cards."""
        self.cards = []
        self.create_deck()

    def create_deck(self) -> None:
        """Creates a standard 52-card deck."""
        ranks = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        self.cards = [Card(rank, suit) for rank in ranks for suit in suits]

    def shuffle(self) -> None:
        """Shuffles the deck of cards."""
        random.shuffle(self.cards)

    def deal_card(self) -> Card:
        """Deals one card from the deck."""
        if self.cards:
            card = self.cards.pop()
            card.turn()  # Turn the card face up
            return card
        return None


# GUI class to handle card display and user interaction
class CardGUI:
    def __init__(self, master) -> None:
        self.master = master
        self.master.title("Cards Demo")
        self.master.geometry("350x350")

        # Create a deck instance
        self.deck = Deck()
        self.deck.shuffle()

        # Set up canvas to display card image
        self.canvas = tk.Canvas(master, width=200, height=250, bg="white", bd=2, relief="solid")
        self.canvas.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

        # Buttons
        self.deal_button = tk.Button(master, text="Deal", command=self.deal_card)
        self.deal_button.grid(row=1, column=0, padx=10)

        self.shuffle_button = tk.Button(master, text="Shuffle", command=self.shuffle_deck)
        self.shuffle_button.grid(row=1, column=1, padx=10)

        self.new_deck_button = tk.Button(master, text="New deck", command=self.new_deck)
        self.new_deck_button.grid(row=1, column=2, padx=10)

        # Display backside of the card initially
        self.backside_image = self.load_card_image('DECK/b.png')
        self.display_card_image(self.backside_image)

    def load_card_image(self, image_filename: str) -> ImageTk.PhotoImage:
        """ Helper function to load a card image """
        try:
            image = Image.open(image_filename)
            image = image.resize((150, 225), Image.LANCZOS)
            return ImageTk.PhotoImage(image)
        except FileNotFoundError:
            messagebox.showerror("Error", f"Image file {image_filename} not found.")
            return None

    def display_card_image(self, card_image: ImageTk.PhotoImage) -> None:
        """ Helper function to display card image on canvas """
        if card_image:
            self.canvas.create_image(100, 125, image=card_image)
            self.canvas.image = card_image  # Keep reference to prevent garbage collection

    def deal_card(self) -> None:
        """ Deals a card and displays it on the canvas """
        card = self.deck.deal_card()
        if card:
            image_filename = card.get_image()
            card_image = self.load_card_image(image_filename)
            if card_image:
                self.display_card_image(card_image)
        else:
            messagebox.showinfo("Info", "No more cards to deal.")

    def shuffle_deck(self) -> None:
        """ Shuffles the deck """
        self.deck.shuffle()
        messagebox.showinfo("Info", "Deck shuffled!")

    def new_deck(self) -> None:
        """ Resets the deck """
        self.deck = Deck()
        self.deck.shuffle()
        self.display_card_image(self.backside_image)
        messagebox.showinfo("Info", "New deck created!")


# Main function to run the GUI application
if __name__ == "__main__":
    root = tk.Tk()
    gui = CardGUI(root)
    root.mainloop()
