import random

option = ("rock", "paper", "scissors")
playing = True

while playing:
    player = None
    comp = random.choice(option)

    while player not in option:
        player = input("Enter the option(rock,paper,scissors): ")

    print(f"Player  : {player}")
    print(f"Computer: {comp}")

    if player == comp:
        print("It's Tie")
    elif player == "rock" and comp == "scissors":
        print("You Win")
    elif player == "paper" and comp == "rock":
        print("You Win")
    elif player == "scissors" and comp == "paper":
        print("You Win")
    else:
        print("You Lose!")

    ply = input("Play Again? (Y/N):")
    while ply not in ['y', 'Y', 'n', 'N']:
        ply = input("Play Again? (Y/N):")

    if not ply.lower() == "y":
        playing = False

print("Thank You!")