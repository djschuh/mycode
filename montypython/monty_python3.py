#!/usr/bin/python3
turn = 0
answer = " "

while turn < 3 and (answer != "Brian" and answer != "Shrubbery"):
    turn += 1     # increase the round counter by 1
    answer = input('Finish the movie title, "Monty Python\'s The Life of ______": ')
    answer=answer.capitalize()
    if answer == "Brian": # logic to check if user gave correct answer
        print("Correct!")
    elif answer == "Shrubbery":
        print("You gave the super secret answer!")
    elif turn == 3:    # logic to ensure round has not yet reached 3
        print("Sorry, the answer was Brian.")
    else:                 # if answer was wrong
        print("Sorry. Try again!")
