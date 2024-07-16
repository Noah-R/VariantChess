from piece import Piece
from rook import Rook

class King(Piece):
    def __init__(self, isWhite = True, x = 0, y = 0, hasMoved = False):
        super().__init__(isWhite, x, y, hasMoved)
    
    def __str__(self):
        if self.isWhite:
            return "K"
        return "k"

    def listMoves(self, game):
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (-1, 1), (1, -1), (-1, -1), (1, 1)]
        options = []
        for direction in directions:
            x = self.x + direction[0]
            y = self.y + direction[1]
            if(x > -1 and y > -1 and x < 8 and y < 8):
                square = game.board[y][x]
                if(square == None or square.isWhite != self.isWhite):
                    options.append((y, x, ""))
        
        if(not self.hasMoved):
            castles = [{"direction": 1, "rook": 7, "kingSpot": 6}, {"direction": -1, "rook": 0, "kingSpot": 2}]
            for castle in castles:
                canCastle = True
                
                for x in range(self.x + castle["direction"], castle["rook"], castle["direction"]):
                    if(game.board[self.y][x] != None):
                        canCastle = False
                        break
                
                rookSpot = game.board[self.y][castle["rook"]]
                if(type(rookSpot) != Rook or rookSpot.hasMoved or rookSpot.isWhite != self.isWhite):
                    canCastle = False

                if(canCastle):
                    options.append((self.y, castle["kingSpot"], ""))
            
        return options