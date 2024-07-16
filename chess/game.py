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
        self.ep_square = None
        self.halfmove_clock = 0
        self.fullmove_number = 1
        self.repetitions = {}
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
    
    def checkStatus(self, fen):
        mate = self.isMate()
        if(mate):
            self.status = mate
            return
        if(self.isInsufficientMaterial()):
            self.status = "Draw - Insufficient material"
            return
        elif(self.repetitions[fen] >= 5):
            self.status = "Draw - fivefold repetition"
            return
        elif(self.halfmove_clock >= 150):
            self.status += "Draw - 75 move rule"
            return

        elif(self.whiteToMove):
            self.status = "White to play"
        else:
            self.status = "Black to play"

        if(self.repetitions[fen] >= 3):
            self.status += " - Threefold repetition may be claimed"
        if(self.halfmove_clock >= 100):
            self.status += " - 50 move rule may be claimed"
    
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
        copy.ep_square = self.ep_square
        copy.halfmove_clock = self.halfmove_clock
        copy.fullmove_number = self.fullmove_number
        copy.repetitions = self.repetitions
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

    def placePiece(self, y, x, targetY, targetX, note = ""):
        if(type(self.board[y][x]) == Pawn or self.board[targetY][targetX] != None):
            self.halfmove_clock = 0
            self.repetitions = {}
        else:
            self.halfmove_clock += 1
        
        if(not self.whiteToMove):
            self.fullmove_number += 1
        
        self.board[y][x].placeAt(targetY, targetX)
        self.board[targetY][targetX] = self.board[y][x]
        self.board[y][x] = None

        if(note in ["N", "B", "R", "Q"]):
            self.board[targetY][targetX] = self.board[targetY][targetX].promote(self.prefixes[note])
        
        if(type(self.board[targetY][targetX]) == Pawn):
            if(self.ep_square == (targetY, targetX)):        
                self.ep_square = None
                if(targetY == 2):
                    self.board[3][targetX] = None
                elif(targetY == 5):
                    self.board[4][targetX] = None
            
            elif(abs(y - targetY) == 2):        
                self.ep_square = None
                if(targetX > 0):
                    ep_pawn = self.board[targetY][targetX-1]
                    if(ep_pawn != None and type(ep_pawn) == Pawn and ep_pawn.isWhite != self.board[targetY][targetX].isWhite):
                        if(targetY == 3):
                            self.ep_square = (2, x)
                        if(targetY == 4):
                            self.ep_square = (5, x)
                if(targetX < 7):
                    ep_pawn = self.board[targetY][targetX+1]
                    if(ep_pawn != None and type(ep_pawn) == Pawn and ep_pawn.isWhite != self.board[targetY][targetX].isWhite):
                        if(targetY == 3):
                            self.ep_square = (2, x)
                        if(targetY == 4):
                            self.ep_square = (5, x)
            
            else:            
                self.ep_square = None
        
        else:
            self.ep_square = None

    def move(self, y, x, targetY, targetX, note = "", checkingForMate = False):
        if(self.status[:13] not in ("White to play", "Black to play")
           or self.board[y][x] == None
           or self.board[y][x].isWhite != self.whiteToMove
           or (targetY, targetX, note) not in self.board[y][x].listMoves(self)):
            return False
        
        testBoard = self.copy()

        if(type(self.board[y][x]) == King and abs(targetX - x) == 2):
            if(testBoard.inCheck()):
                return False
            
            if(targetX > x):
                direction = 1
                rookSpot = 7
            else:
                direction = -1
                rookSpot = 0
            
            testBoard.placePiece(y, x, y, x + direction)
            if(testBoard.inCheck()):
                return False
            testBoard = self.copy()
            
            testBoard.placePiece(y, x, targetY, targetX)
            testBoard.placePiece(y, rookSpot, targetY, targetX - direction)
            if(testBoard.inCheck()):
                return False
        
            self.placePiece(y, x, targetY, targetX)
            self.placePiece(y, rookSpot, targetY, targetX - direction)
            self.whiteToMove = not self.whiteToMove
            if(not checkingForMate):
                fen = self.getFEN(forThreefold = True)
                self.repetitions[fen] = self.repetitions.get(fen, 0) + 1
                self.checkStatus(fen)
            return True

        else:
            testBoard.placePiece(y, x, targetY, targetX, note)
            
            if(testBoard.inCheck()):
                return False

            self.placePiece(y, x, targetY, targetX, note)
            self.whiteToMove = not self.whiteToMove
            if(not checkingForMate):
                fen = self.getFEN(forThreefold = True)
                self.repetitions[fen] = self.repetitions.get(fen, 0) + 1
                self.checkStatus(fen)
            return True

    def inCheck(self):
        king = self.blackKing
        if(self.whiteToMove):
            king = self.whiteKing
        kingCaptures = [(king.y, king.x, ""), (king.y, king.x, "Q")]
        
        for row in self.board:
            for piece in row:
                if(not piece == None and piece.isWhite != self.whiteToMove):
                    moves = piece.listMoves(self)
                    for capture in kingCaptures:
                        if(capture in moves):
                            return True
        
        return False

    def isMate(self):
        for row in self.board:
            for piece in row:
                if(not piece == None and piece.isWhite == self.whiteToMove):
                    moves = piece.listMoves(self)
                    for move in moves:
                        testBoard = self.copy()
                        if(testBoard.move(piece.y, piece.x, move[0], move[1], move[2], checkingForMate = True)):
                            return False
        
        if self.inCheck():
            if(self.whiteToMove):
                return "Black wins - Checkmate"
            return "White wins - Checkmate"
        return "Draw - Stalemate"

    def getFEN(self, piecesOnly = False, forThreefold = False):
        fen = ""

        #piece placement
        for rank in self.board:
            row = ""
            number = 0
            for piece in rank:
                if(piece == None):
                    number += 1
                else:
                    if(number > 0):
                        row += str(number)
                        number = 0
                    row += str(piece)
            
            if(number > 0):
                row += str(number)
                number = 0
            fen = row + "/" + fen
        if(piecesOnly):
            return fen

        #active color
        if(self.whiteToMove):
            fen += " w"
        else:
            fen += " b"
        
        #castling availability
        castles = " "
        
        if(self.board[0][4] != None and not self.board[0][4].hasMoved):
            if(self.board[0][7] != None and not self.board[0][7].hasMoved):
                castles += "K"
            if(self.board[0][0] != None and not self.board[0][0].hasMoved):
                castles += "Q"

        if(self.board[7][4] != None and not self.board[7][4].hasMoved):
            if(self.board[7][7] != None and not self.board[7][7].hasMoved):
                castles += "k"
            if(self.board[7][0] != None and not self.board[7][0].hasMoved):
                castles += "q"
        
        if(castles == " "):
            castles = " -"
        fen += castles

        #en passant target square
        if(self.ep_square == None):
            fen += " -"
        else:        
            fen += ' ' + chr(self.ep_square[1] + 97) + chr(self.ep_square[0] + 49)

        if(forThreefold):
            return fen
        
        #halfmove clock
        fen += " " + str(self.halfmove_clock)

        #fullmove number
        fen += " " + str(self.fullmove_number)
        
        return fen
    
    def isInsufficientMaterial(self):
        foundKnight = False
        foundLSB = False
        foundDSB = False

        for rank in self.board:
            for piece in rank:
                if(piece != None):
                    if(type(piece) in [Rook, Queen, Pawn]):
                        return False
                    
                    if(type(piece) == Knight):
                        if(foundKnight or foundLSB or foundDSB):
                            return False
                        foundKnight = True
                    
                    elif(type(piece) == Bishop and piece.lightSquare):
                        if(foundDSB or foundKnight):
                            return False
                        foundLSB = True
        
                    elif(type(piece) == Bishop and not piece.lightSquare):
                        if(foundLSB or foundKnight):
                            return False
                        foundDSB = True
        
        return True