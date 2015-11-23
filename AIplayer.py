import Board
import random
import copy

class AIplayer(object):
    def __init__(self, board, my_mark, opponent_mark):
        self.board = board


class RandomPlay(AIplayer):
    def __init__(self, board, my_mark, opponent_mark):
        super(RandomPlay, self).__init__(board, my_mark, opponent_mark)
        
    def getInput(self):
        while True:
            row, col = random.randint(0,2), random.randint(0,2)
            if self.board.checkEmpty(row, col):
                return (row, col)


class MinMaxPlay(AIplayer):
    def __init__(self, board, my_mark, opponent_mark):
        super(MinMaxPlay, self).__init__(board, my_mark, opponent_mark)
        self.my_mark = my_mark
        self.opponent_mark = opponent_mark

    def searchEmptyPlaces(self, board):
        empty_places = []
        for row in range(3):
            for col in range(3):
                if board.checkEmpty(row,col):
                    empty_places.append( (row, col) )
        return empty_places

    def minmax(self, board, my_turn, depth):
        scores = {}
        empty_places = self.searchEmptyPlaces(board)
        for place in empty_places:
            row, col = place[0], place[1]
            virt_board = copy.deepcopy(board)
            if my_turn:
                virt_board.setMark(row, col, self.my_mark)
            else:
                virt_board.setMark(row, col, self.opponent_mark)
            score = self.score(virt_board, my_turn, depth)
            # virt_board.dump() # debug print
            # print my_turn, "depth", depth, "score:", score, '\n' # debug print
            if score is not None:
                scores[(row,col)] = score
            else:
                score = self.minmax(virt_board, not my_turn, depth + 1)[0]
                scores[(row,col)] = score
        #print "scores:", scores # debug print
        if my_turn:
            return (max(scores.values()), max(scores, key=(lambda x: scores[x])))
        else:
            return (min(scores.values()), min(scores, key=(lambda x: scores[x])))

    def getInput(self):
        board = copy.deepcopy(self.board) # virtual board
        ret = self.minmax(board, True, 0)
        print ret
        return ret[1]

    def score(self,board, my_turn, depth):
        goal_flg = board.checkGoal()
        if goal_flg == 1:
            if my_turn:
                return 10 - depth
            else: # opponent wins
                return depth -10
        elif goal_flg == -1: # draw
            return 0 # un-finished case
        else:
            return None



if __name__ == '__main__':
    board = Board.Board()
    ai = MinMaxPlay(board, 'o', 'x')

    # o
    # oxx
    # x o
    #
    board.setMark(0,0,'o')
    board.setMark(2,2,'o')
    board.setMark(1,0,'o')

    board.setMark(1,2,'x')
    board.setMark(1,1,'x')
    board.setMark(2,0,'x')

    ai.getInput()
