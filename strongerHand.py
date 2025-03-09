import random
import findHand
from itertools import combinations

def probability_of_stronger_hand(tup, pool_cards, deck, num_opponents=1, num_simulations=10000):
    """
    Estimates the probability that at least one opponent has a stronger hand than yours.

    :param your_rank: Hand rank (0-8).
    :param your_high_card: High card if applicable (None if not needed).
    :param your_top_card: Top card of a straight/flush if applicable (None otherwise).
    :param pool_cards: List of community cards (0-5 cards).
    :param deck: Remaining deck after known cards are removed.
    :param num_opponents: Number of opponents.
    :param num_simulations: Number of random simulations to run.
    :return: Probability that at least one opponent has a stronger hand.
    """
    your_rank, your_high_card, your_top_card = tup[1], tup[2], tup[3]
    remaining_deck = [card for card in deck if card not in pool_cards]  # Ensure pool cards are removed
    stronger_simulations = 0  # Counter for how often at least one opponent has a better hand

    for _ in range(num_simulations):
        at_least_one_better = False  # Track if any opponent has a better hand

        for _ in range(num_opponents):
            if len(remaining_deck) < 2:
                continue  # Avoid sampling errors if not enough cards remain

            # Assign a random 2-card hand to the opponent
            opponent_hand = random.sample(remaining_deck, 2)

            # Ensure the opponent has a full 7-card hand
            num_needed = 7 - (len(opponent_hand) + len(pool_cards))
            additional_cards = random.sample([c for c in remaining_deck if c not in opponent_hand], num_needed) if num_needed > 0 else []

            opponent_full_hand = opponent_hand + pool_cards + additional_cards

            # Determine the best 5-card hand for the opponent
            opponent_best_hand, opponent_rank, opponent_high_card, opponent_top_card = findHand.best_hand(opponent_full_hand)

            # Compare ranks first
            if opponent_rank > your_rank:
                at_least_one_better = True
                break  # Stop checking this simulation if an opponent is already better

            # Handle ties: Use the correct comparison logic
            if opponent_rank == your_rank:
                if your_rank >= 4:
                    if opponent_top_card and your_top_card and opponent_top_card > your_top_card:
                        at_least_one_better = True
                        break
                    
                
                elif opponent_high_card and your_top_card and opponent_high_card > your_top_card:
                        at_least_one_better = True
                        break
                
                # Compare top cards for straight/flush ties
                elif opponent_top_card and your_top_card and opponent_top_card > your_top_card:
                    at_least_one_better = True
                    break

        # If at least one opponent was better in this simulation, count it
        if at_least_one_better:
            stronger_simulations += 1

    # Compute probability
    probability = stronger_simulations / num_simulations
    return probability