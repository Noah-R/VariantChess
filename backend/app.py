import socketio
import eventlet
from game import Game

games = {} #game name: {game: game object, white: white's sid, black: black's sid}
players = {} #sid: game name

sio = socketio.Server()
app = socketio.WSGIApp(sio, static_files={
    '/': './frontend/dist/index.html',
    '/index.js': './frontend/dist/index.js',
    '/style.css': './frontend/dist/style.css'
})

@sio.event
def connect(sid, environ):
	print(sid, "connected")
	players[sid] = ""

@sio.event
def disconnect(sid):
	print(sid, "disconnected")

@sio.event
def join(sid, data):
	room = "#" + data[0][:32]
	color = data[1]

	if(players[sid] == ""):
		if(room not in games):
			games[room] = {"game": Game(), "white": "", "black": ""}
		
		if(games[room][color] == ""):
			games[room][color] = sid
			players[sid] = room
			sio.emit("position", games[room]["game"].getFEN(), to=[games[players[sid]]["white"], games[players[sid]]["black"]])
			sio.emit("status", games[room]["game"].status, to=[games[players[sid]]["white"], games[players[sid]]["black"]])

@sio.event
def move(sid, data):
	if(players[sid] not in games or not ((games[players[sid]]["game"].whiteToMove and games[players[sid]]["white"] == sid) or (not games[players[sid]]["game"].whiteToMove and games[players[sid]]["black"] == sid))):
		return
	x = ord(data[0]) - 97
	y = ord(data[1]) - 49
	targetX = ord(data[2]) - 97
	targetY = ord(data[3]) - 49
	
	if(len(data) == 4):
		games[players[sid]]["game"].move(y, x, targetY, targetX, "")
	else:
		games[players[sid]]["game"].move(y, x, targetY, targetX, data[5])
	
	sio.emit("position", games[players[sid]]["game"].getFEN(), to=[games[players[sid]]["white"], games[players[sid]]["black"]])
	sio.emit("status", games[players[sid]]["game"].status, to=[games[players[sid]]["white"], games[players[sid]]["black"]])

if __name__ == '__main__':
	eventlet.wsgi.server(eventlet.listen(('', 5000)), app)