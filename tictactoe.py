# Project 3 - Tic-Tac-Toe Simulator
#
# Name: Kenneth Liu
# Instructor: S. Einakian
# Section: 01,02



import tictactoeFuncs
import random


#gobal variables
Player=tictactoeFuncs.show_welcome()
counter=0
board = ["", "", "", "", "", "", "", "", ""]



#user wants to play against computer
if Player==1:
    print("The board will look like this:")
    tictactoeFuncs.createBoard()
    print("The empty board:")
    tictactoeFuncs.printBoard(board)
    letter = tictactoeFuncs.pickLetter()
    if letter=="X":
        while True:
            #turn starts at 1 and increments by 1
            counter = tictactoeFuncs.turnCount(counter)
            print("Turn number ", counter)
            # counter starts at 1 so 1%2 always = 1, X always starts
            if counter % 2 == 1:
                letter="X"
                tictactoeFuncs.getInput(letter,board)
                print("The board will look like this:")
                tictactoeFuncs.printBoard(board)
            elif counter % 2 == 0:
                letter="O"
                #places random O in index 0-8 only if it is empty (" ")
                while True:
                    valuetown=random.randint(0,8)
                    if board[valuetown]=="":
                        board[valuetown]=letter
                        break
                print("The board will look like this:")
                tictactoeFuncs.printBoard(board)
            # checks for winner, if there is winner, break
            if tictactoeFuncs.checkWin(tictactoeFuncs.checkRows(board), tictactoeFuncs.checkCols(board), tictactoeFuncs.checkDiags(board)) == True:
                break
            #there can only be 9 turns so it's a draw if check win is not true
            elif counter==9:
                print("It's a draw!")
                break


    if letter=="O":
        while True:
            #turn starts at 1 and increments by 1
            counter = tictactoeFuncs.turnCount(counter)
            print("Turn number ", counter)
            #counter starts at 1 so 1%2 always = 1, X always starts
            if counter % 2 == 1:
                letter="X"
                #places a X in a random index(0-8) only if it is empty(" ")
                while True:
                    valuetown=random.randint(0,8)
                    if board[valuetown]=="":
                        board[valuetown]=letter
                        break
                print("The board will look like this:")
                tictactoeFuncs.printBoard(board)
            elif counter % 2 == 0:
                letter="O"
                tictactoeFuncs.getInput(letter, board)
                print("The board will look like this:")
                tictactoeFuncs.printBoard(board)
            if tictactoeFuncs.checkWin(tictactoeFuncs.checkRows(board), tictactoeFuncs.checkCols(board), tictactoeFuncs.checkDiags(board)) == True:
                break
            # there can only be 9 turns so it's a draw if check win is not true
            elif counter==9:
                print("It's a draw!")
                break



#if user wants to play with another person
if Player==2:
    #print instructions
    print("The board will look like this:")
    tictactoeFuncs.createBoard()
    print("The empty board:")
    tictactoeFuncs.printBoard(board)
    letter=tictactoeFuncs.pickLetter()
    while True:
        #turn starts at 1 and increments by 1
        counter = tictactoeFuncs.turnCount(counter)
        print("Turn number ", counter)
        #if counter%2==0, letter is O and if counter%2==1, letter is X
        letter = 'O' if counter % 2 == 0 else "X"
        tictactoeFuncs.getInput(letter,board)
        print("The board will look like this:")
        tictactoeFuncs.printBoard(board)
        if tictactoeFuncs.checkWin(tictactoeFuncs.checkRows(board), tictactoeFuncs.checkCols(board), tictactoeFuncs.checkDiags(board)) == True:
            break
        # there can only be 9 turns so it's a draw if check win is not true
        elif counter==9:
            print("It's a draw!")
            break
