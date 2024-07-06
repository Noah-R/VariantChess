class Piece:
    def __init__(self, isWhite = True, x = 0, y = 0, hasMoved = False):
        self.isWhite = isWhite
        self.placeAt(y, x)
        self.hasMoved = hasMoved
    
    def placeAt(self, y, x):
        self.y = y
        self.x = x
        self.hasMoved = True
    
    def copy(self):
        return type(self)(self.isWhite, self.x, self.y, self.hasMoved)
    
    def listMoves(self, game, directions = []):
        options = []
        for direction in directions:
            for dist in range(1, 8):
                x = self.x + direction[0]*dist
                y = self.y + direction[1]*dist
                if(x < 0 or y < 0 or x > 7 or y > 7):
                    break
                square = game.board[y][x]
                if(square == None):
                    options.append((y, x, ""))
                    continue
                elif(square.isWhite != self.isWhite):
                    options.append((y, x, ""))
                    break
                else:
                    break
        return options