import random

options = ("rock", "paper", "scissors")
running = True
 
while running:    
    
    user = None
    computer = random.choice(options)
    while user not in options:
        user = input("Enter an option (Rock, Paper,scissors) : ").lower()

    print(f"USER : {user}")
    print(f"Computer : {computer}")

    if user == computer:
        print("Its a Tie!")
    elif user == "rock" and computer == "scissors":
        print(f"You Win!")
    elif user == "scissors" and computer == "paper":
        print(f"You Win!")
    elif user == "paper" and computer =="rock":
        print(f"You Win!")
    else:
        print("You Lose!")


    if not input("Play again? (y/n): ").lower() == "y":
        running = False

print("Thanks your playing")
