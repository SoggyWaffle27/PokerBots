import random

class CardDeck:
    def __init__(self):
        """Initialize a standard 52-card deck."""
        self.suits = ['D', 'C', 'S', 'H']
        self.ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        self._reset_deck()

    def _reset_deck(self):
        """Resets the deck to a full 52 cards."""
        self.deck = [(rank, suit) for suit in self.suits for rank in self.ranks]
        self.shuffle()

    def shuffle(self):
        """Shuffles the deck."""
        random.shuffle(self.deck)

    def draw(self, num=1):
        """Draws `num` cards from the deck."""
        if num > len(self.deck):
            raise ValueError("Not enough cards left to draw.")
        return [self.deck.pop() for _ in range(num)]

    def size(self):
        """Returns the number of remaining cards in the deck."""
        return len(self.deck)

    def reset(self):
        """Resets and reshuffles the deck."""
        self._reset_deck()
