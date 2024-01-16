from piece import Piece

class Rook(Piece):
    def __init__(self, isWhite = True, x = 0, y = 0):
        s = "r"
        if(isWhite):
            s = "R"
        super().__init__(isWhite, x, y, s)
    
    def moves(self, board):
        options = []
        for x in range(self.x + 1, 8):
            square = board[x][self.y]
            if(square == None):
                options.append((x, self.y))
                continue
            elif(square.isWhite != self.isWhite):
                options.append((x, self.y))
                break
            else:
                break
        for x in range(self.x - 1, -1, -1):
            square = board[x][self.y]
            if(square == None):
                options.append((x, self.y))
                continue
            elif(square.isWhite != self.isWhite):
                options.append((x, self.y))
                break
            else:
                break
        for y in range(self.y + 1, 8):
            square = board[self.x][y]
            if(square == None):
                options.append((self.x, y))
                continue
            elif(square.isWhite != self.isWhite):
                options.append((self.x, y))
                break
            else:
                break
        for y in range(self.y -1, -1, -1):
            square = board[self.x][y]
            if(square == None):
                options.append((self.x, y))
                continue
            elif(square.isWhite != self.isWhite):
                options.append((self.x, y))
                break
            else:
                break
        return options