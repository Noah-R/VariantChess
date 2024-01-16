class Piece:
    def __init__(self, pieceType = "pawn", pieceColor = "white", file = "A", rank = "1"):
        self.pieceType = pieceType
        self.pieceColor = pieceColor
        self.file = file
        self.rank = rank
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
        for _ in range(8):
            self.board.append([])
        for f in range(8):
            pass
    def __str__(self):
        result = ""
        for rank in self.board:
            result = str(rank) + "\n" + result
        return result

print(Game())