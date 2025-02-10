from flask import Flask
from flask_cors import CORS, cross_origin
from game import Game

app = Flask(__name__)

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

game = Game()

@app.route("/<string:move>")
@cross_origin()
def get_position(move = "a1a1"):
	x = ord(move[0]) - 97
	y = ord(move[1]) - 49
	targetX = ord(move[2]) - 97
	targetY = ord(move[3]) - 49
	
	if(len(move) == 4):
		game.move(y, x, targetY, targetX, "")
	else:
		game.move(y, x, targetY, targetX, move[4])
	
	return f'{game.getFEN(piecesOnly = True)[:-1]}'