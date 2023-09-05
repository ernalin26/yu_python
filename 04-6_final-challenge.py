import random

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

#Write your code below this line 👇
choice = [rock, paper, scissors]

prompt = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if prompt == 0:
  print(choice[0])
elif prompt == 1:
  print(choice[1])
elif prompt == 2:
  print(choice[2])

computer_choice = random.choice(choice)
print(f"Computer chose:\n{computer_choice}")

if prompt == computer_choice:
  print("It's a draw")
if prompt == choice[0] and computer_choice == choice[2]:
  print("You win")
elif prompt == choice[2] and computer_choice == choice[1]:
   print("You win")
elif prompt == choice[1] and computer_choice == choice[0]:
  print("You win")
else:
  print("You lose")