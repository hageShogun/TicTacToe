import Board
import AIplayer

class TicTacToe():
    def __init__(self, initial_turn=True):
        self.board = Board.Board()
        self.board.reset
        self.initial_turn = initial_turn
        self.player_mark, self.ai_mark = None, None
        self.ai = None

    def setAI(self, mode, my_mark, opponent_mark):
        if mode == 'random':
            self.ai = AIplayer.RandomPlay(self.board, my_mark, opponent_mark)
        elif mode == 'minmax':
            self.ai = AIplayer.MinMaxPlay(self.board, my_mark, opponent_mark)
        else:
            print "Unknown ai mode is input."
            exit
        self.ai_mark = my_mark

    def setPlayerMark(self, mark):
        self.player_mark = mark

    def resetBoard(self):
        self.board.reset()

    def getInputFromStdin(self):
        print "It's your turn, please input the next position. ie 0 0."
        while True:
            input = raw_input().split()
            if len(input) != 2:
                print "incorrect input, incorrect input size."
                continue
            elif  not input[0].isdigit() or not input[1].isdigit():
                print "incorrect input, not integer input."
                continue
            
            row, col = map(int, input)
            ret = self.board.checkInput(row, col)
            if ret[0]:
                return(row, col)
            else:
                print ret[1]
                continue


    def play(self):
        player_turn = self.initial_turn # if true: player, false: ai
        while True:
            if player_turn:
                row, col = self.getInputFromStdin()
                self.board.setMark(row, col, self.player_mark)
            else: # ai turn
                row, col = self.ai.getInput()
                print row, col, "is input."
                self.board.setMark(row, col, self.ai_mark)
            self.board.dump()
            flg = self.board.checkGoal()
            if flg == 1: # one of the player win
                if player_turn:
                    print "You win"
                else:
                    print "You loose"
                break
            elif flg == -1:
                print "Draw"
                break
            player_turn = not player_turn


if __name__ == '__main__':
    game = TicTacToe(True)
    game.setPlayerMark('o')
    #game.setAI("random", 'x', 'o')
    game.setAI("minmax", 'x', 'o')
    game.play()
