from piece import Piece

class Knight(Piece):
    def __init__(self, isWhite = True, x = 0, y = 0, moved = False):
        super().__init__(isWhite, x, y, moved)
    
    def __str__(self):
        if self.isWhite:
            return "N"
        return "n"
    
    def listMoves(self, board):
        options = []
        directions = [(2, 1), (1, 2), (2, -1), (-1, 2), (-2, 1), (1, -2), (-2, -1), (-1, -2)]
        for direction in directions:
            x = self.x + direction[0]
            y = self.y + direction[1]
            if(x < 0 or y < 0 or x > 7 or y > 7):
                continue
            square = board[y][x]
            if(square == None or square.isWhite != self.isWhite):
                options.append((y, x, ""))
        return options