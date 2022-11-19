import random

point = 0

print("This is a game of Rock, Paper, Scissors. Your opponent will be the computer, and you will earn a point for each victory or lose a point for each loss.")

print("")

name = input("Please begin by entering your name: ")

print("")

entry = input("Hi " + name + ", Please type 'Rock', 'Paper', or 'Scissors'. Type 'End' if you would like to end the current game. ").title()

while entry == entry:
    random_number = random.randint(1, 3)
    #1 = Rock
    #2 = Paper
    #3 = Scissors
    if entry == "End":
        print("")
        print("Your final score is: " + str(point) + ". Thanks for playing, " + name + "!")
        break
    elif entry == "Rock":
        if random_number == 1:
            print("")
            print("Your opponent played Rock. It's a tie!")
            print("You gained or lost no points! Your score is now: " + str(point))
        elif random_number == 2:
            print("")
            print("Your opponent played Paper. You lose!")
            point -= 1
            print("You lost a point! Your score is now: " + str(point))
        else:
            print("")
            print("Your opponent played Scissors. You win!")
            point += 1
            print("You gained a point! Your score is now: " + str(point))
    elif entry == "Paper":
        if random_number == 1:
            print("")
            print("Your opponent played Rock. You win!")
            point += 1
            print("You gained a point! Your score is now: " + str(point))
        elif random_number == 2:
            print("")
            print("Your opponent played Paper. It's a tie!")
            print("You gained or lost no points! Your score is now: " + str(point))
        else:
            print("")
            print("Your opponent played Scissors. You lose!")
            point -= 1
            print("You lost a point! Your score is now: " + str(point))
    elif entry == "Scissors":
        if random_number == 1:
            print("")
            print("Your opponent played Rock. You lose!")
            point -= 1
            print("You lost a point! Your score is now: " + str(point))
        elif random_number == 2:
            print("")
            print("Your opponent played Paper. You win!")
            point += 1
            print("You gained a point! Your score is now: " + str(point))
        else:
            print("")
            print("Your opponent played Scissors. It's a tie!")
            print("You gained or lost no points! Your score is now: " + str(point))
    else:
        print("")
        print("I do not recognize this input. Please check your spelling!")
    print("")
    entry = input("Hi " + name + ", Please type 'Rock', 'Paper', or 'Scissors'. Type 'End' if you would like to end the current game. ").title()