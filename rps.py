import random

print("This is a game of Rock, Paper, Scissors. Your opponent will be the computer, and you will earn a point for each victory or lose a point for each loss.")

print(" ")

name = input("Please begin by entering your name: ")

print("")

entry = input("Hi " + name + ", Please type 'Rock', 'Paper', or 'Scissors'. ")

rock = "Rock"
paper = "Paper"
scissors = "Scissors"

random_number = random.randint(1, 3)

if entry == "Rock":
    if random_number == 1:
        print("Your opponent played Rock. It's a tie!")
    elif random_number == 2:
        print("Your opponent played Paper. You lose!")
    else:
        print("Your opponent played Scissors. You win!")
elif entry == "Paper":
    if random_number == 1:
        print("Your opponent played Rock. You win!")
    elif random_number == 2:
        print("Your opponent played Paper. It's a tie!")
    else:
        print("Your opponent played Scissors. You lose!")
else:
    if random_number == 1:
        print("Your opponent played Rock. You lose!")
    elif random_number == 2:
        print("Your opponent played Paper. You win!")
    else:
        print("Your opponent played Scissors. It's a tie!")