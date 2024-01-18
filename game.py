from pawn import Pawn
from knight import Knight
from bishop import Bishop
from rook import Rook
from queen import Queen
from king import King

class Game:
    def __init__(self):
        self.whiteToMove = True
        self.whiteKing = None
        self.blackKing = None
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
            if(pieces[f] == King):
                self.whiteKing = self.board[0][-1]
                self.blackKing = self.board[7][-1]

        self.prefixes = {"N": Knight, "B": Bishop, "R": Rook, "Q": Queen, "K": King}
    
    def copy(self):
        copy = Game()
        copy.whiteToMove = self.whiteToMove
        for y in range(8):
            for x in range(8):
                copy.board[y][x] = self.board[y][x].copy()
        copy.prefixes = self.prefixes

        return copy

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

    def move(self, y, x, targetY, targetX, note):
        if(self.board[y][x] == None
           or self.board[y][x].isWhite != self.whiteToMove
           or (targetY, targetX, note) not in self.board[y][x].listMoves(self.board)):
            return False
        self.board[y][x].placeAt(targetY, targetX)
        self.board[targetY][targetX] = self.board[y][x]
        self.board[y][x] = None
        self.whiteToMove = not self.whiteToMove

        if(note in self.prefixes and not note == "K"):
            self.board[targetY][targetX] = self.board[targetY][targetX].promote(self.prefixes[note])

        return True

    def inCheck(self, white):
        king = self.blackKing
        if(white):
            king = self.whiteKing
        kingCaptures = [(king.y, king.x, ""), (king.y, king.x, "Q")]
        
        for row in self.board:
            for piece in row:
                if(not piece == None and piece.isWhite != white):
                    moves = piece.listMoves(self.board)
                    for capture in kingCaptures:
                        if(capture in moves):
                            return True
        
        return False


    def play(self):
        while(True):
            print(self)
            move = input("enter move\n")
            if(move == "resign"):
                break
            
            for char in "x+#!?":
                move = move.replace(char, "")

            piece = Pawn
            note = ""
            if(move[0] in self.prefixes):
                piece = self.prefixes[move[0]]
                move = move[1:]
            else:
                if(move[-2] == "="):
                    note = move[-1]
                    move = move[:-2]
            
            #The ASCII code for lowercase 'a' is 97
            #The ASCIi code for digit '0' is 48
            targetX = ord(move[-2]) - 97
            targetY = ord(move[-1]) - 49

            #move will be the file/rank of the piece to move, if it needed to be specified
            move = move[:-2]

            for row in self.board:
                for spot in row:
                    if(spot != None
                       and spot.isWhite == self.whiteToMove
                       and type(spot) == piece
                       and (len(move) == 0 or ord(move) - 49 == spot.y or ord(move) - 97 == spot.x)):
                        self.move(spot.y, spot.x, targetY, targetX, note)