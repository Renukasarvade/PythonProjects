import random
get_random=random.randint(0 ,1)
if get_random == 1:
    print("heads")
else:
    print("tails")



friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
rand_friend = random.choice(list(friends))
print(rand_friend)


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

while True:
    try:
        print("\n0. Rock  1. Paper  2. Scissors  3. Exit")
        user = int(input("Enter your choice: "))

        # Exit condition
        if user == 3:
            print("Game exited.")
            break

        # Validate input
        if user not in [0,1, 2]:
            print("Invalid choice, try again.")
            continue

        # Computer choice
        computer = random.randint(0, 2)

        # Mapping numbers to names
        choices = {0: "Rock", 1: "Paper", 2: "Scissors"}

        print(f"You chose: {choices[user]}")
        print(f"Computer chose: {choices[computer]}")

        # Game logic
        if user == computer:
            print("It's a Draw!")

        elif (user == 0 and computer == 2) or \
             (user == 1 and computer == 0) or \
             (user == 2 and computer == 1):
            print("You Win!")

        else:
            print("Computer Wins!")

    except ValueError:
        print("Invalid input! Please enter a number.")
