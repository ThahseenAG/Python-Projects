import sys
import random


def printgameboard(Gameboard):
    print("\033[96m")
    for i in range(1, len(Gameboard) + 1):
        if i % 3 != 0:
            if Gameboard[i-1] == 'X' or Gameboard[i-1] =='O':
                print("\t", Gameboard[i - 1], "\t|", end="")
            else:
                print("\t", "-", "\t|", end="")
        else:
            if Gameboard[i - 1] == 'X' or Gameboard[i - 1] == 'O':
                print("\t", Gameboard[i - 1], "", end="\n")
            else:
                print("\t","-", "", end="\n")
            if i != len(Gameboard):
                print("\t----*-------*------")


def CheckWinner(GB):
    if GB[0] == GB[1] == GB[2] or \
            GB[0] == GB[3] == GB[6] or \
            GB[0] == GB[4] == GB[8] or \
            GB[3] == GB[4] == GB[5] or \
            GB[6] == GB[7] == GB[8] or \
            GB[2] == GB[5] == GB[8] or \
            GB[2] == GB[4] == GB[6] or \
            GB[1] == GB[4] == GB[7]:
        return True
    return False


def CreatingBoard():
    print('\033[95m'+"*********\033[94m\tHi!!! Welcome To The Game of Tic-Tac-Toe\t\033[95m********")
    print("\033[0m+++++++++\tBelow is the GameBoard with each position is marked with its number\t+++++++++"+'\033[96m')
    Gameboard = [i for i in range(1, 10)]
    Open_Position = [i for i in range(1, 10)]
    Selected_Position = []
    #printgameboard(Gameboard)
    for i in range(1, len(Gameboard) + 1):
        if i % 3 != 0:
            print("\t",Gameboard[i - 1], "\t|", end="")
        else:

            print("\t",Gameboard[i - 1], "", end="\n")
            if i != len(Gameboard):
                print("\t----*-------*------")
    PlayGame(Gameboard, Open_Position, Selected_Position)



def ComputerChoose(Gameboard, Open_Position, Selected_Position):
    print('\033[93m')
    GB = Gameboard[:]
    print("--------------")
    print(" Player O Plays!!")
    print("--------------")
    # Checking if it is computers first move
    if 'O' not in GB:
        position = random.choice(Open_Position)
        GB[position - 1] = 'O'
        Open_Position.remove(position)
        Selected_Position.append(position)
        printgameboard(GB)
        PlayGame(GB, Open_Position, Selected_Position)

    # checking if computer can be a winner
    for position in Open_Position:
        GB[position - 1] = 'O'
        result = CheckWinner(GB)
        if result:
            print("****** O Wins!!! *******")
            printgameboard(GB)
            sys.exit("****** O Wins!!! *******")
        GB[position - 1] = position

    GB = Gameboard[:]

    # Checking if the user can be a winner

    for position in Open_Position:
        GB[position - 1] = 'X'
        result = CheckWinner(GB)
        if result:
            GB[position - 1] = 'O'
            Open_Position.remove(position)
            Selected_Position.append(position)
            printgameboard(GB)
            PlayGame(GB, Open_Position, Selected_Position)
        GB[position - 1] = position

    GB_copy = Gameboard[:]
    GB = Gameboard[:]

    # Both Cannot be winner then selecting computers next move by checking which 2 moves can make computer win
    op = Open_Position[:]
    found = False
    for position in Open_Position:
        op.remove(position)
        GB_copy[position - 1] = 'O'
        for second_position in op:
            GB_copy[second_position - 1] = 'O'
            can_i_win = CheckWinner(GB_copy)
            if can_i_win:
                found = True
                GB[position - 1] = 'O'
                Open_Position.remove(position)
                Selected_Position.append(position)
                printgameboard(GB)
                PlayGame(GB, Open_Position, Selected_Position)
            else:
                GB_copy[second_position - 1] = second_position
        op.append(position)
    if not found:
        position = random.choice(Open_Position)
        GB[position - 1] = 'O'
        Open_Position.remove(position)
        Selected_Position.append(position)
        printgameboard(GB)
        PlayGame(GB, Open_Position, Selected_Position)


def PlayGame(Gameboard, Open_Position, Selected_Position):
    print("\033[92m")
    print("Select a position Player 'X'")
    position = input()
    try:
        position = int(position)
    except:
        print("Oops!  That was not a valid number.  Try again...")
        PlayGame(Gameboard, Open_Position, Selected_Position)
    if position not in Gameboard or position in Selected_Position:
        print("The position selected is invalid or already selected. Please select again...")
        PlayGame(Gameboard, Open_Position, Selected_Position)
    position = int(position)
    # Checking if it is the last Move
    if len(Open_Position) == 1:
        Gameboard[position - 1] = 'X'
        result = CheckWinner(Gameboard)
        if result:
            print("****** X Wins!!! *******")
            printgameboard(Gameboard)
            sys.exit("****** X Wins!!! *******")
        else:
            print("******Its A Tie!!!*******")
            printgameboard(Gameboard)
            sys.exit("******Its A Tie!!!*******")
    else:
        Gameboard[position - 1] = 'X'
        Open_Position.remove(position)
        Selected_Position.append(position)
        result = CheckWinner(Gameboard)
        if result:
            print("****** X Wins!! ********")
            printgameboard(Gameboard)
            sys.exit("****** X Wins!! ********")

        ComputerChoose(Gameboard, Open_Position, Selected_Position)


CreatingBoard()
