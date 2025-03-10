import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error
import ast
import strongerHand, findHand, deck
from sklearn.preprocessing import MinMaxScaler

# Load dataset
file_path = "output.csv"
df = pd.read_csv(file_path, delimiter='\t')

# Drop unnecessary columns
df = df.drop(columns=['Unnamed: 1', 'Unnamed: 3'], errors='ignore')

# Ensure correct data types
df['Hand'] = df['Hand'].apply(ast.literal_eval)
df['Pool'] = df['Pool'].apply(ast.literal_eval)

df = df.sample(frac=1, random_state=42).reset_index(drop=True)

# Select features and target
features = ['Win Probability', 'Agro']  # Features to use
target = 'Bet'

# Scale 'Pot' separately
scaler = MinMaxScaler()
df['Pot'] = scaler.fit_transform(df[['Pot']])  # Scale only 'Pot' column

# Feature matrix
X = df[features + ['Pot']]  # Include the scaled 'Pot' column

# Target variable
y = df[target]  # Don't scale target

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Evaluate model
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)

print(f"Mean Absolute Error: {mae:.2f}")
print(f"Mean Squared Error: {mse:.2f}")
print(f"Root Mean Squared Error: {rmse:.2f}")


import matplotlib.pyplot as plt

show_graph = True

if show_graph:
    #Plot each feature against 'Bet' separately
    for feature in ['Win Probability']:#, 'Pot', 'Agro', 'Bluff', 'Payout (exc)', 'Round']:
        plt.figure(figsize=(6, 4))
        plt.scatter(df[feature], df['Bet'], alpha=0.5)
        plt.xlabel(feature)
        plt.ylabel('Bet')
        plt.title(f'Bet vs {feature}')
        plt.show()

deck = deck.CardDeck()

hand = [('6', 'C'), ('Q', 'S')]
pool = [('K', 'S'), ('7', 'S'), ('9', 'D'), ('J', 'C'), ('4', 'H')]
hand = hand + pool
deckL = [(v, s) for v in range(2, 15) for s in "CDHS" if (v, s) not in hand]
ignore, hand_rank, high_card, top_card = findHand.best_hand(hand)
deckL = deck.deck  # Get the remaining deck
new_pot = 20
Pot = scaler.transform(pd.DataFrame([[new_pot]], columns=['Pot'])).flatten()[0]  # ✅ Fix


new_data = pd.DataFrame({
    'Win Probability': [strongerHand.probability_of_stronger_hand(findHand.best_hand(hand), pool, deckL, num_opponents=1, num_simulations=5000)],
    #'Round': [2],
    'Agro': [0.3],
    'Pot': [Pot]
    #'Bluff': [0],
    #'Outcome': [0]  # Neutral estimate
})

predicted_bet = model.predict(new_data)
print(f"Predicted Bet: {predicted_bet[0]:.2f}")

# x = input("Card1:")
# y = input("Card2:")
# hand = [(x[0], x[1]), (y[0], y[1])]
# x = input("Card1:")
# y = input("Card2:")
# z = input("Card3:")
# pool = [(x[0], x[1]), (y[0], y[1]), (z[0], z[1])]
# pot = 0
# r = 0
# while True:
#     hand = hand + pool
#     deckL = [(v, s) for v in range(2, 15) for s in "CDHS" if (v, s) not in hand]
#     ignore, hand_rank, high_card, top_card = findHand.best_hand(hand)
#     deckL = deck.deck  # Get the remaining deck
#     pot += int(input('Pot: '))
#     new_data = pd.DataFrame({
#         'Win Probability': [strongerHand.probability_of_stronger_hand(findHand.best_hand(hand), pool, deckL, num_opponents=1, num_simulations=5000)],
#         'Pot': [pot],
#         'Round': [len(pool) - 2 + r],
#         'Agro': [0.3]
#         #'Bluff': [0],
#         #'Outcome': [0]  # Neutral estimate
#     })

#     predicted_bet = model.predict(new_data)
#     pot += (int(predicted_bet[0]) % 5) * 5
#     print(f"Predicted Bet: {predicted_bet[0]:.2f}")
#     r += 1
#     h = input("Card3:")
#     pool = pool + [(h[0], h[1])]
#     print(pot)
#     print(pool)

