
# keep the same
from strongerHand import *
import deck

deck = deck.CardDeck()

# Draw initial cards (3 known cards)
cards = [('8', 'H'), ('A', 'S'), ('7', 'D')]#deck.draw(3)

# Construct full hand with 2 additional drawn cards
hand = [('A', 'S'), ('7', 'S'), ('8', 'H'), ('A', 'D'), ('7', 'D')]#[cards[0], cards[1], cards[2], deck.draw(1)[0], deck.draw(1)[0]]

# Exclude known cards from the remaining deck
known_cards = set(hand)  # Use a set to remove duplicates
deckL = deck.deck  # Get the remaining deck

# Compute best hand rank for the drawn cards
best_hand, hand_rank, high_card, top_card = findHand.best_hand(hand)
# Run probability calculation

# findHand.find(hand)
# print(probability_of_stronger_hand(findHand.best_hand(hand), cards, deckL, num_opponents=1, num_simulations=10000))

import pandas as pd
import ast

def parse_cards(card_str):
    """Convert card string (e.g., '6h, 8d') to tuple format [(6, 'H'), (8, 'D')]."""
    cards = card_str.split(', ')
    return [(int(card[:-1]) if card[:-1].isdigit() else 10 if card[:-1] == 'T' else 11 if card[:-1] == 'J' else 12 if card[:-1] == 'Q' else 13 if card[:-1] == 'K' else 14, card[-1].upper()) for card in cards]

def determine_round(pool):
    """Determine the betting round based on the number of community cards."""
    num_cards = len(pool)
    if num_cards == 3:
        return 1
    elif num_cards == 4:
        return 2
    elif num_cards == 5:
        return 3
    return 0

def prob(row):
    """Calculate probability using findHand.best_hand and probability_of_stronger_hand."""
    hand = row['Hand']
    pool = row['Pool']
    
    hand = hand + pool
    deckL = [(v, s) for v in range(2, 15) for s in "CDHS" if (v, s) not in cards]

    # Determine best hand
    ignore, hand_rank, high_card, top_card = findHand.best_hand(cards)
    
    # Construct full hand with 2 additional drawn cards
    hand = [('A', 'S'), ('7', 'S'), ('8', 'H'), ('A', 'D'), ('7', 'D')]
    
    known_cards = set(hand)
    deckL = deck.deck  # Get the remaining deck

    return probability_of_stronger_hand(findHand.best_hand(hand), pool, deckL, num_opponents=1, num_simulations=5000)

def process_csv(file_path, output_path):
    df = pd.read_csv(file_path, delimiter='\t')  # Assuming tab CSV
    
    # Convert card strings to (value, suit) tuples
    df['Hand'] = df['Hand'].apply(parse_cards)
    df['Pool'] = df['Pool'].apply(parse_cards)
    
    # Determine betting round
    df['Round'] = df['Pool'].apply(determine_round)
    
    # Calculate win probability using the updated prob function
    df['Win Probability'] = df.apply(prob, axis=1)

    # Save modified file
    df.to_csv(output_path, index=False, sep='\t')
    print(f"Processed file saved as {output_path}")

# Example usage:
process_csv("Extended_Poker_Data.csv", "output.csv")
