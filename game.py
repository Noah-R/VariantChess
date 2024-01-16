from pawn import Pawn
from knight import Knight
from bishop import Bishop
from rook import Rook
from queen import Queen
from king import King

class Game:
    def __init__(self):
        self.board = []
        for r in range(8):
            self.board.append([])
        pieces = [Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook]
        for f in range(8):
            self.board[0].append(pieces[f](color = "white", x = f, y = 0))
            self.board[1].append(Pawn(color = "white", x = f, y = 1))
            self.board[2].append(None)
            self.board[3].append(None)
            self.board[4].append(None)
            self.board[5].append(None)
            self.board[6].append(Pawn(color = "black",  x = f, y = 6))
            self.board[7].append(pieces[f](color = "black", x = f, y = 7))
        self.whiteToMove = True

    def __str__(self):
        result = ""
        for rank in self.board:
            row = ""
            for piece in rank:
                if(piece == None):
                    row += " "
                else:
                    row += str(piece)
            row += "\n"
            result = row + result
        return result