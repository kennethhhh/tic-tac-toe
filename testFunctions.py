# Project 3 - Tic-Tac-Toe Simulator
#
# Name: Kenneth Liu
# Instructor: S. Einakian
# Section: 01,02


import unittest
import tictactoeFuncs

class TestCases(unittest.TestCase):
    def test_checkRows(self):
        List=["X","X","X","","","","","",""]
        self.assertEqual(tictactoeFuncs.checkRows(List), (True, "X"))
        List=["X","X","O","","","","","",""]
        self.assertEqual(tictactoeFuncs.checkRows(List), (False, "X and O"))
        List = ["X","X","O","O","O","O","X","O","O"]
        self.assertEqual(tictactoeFuncs.checkRows(List), (True, "O"))

    def test_checkCols(self):
        List=["X","","","X","","","X","",""]
        self.assertEqual(tictactoeFuncs.checkCols(List), (True, "X"))
        List=["X","X","X","","","","","",""]
        self.assertEqual(tictactoeFuncs.checkCols(List), (False, "X and O"))
        List=["X","O","O","O","O","X","X","O","O"]
        self.assertEqual(tictactoeFuncs.checkCols(List), (True, "O"))

    def test_checkDiags(self):
        List = ["X","","","","X","","","","X"]
        self.assertEqual(tictactoeFuncs.checkDiags(List), (True, "X"))
        List = ["","","O","","O","","O","",""]
        self.assertEqual(tictactoeFuncs.checkDiags(List), (True, "O"))
        List = ["X","","","X","","","X","",""]
        self.assertEqual(tictactoeFuncs.checkDiags(List), (False, "X and O"))

    def test_checkWin(self):
        row=False
        col=False
        diag=(True, "X")
        self.assertEqual(tictactoeFuncs.checkWin(row,col,diag), True)
        row=False
        col=False
        diag=False
        self.assertEqual(tictactoeFuncs.checkWin(row,col,diag), False)


      

# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

