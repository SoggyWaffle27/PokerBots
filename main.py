import MainBot
import deck

# Example usage
deck = deck.CardDeck()
cards = deck.draw(5)
print("Drawn cards:", cards)
print("Cards left:", deck.size())
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']

bot1 = MainBot.Bot(1, 1, 10, 1000, 10000, seat = 1, hands = 1)
#print(bot1.bet())
bot1.stats
bot1.calcHands(deck, 1,1,1)
bot1.hand(cards)

#♠️♥️♦️♣️