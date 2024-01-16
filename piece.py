class Piece:
    def __init__(self, isWhite = True, x = 0, y = 0, string = ""):
        self.isWhite = isWhite
        self.x = x
        self.y = y
        self.string = string

    def __str__(self):
        return self.string
    
    def moves(self, board, directions = []):
        options = []
        for direction in directions:
            for dist in range(1, 8):
                x = self.x + direction[0]*dist
                y = self.y + direction[1]*dist
                if(x < 0 or y < 0 or x > 7 or y > 7):
                    break
                square = board[y][x]
                if(square == None):
                    options.append((y, x))
                    continue
                elif(square.isWhite != self.isWhite):
                    options.append((y, x))
                    break
                else:
                    break
        return options