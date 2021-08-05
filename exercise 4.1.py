#Write your code below this line 👇
#Hint: Remember to import the random module first. 🎲

import random

print("Welcome. This is a coin toss programme.")
coin_side_chosen = int(input("Type 0 for Heads and 1 for Tails."))

if coin_side_chosen == 0:
  print("You chose Heads.")
else:
  print("You chose Tails.")

comp_coin_side_chosen = random.randint(0, 1)

if comp_coin_side_chosen == 0:
  print("Computer chose Heads.")
else:
  print("Computer chose Tails.")

if coin_side_chosen == comp_coin_side_chosen:
  print("You Won.")
else:
  print("You Lose.")
