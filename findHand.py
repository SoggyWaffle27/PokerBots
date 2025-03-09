from itertools import combinations

def hand_rank(hand):
    """
    Returns a ranking tuple for a given 2-7 card hand.
    Works with 2 to 7 card inputs.
    """
    vals = {
        "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, 
        "J": 11, "Q": 12, "K": 13, "A": 14, "11":11, "12": 12, "13":13,"14":14
    }
    values = sorted([vals[str(card[0])] for card in hand], reverse=True)  # Extract values
    suits = [card[1] for card in hand]  # Extract suits
    
    value_counts = {v: values.count(v) for v in set(values)}
    sorted_counts = sorted(value_counts.items(), key=lambda x: (-x[1], -x[0]))  # Sort by frequency, then by value

    is_flush = len(set(suits)) == 1 if len(hand) >= 5 else False
    is_straight = len(hand) >= 5 and (values == list(range(values[0], values[0] - 5, -1)) or values == [14, 5, 4, 3, 2])
    top_straight_card = values[0] if is_straight else (5 if values == [14, 5, 4, 3, 2] else None)  # Handle A-5 straight

    # Special handling for <5 cards
    if len(hand) < 5:
        if sorted_counts[0][1] == 3:
            return (3, None, sorted_counts[0][0])  # Three of a Kind
        if sorted_counts[0][1] == 2:
            return (1, max((v for v in values if v != sorted_counts[0][0]), default=None), sorted_counts[0][0])  # One Pair
        return (0, values[0], None)  # High Card
    
    # Standard 5-card+ hand ranking
    if is_flush and is_straight:
        return (8, None, values[0])  # Straight Flush
    if sorted_counts[0][1] == 4:
        return (7, None, sorted_counts[0][0])  # Four of a Kind
    if sorted_counts[0][1] == 3 and sorted_counts[1][1] == 2:
        return (6, None, sorted_counts[0][0])  # Full House
    if is_flush:
        return (5, None, values[0])  # Flush
    if is_straight:
        return (4, None, top_straight_card)  # Straight
    if sorted_counts[0][1] == 3:
        return (3, None, sorted_counts[0][0])  # Three of a Kind
    if sorted_counts[0][1] == 2 and sorted_counts[1][1] == 2:
        return (2, max((v for v in values if v not in [sorted_counts[0][0], sorted_counts[1][0]]), default=None), sorted_counts[0][0])  # Two Pair
    if sorted_counts[0][1] == 2:
        return (1, max((v for v in values if v != sorted_counts[0][0]), default=None), sorted_counts[0][0])  # One Pair
    return (0, values[0], None)  # High Card

from itertools import combinations

def best_hand(cards):
    """
    Given 2-7 cards, finds the best possible 5-card poker hand.
    If there are fewer than 5 cards, it ranks them accordingly.
    Returns (best_hand, rank, high_card, top_card).
    """
    if len(cards) < 2:
        raise ValueError("At least 2 cards are required to determine a hand.")

    if len(cards) >= 5:
        best = max(combinations(cards, 5), key=hand_rank)
        rank, high_card, top_card = hand_rank(best)
        return best, rank, high_card, top_card
    else:
        # If fewer than 5 cards, use all available cards and rank them
        rank, high_card, top_card = hand_rank(cards)

        # Ensure we return a valid 5-card format
        best = sorted(cards, key=lambda card: hand_rank([card]), reverse=True)  # Sort by strength
        return best, rank, high_card, top_card


def find(cards):
    """
    Prints the best hand ranking from 2 to 7 given cards.
    """
    best, rank, high_card, top_card = best_hand(cards)

    RANK_NAMES = {
        0: "High Card",
        1: "One Pair",
        2: "Two Pair",
        3: "Three of a Kind",
        4: "Straight",
        5: "Flush",
        6: "Full House",
        7: "Four of a Kind",
        8: "Straight Flush"
    }

    print(f"Cards: {cards}")
    print(f"Best hand: {best}")
    print(f"Hand rank: {RANK_NAMES[rank]}")
    print(f"High card: {high_card if high_card else 'N/A'}")
    print(f"Top card (for straights): {top_card if top_card else 'N/A'}")

