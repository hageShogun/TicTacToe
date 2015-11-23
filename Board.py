import numpy as np

class Board():
    def __init__(self, initial_turn=True):
        self.spaces = np.array([[" "," "," "],[" "," "," "],[" "," "," "]]) 
        self.cnt_mark = 0


    def reset(self):
        self.spaces = np.array([[" "," "," "],[" "," "," "],[" "," "," "]])
        self.cnt_mark = 0


    def checkEmpty(self, row, col):
        if self.spaces[row][col] == " ":
            return True
        else:
            return False

    def checkInput(self, row, col):
        if (not row in [0,1,2]) or (not col in [0,1,2]):
            return (False, "incorrect input, over/under range.")
        elif not self.checkEmpty(row, col):
            return (False, "incorrect input, it have been placed.")
        else:
            return (True, "")

    def setMark(self, row, col, mark):
        self.spaces[row][col] = mark 
        self.cnt_mark += 1

    # 0: not finish, 1:finish, a user win -1: draw
    def checkGoal(self):
        if self.checkGoalOnRow() or self.checkGoalOnColumn() or \
           self.checkGoalOnDiagonal():
            return 1
        elif self.cnt_mark == 9:
            return -1
        else:
            return 0

    def checkGoalOnRow(self):
        for row in range(3):
            if not self.spaces[row][0] == " " and \
               self.spaces[row][0] == self.spaces[row][1] == self.spaces[row][2]:
                return True
        return False

    def checkGoalOnColumn(self):
        for col in range(3):
            if not self.spaces[0][col] == " " and \
               self.spaces[0][col] == self.spaces[1][col] == self.spaces[2][col]:
                return True
        return False

    def checkGoalOnDiagonal(self):
        if not self.spaces[1][1] == " ":
            if self.spaces[0][0] == self.spaces[1][1] == self.spaces[2][2]:
                return True
            if self.spaces[0][2] == self.spaces[1][1] == self.spaces[2][0]:
                return True
        return False


    # CUI
    def dump(self):
        print "-------------"
        for row in range(3):
            print '|',
            for col in range(3):
                print self.spaces[row][col],'|',
            print "\n-------------"

