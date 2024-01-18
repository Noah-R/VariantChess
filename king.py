from piece import Piece

class King(Piece):
    def __init__(self, isWhite = True, x = 0, y = 0):
        s = "k"
        if(isWhite):
            s = "K"
        super().__init__(isWhite, x, y, s)

    def listMoves(self, board):
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (-1, 1), (1, -1), (-1, -1), (1, 1)]
        options = []
        for direction in directions:
            x = self.x + direction[0]
            y = self.y + direction[1]
            if(x > -1 and y > -1 and x < 8 and y < 8):
                square = board[y][x]
                if(square == None or square.isWhite != self.isWhite):
                    options.append((y, x, ""))
        return options