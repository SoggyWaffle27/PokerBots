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
action_pattern = re.compile(r"(\w+): (folds|calls|bets|raises|checks) (\d+)?")
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
        if action == "folds":
            amount = -1
        elif action == "checks":
            amount = 0
        else:
            amount = int(amount) if amount else 0  # Convert valid amounts
        
        current_hand["actions"].append({"player": player, "action": action, "amount": amount})
    
    elif pot_match := pot_pattern.match(line):
        current_hand["total_pot"] = int(pot_match.group(1))

# Add last hand
if current_hand:
    hands.append(current_hand)

# Convert to DataFrame
df = pd.DataFrame(hands)

# Extract nth entry (e.g., second hand, index 1)
def readline(n):
    if 0 <= n < len(df):
        nth_entry = df.iloc[n]
        # Extract relevant values
        hand_number = nth_entry["hand_number"]
        action_values = [action["amount"] for action in nth_entry["actions"]]
        total_pot = nth_entry["total_pot"]

        # Final formatted list
        result = [hand_number] + action_values + [total_pot]
        print(result)
    else:
        print("Error: Index out of range.")

for n in range(0, 3):
    readline(n)