import random

def rock_paper_scissors():
    choices = ['Rock', 'Paper', 'Scissors']
    computer_choice = random.choice(choices)

    print("Welcome to Rock-Paper-Scissors!")
    player_choice = input("Enter your choice (Rock, Paper, Scissors): ")

    print(f"You chose {player_choice}, Computer chose {computer_choice}")

    if player_choice == computer_choice:
        print("It's a draw!")
    elif (player_choice == 'Rock' and computer_choice == 'Scissors') or \
         (player_choice == 'Scissors' and computer_choice == 'Paper') or \
         (player_choice == 'Paper' and computer_choice == 'Rock'):
        print("You win!")
    else:
        print("You lose!")

rock_paper_scissors()
