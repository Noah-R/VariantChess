import socketio
import eventlet
from game import Game

games = {"only": {"game": Game(), "white": "", "black": ""}}
players = {}

sio = socketio.Server()
app = socketio.WSGIApp(sio, static_files={
    '/': './frontend/dist/index.html',
    '/index.js': './frontend/dist/index.js',
    '/style.css': './frontend/dist/style.css'
})

@sio.event
def connect(sid, environ):
	print(sid, "connected")
	players[sid] = "only"
	sio.emit("position", games[players[sid]]["game"].getFEN())

@sio.event
def disconnect(sid):
	print(sid, "disconnected")

@sio.event
def setColor(sid, color):
	if(color == "white"):
		games[players[sid]]["white"] = sid
	elif(color == "black"):
		games[players[sid]]["black"] = sid

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
	
	sio.emit("position", games[players[sid]]["game"].getFEN())
	sio.emit("status", games[players[sid]]["game"].status)

if __name__ == '__main__':
	eventlet.wsgi.server(eventlet.listen(('', 5000)), app)