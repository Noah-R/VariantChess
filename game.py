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
            self.board[0].append(pieces[f](isWhite = True, x = f, y = 0))
            self.board[1].append(Pawn(isWhite = True, x = f, y = 1))
            self.board[2].append(None)
            self.board[3].append(None)
            self.board[4].append(None)
            self.board[5].append(None)
            self.board[6].append(Pawn(isWhite = False,  x = f, y = 6))
            self.board[7].append(pieces[f](isWhite = False, x = f, y = 7))
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

    def test(self):
        command = "start"
        while(command != "end"):
            print(self)
            command = input("enter command")
            x = int(input("enter x"))
            y = int(input("enter y"))
            if(command == "list"):
                print(self.board[y][x].listMoves(self.board))
            elif(command == "move"):
                targetX = int(input("enter target x"))
                targetY = int(input("enter target y"))
                self.move(y, x, targetY, targetX)