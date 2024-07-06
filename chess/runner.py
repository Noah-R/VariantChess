from game import Game

game = Game()
while(True):
    moved = False
    print(game)
    print(game.isMate())
    move = input()

    if(move == "resign"):
        break

    elif(move == "O-O"):
        if(game.whiteToMove):
            game.move(game.whiteKing.y, game.whiteKing.x, 0, 6, move)
        else:
            game.move(game.blackKing.y, game.blackKing.x, 7, 6, move)

    elif(move == "O-O-O"):
        if(game.whiteToMove):
            game.move(game.whiteKing.y, game.whiteKing.x, 0, 2, move)
        else:
            game.move(game.blackKing.y, game.blackKing.x, 7, 2, move)
    
    else:
        for char in "x+#!?":
            move = move.replace(char, "")

        piece = game.prefixes["P"]
        note = ""
        if(move[0] in game.prefixes):
            piece = game.prefixes[move[0]]
            move = move[1:]
        else:
            if(move[-2] == "="):
                note = move[-1]
                move = move[:-2]
        
        #The ASCII code for lowercase 'a' is 97
        #The ASCIi code for digit '0' is 48
        targetX = ord(move[-2]) - 97
        targetY = ord(move[-1]) - 49

        #move will be the file/rank of the piece to move, if it needed to be specified
        move = move[:-2]

        for row in game.board:
            for spot in row:
                if(not moved
                    and spot != None
                    and spot.isWhite == game.whiteToMove
                    and type(spot) == piece
                    and (len(move) == 0 or ord(move) - 49 == spot.y or ord(move) - 97 == spot.x)):
                    if(game.move(spot.y, spot.x, targetY, targetX, note)):
                        moved = True