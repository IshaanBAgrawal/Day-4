rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random

print("Welcome to the stone, paper and scissors game.")

play_again = True
while play_again:
  user_choice = int(input("What do you choose? Type 0 for rock, 1 for paper and 2 for scissors. "))

  if user_choice == 0:
    print(f"You chose Rock.\n{rock}")
  elif user_choice == 1:
    print(f"You chose Paper.\n{paper}")
  elif user_choice == 2:
    print(f"You chose scissors.\n{scissors}")
  else:
    print("You Chose an Invalid Number.")

  computer_choice = random.randint(0 , 2)

  if user_choice >=3 or user_choice < 0:
    print("You lose.")
  elif computer_choice == 0:
    print(f"Computer chose Rock.\n{rock}")
  elif computer_choice == 1:
    print(f"Computer chose Paper.\n{paper}")
  else:
    print(f"Computer chose scissors.\n{scissors}")


  if user_choice == 0 and computer_choice == 2:
    print("You Won.")
  elif user_choice == 2 and computer_choice == 0:
    print("You lose.")
  elif user_choice == 2 and computer_choice == 1:
    print("You Won.")
  elif user_choice == 1 and computer_choice == 2:
    print("You Lose.")
  elif user_choice == 1 and computer_choice == 0:
    print("You Won.")
  elif user_choice == 0 and computer_choice == 1:
    print("You Lose.")
  elif user_choice == computer_choice:
    print("It's a draw.")
  else:
    print("")

  if input("Do you wanna play again? If yes, type 'y'. If no, type 'n'.") == 'n':
    play_again = False
