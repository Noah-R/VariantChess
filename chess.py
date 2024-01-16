class Piece:
    def __init__(self, pieceType = "pawn", pieceColor = "white", x = 0, y = 0):
        self.pieceType = pieceType
        self.pieceColor = pieceColor
        self.x = x
        self.y = y
        self.str = pieceType[0]
        if(pieceType == "knight"):
            self.str = "n"
        if(pieceColor == "white"):
            self.str = self.str.upper()

    def __str__(self):
        return self.str

class Game:
    def __init__(self):
        self.board = []
        for r in range(8):
            self.board.append([])
        pieces = ["rook", "knight", "bishop", "queen", "king", "bishop", "knight", "rook"]
        for f in range(8):
            self.board[0].append(Piece(pieceColor = "white", pieceType = pieces[f], x = f, y = 0))
            self.board[1].append(Piece(pieceColor = "white", pieceType = "pawn", x = f, y = 1))
            self.board[2].append(None)
            self.board[3].append(None)
            self.board[4].append(None)
            self.board[5].append(None)
            self.board[6].append(Piece(pieceColor = "black", pieceType = "pawn", x = f, y = 6))
            self.board[7].append(Piece(pieceColor = "black", pieceType = pieces[f], x = f, y = 7))

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

print(Game())