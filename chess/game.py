from pawn import Pawn
from knight import Knight
from bishop import Bishop
from rook import Rook
from queen import Queen
from king import King

class Game:
    def __init__(self):
        self.whiteToMove = True
        self.status = "White to play"
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
        
            self. prefixes = {"N": Knight, "B": Bishop, "R": Rook, "Q": Queen, "K": King, "P": Pawn}
    
    def checkStatus(self):
        if(self.whiteToMove):
            self.status = "White to play"
        else:
            self.status = "Black to play"
    
    def copy(self):
        copy = Game()
        copy.whiteToMove = self.whiteToMove
        for y in range(8):
            for x in range(8):
                if(self.board[y][x] != None):
                    copy.board[y][x] = self.board[y][x].copy()
                else:
                    copy.board[y][x] = None
        copy.whiteKing = copy.board[self.whiteKing.y][self.whiteKing.x]
        copy.blackKing = copy.board[self.blackKing.y][self.blackKing.x]
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
        return result + "\n" + self.status

    def executeMove(self, y, x, targetY, targetX, note):
        self.board[y][x].placeAt(targetY, targetX)
        self.board[targetY][targetX] = self.board[y][x]
        self.board[y][x] = None

        if(note in self.prefixes and not note == "K"):
            self.board[targetY][targetX] = self.board[targetY][targetX].promote(self.prefixes[note])

    def move(self, y, x, targetY, targetX, note):
        if(self.board[y][x] == None
           or self.board[y][x].isWhite != self.whiteToMove
           or (targetY, targetX, note) not in self.board[y][x].listMoves(self.board)):
            return False
        
        testBoard = self.copy()

        if(note in ["O-O", "O-O-O"]):
            if(note == "O-O"):
                direction = 1
                end = 7
            else:
                direction = -1
                end = 7
            
            counter = x
            while(counter < targetX):
                if(testBoard.inCheck(self.whiteToMove)):
                    return False
                testBoard.executeMove(y, counter, targetY, counter + direction, note)
                counter += direction
            while(counter != end):
                counter += direction
                if(type(testBoard.board[y][counter]) == Rook):
                    testBoard.executeMove(y, counter, targetY, targetX - direction, note)
                    if(testBoard.inCheck(self.whiteToMove)):
                        return False
                    break
                
            self.executeMove(y, x, targetY, targetX, note)
            self.executeMove(y, counter, targetY, targetX - direction, note)
            self.whiteToMove = not self.whiteToMove
            self.checkStatus()
            return True

        else:
            testBoard.executeMove(y, x, targetY, targetX, note)
            
            if(testBoard.inCheck(self.whiteToMove)):
                return False

            self.executeMove(y, x, targetY, targetX, note)
            self.whiteToMove = not self.whiteToMove
            self.checkStatus()
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