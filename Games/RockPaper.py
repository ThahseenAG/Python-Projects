
# Rock Paper Scissors
# for selecting computer choice

import random


def rockpaperscissors():
    Choices = ["rock", "paper", "scissors"]
    Computer_Choice = Choices[random.randint(0 , 2)]
    correct_choice = True

    while correct_choice:
        print("Please Input Your Choice [Rock! Paper! Scissors!]")
        User_Choice = input().lower()
        if User_Choice in Choices:
            correct_choice = False
            print("You Choose :", User_Choice)
            print("Computer Choose :", Computer_Choice)
            if User_Choice == Computer_Choice:
                print("Its A Tie !!!")
            elif User_Choice == 'rock':
                if Computer_Choice == 'scissors':
                    print("You Won!! :) Rock Crushes Scissor!!")
                else:
                    print("You Lost! :( Paper Beats Rock!!")
            elif User_Choice == 'paper':
                if Computer_Choice == 'rock':
                    print("You Won!! :) Paper Beats Rock!!")
                else:
                    print("You Lost! :( Scissor Cuts Paper!!")
            elif User_Choice == 'scissors':
                if Computer_Choice == 'paper':
                    print("You Won!! :) Scissor Cuts Paper!!")
                else:
                    print("You Lost! :( Rock Crushes Scissor!!")
            print("Want to play again?!! Press Y")
            continue_game = input().lower()
            if continue_game == 'y':
                rockpaperscissors()
            else:
                print("BYE!")
                break
        else:
            print("Invalid Choice")
            rockpaperscissors()
        return
rockpaperscissors()






