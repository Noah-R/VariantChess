from pawn import Pawn
from knight import Knight
from bishop import Bishop
from rook import Rook
from queen import Queen
from king import King

class Game:
    def __init__(self):
        self.whiteToMove = True
        self.board = []
        for r in range(8):
            self.board.append([])
        pieces = [Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook]
        for f in range(8):
            self.board[0].append(pieces[f](isWhite = True, x = f, y = 0))
            self.board[1].append(Pawn(isWhite = True, x = f, y = 1))
            self.board[2].append(None)
            self.board[3].append(None)
            self.board[4].append(None)
            self.board[5].append(None)
            self.board[6].append(Pawn(isWhite = False,  x = f, y = 6))
            self.board[7].append(pieces[f](isWhite = False, x = f, y = 7))

        self.play()

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

    def move(self, y, x, targetY, targetX):
        if(self.board[y][x] == None
           or self.board[y][x].isWhite != self.whiteToMove
           or (targetY, targetX) not in self.board[y][x].listMoves(self.board)):
            return False
        self.board[y][x].placeAt(targetY, targetX)
        self.board[targetY][targetX] = self.board[y][x]
        self.board[y][x] = None
        self.whiteToMove = not self.whiteToMove
        return True

    def play(self):
        prefixes = {"N": Knight, "B": Bishop, "R": Rook, "Q": Queen, "K": King}
        while(True):
            print(self)
            move = input("enter move\n")
            if(move == "resign"):
                break

            piece = Pawn
            if(move[0] in prefixes):
                piece = prefixes[move[0]]
                move = move[1:]
            
            #The ASCII code for lowercase 'a' is 97
            #The ASCIi code for digit '0' is 48
            targetX = ord(move[-2]) - 97
            targetY = ord(move[-1]) - 49

            #move will be the file/rank of the piece to move, if it needed to be specified
            move = move[:-2]
            move = move.replace("x", "")

            for row in self.board:
                for spot in row:
                    if(spot != None
                       and spot.isWhite == self.whiteToMove
                       and type(spot) == piece
                       and (targetY, targetX) in spot.listMoves(self.board)
                       and (len(move) == 0 or ord(move) - 49 == spot.y or ord(move) - 97 == spot.x)):
                        self.move(spot.y, spot.x, targetY, targetX)
                        break