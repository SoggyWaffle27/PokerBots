import os
import re
import pandas as pd

# Define file path
file_path = "TestData/pluribus_30.txt"

# Read file
with open(file_path, "r", encoding="utf-8") as file:
    raw_data = file.readlines()

# Initialize lists to store extracted data
hands = []
current_hand = {}
players = {}

# Regex patterns
hand_number_pattern = re.compile(r"PokerStars Hand #(\d+)")
player_pattern = re.compile(r"Seat (\d+): (\w+) \((\d+) in chips\)")
action_pattern = re.compile(r"(\w+): (folds|calls|bets|raises) (\d+)?")
pot_pattern = re.compile(r"Total pot (\d+)")

# Process each line
for line in raw_data:
    line = line.strip()
    
    if hand_number_match := hand_number_pattern.match(line):
        # Save previous hand
        if current_hand:
            hands.append(current_hand)
        # Start new hand
        current_hand = {"hand_number": hand_number_match.group(1), "actions": []}
    
    elif player_match := player_pattern.match(line):
        seat, player, chips = player_match.groups()
        players[player] = int(chips)
    
    elif action_match := action_pattern.match(line):
        player, action, amount = action_match.groups()
        current_hand["actions"].append({"player": player, "action": action, "amount": int(amount) if amount else 0})
    
    elif pot_match := pot_pattern.match(line):
        current_hand["total_pot"] = int(pot_match.group(1))

# Add last hand
if current_hand:
    hands.append(current_hand)

# Convert to DataFrame
df = pd.DataFrame(hands)

# Display DataFrame
import ace_tools as tools
tools.display_dataframe_to_user(name="Poker Hands Analysis", dataframe=df)
