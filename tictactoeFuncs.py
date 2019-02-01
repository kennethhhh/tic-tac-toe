# Project 3 - Tic-Tac-Toe Simulator
#
# Name: Kenneth Liu
# Instructor: S. Einakian
# Section: 01,02
# Functions definitions comes here




#1 is playing with computer
#2 is playing with 2 users
def show_welcome():
    print("Welcome to Tic-Tac-Toe")
    print("Use numbers 1-9 to make your move in the corresponding cell numbers")
    play = int(input("Would you like to play with a (1)computer or (2)Player2?"))
    if play == 1:
        return(1)
    if play == 2:
        return(2)





#prints example board with numbers corresponding with the location
def createBoard():
    Start = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print("{0:^5}|{1:^5}|{2:^5}".format(Start[0], Start[1], Start[2]))
    print("-" * 17)
    print("{0:^5}|{1:^5}|{2:^5}".format(Start[3], Start[4], Start[5]))
    print("-" * 17)
    print("{0:^5}|{1:^5}|{2:^5}".format(Start[6], Start[7], Start[8]))




#prints updated board
def printBoard(board):
    print("{0:^5}|{1:^5}|{2:^5}".format(board[0], board[1], board[2]))
    print("-" * 17)
    print("{0:^5}|{1:^5}|{2:^5}".format(board[3], board[4], board[5]))
    print("-" * 17)
    print("{0:^5}|{1:^5}|{2:^5}".format(board[6], board[7], board[8]))
    return (board)




#asks user to pick a letter, if it is not X or O, it will give error and ask until X or O
def pickLetter():
    pick = input("Select your letter(X or O): ")
    if pick == "X":
        return (pick)
    elif pick == "O":
        return (pick)
    while pick != "X" or pick != "O":
        print("Invalid character. Please select X or O.")
        pick = input("Select your letter(X or O): ")
        if pick == "X":
            return (pick)
        elif pick == "O":
            return (pick)



#asks user where they would like to place X(if pick letter is X) or O(if pick letter is O)
#updates board list
#board[move-1] because index starts from 0, but example board starts at 1
def getInput(letter, board):
    # letter= pickletter()
    # board= printboard()
    if letter == "X":
        moveX = int(input("Where would you like to place your X(1-9)?"))
        while moveX < 1 or moveX > 9:
            print("Invalid move! Please try again.")
            moveX = int(input("Where would you like to place your X(1-9)?"))
        while board[moveX - 1] == "O" or board[moveX - 1] == "X":
            print("Invalid move! Location is already taken. Please try again.")
            moveX = int(input("Where would you like to place your X(1-9)?"))
        board[moveX - 1] = letter

    if letter == "O":
        moveO = int(input("Where would you like to place your O(1-9)?"))
        while moveO < 1 or moveO > 9:
            print("Invalid move! Please try again.")
            moveO = int(input("Where would you like to place your O(1-9)?"))
        while board[moveO - 1] == "O" or board[moveO - 1] == "X":
            print("Invalid move! Location is already taken. Please try again.")
            moveO = int(input("Where would you like to place your O(1-9)?"))
        board[moveO - 1] = letter

    return (board)




# checks for 3 X's or O's in a row
def checkRows(board):
    if board[0] == "X" and board[1] == "X" and board[2] == "X":
        return (True, "X")
    elif board[3] == "X" and board[4] == "X" and board[5] == "X":
        return (True, "X")
    elif board[6] == "X" and board[7] == "X" and board[8] == "X":
        return (True, "X")
    elif board[0] == "O" and board[1] == "O" and board[2] == "O":
        return (True, "O")
    elif board[3] == "O" and board[4] == "O" and board[5] == "O":
        return (True, "O")
    elif board[6] == "O" and board[7] == "O" and board[8] == "O":
        return (True, "O")
    else:
        return (False, "X and O")




# checks for 3 X's or O's in a column
def checkCols(board):
    if board[0] == "X" and board[3] == "X" and board[6] == "X":
        return (True, "X")
    elif board[1] == "X" and board[4] == "X" and board[7] == "X":
        return (True, "X")
    elif board[2] == "X" and board[5] == "X" and board[8] == "X":
        return (True, "X")
    elif board[0] == "O" and board[3] == "O" and board[6] == "O":
        return (True, "O")
    elif board[1] == "O" and board[4] == "O" and board[7] == "O":
        return (True, "O")
    elif board[2] == "O" and board[5] == "O" and board[8] == "O":
        return (True, "O")
    else:
        return (False, "X and O")


#

# checks for 3 X's or O's in diaganols
def checkDiags(board):
    if board[0] == "X" and board[4] == "X" and board[8] == "X":
        return (True, "X")
    elif board[2] == "X" and board[4] == "X" and board[6] == "X":
        return (True, "X")
    elif board[0] == "O" and board[4] == "O" and board[8] == "O":
        return (True, "O")
    elif board[2] == "O" and board[4] == "O" and board[6] == "O":
        return (True, "O")
    else:
        return (False, "X and O")




# win if 3 in a row, column, or diaganol
#if nothing, it's a draw
def checkWin(row, col, diag):
    if row == (True, "X") or col == (True, "X") or diag == (True, "X"):
        print("X wins")
        return(True)
    elif row == (True, "O") or col == (True, "O") or diag == (True, "O"):
        print("O wins")
        return(True)
    elif row==False and col==False and diag==False:
        print("It's a draw!")
        return(False)







# counts how many turns, max turn is 9 because only 9 spots
def turnCount(counter):
    counter += 1
    return (counter)


