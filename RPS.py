player1Choice = input("Rock, Paper, Scisors?\n")
print(f"Player 1 choice {player1Choice}")
player2Choice = input("Rock, Paper, Scissors?\n")
print(f"Player 2 choice {player2Choice}")

if player1Choice == player2Choice:
    print("Tie!")
elif (player1Choice == "Rock" and player2Choice == "Scissors") or \
    (player1Choice == "Paper" and player2Choice == "Rock") or \
    (player1Choice == "Scissors" and player2Choice == "Paper"):
    print("Player 1 wins!")
else:
    print("Player 2 wins!")