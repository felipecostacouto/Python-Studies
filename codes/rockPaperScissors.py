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

print("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors")
player = int(input("Enter your choice: "))
roboto = random.randint(0, 2)
games_img = [rock, paper, scissors]

if player >= 3 or player < 0:
    print("You typed an invalid number, You lose !")

else:
    print(f"\nPlayer`s choice: {player}")
    print(games_img[player])

    print(f"Computer`s choice: {roboto}")
    print(games_img[roboto])

    # Rock
    if player == 0:
        if roboto == 0:
            print("Draw")
        elif roboto == 1:
            print("Roboto wins")
        else:
            print("Player wins")
    # Paper
    elif player == 1:
        if roboto == 0:
            print("Player wins")
        elif roboto == 1:
            print("Draw")
        else:
            print("Roboto wins")
    # Scissors
    else:
        if roboto == 0:
            print("Roboto wins")
        elif roboto == 1:
            print("Player wins")
        else:
            print("Draw")

