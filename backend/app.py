import socketio
import eventlet
from game import Game

game = Game()

sio = socketio.Server()
app = socketio.WSGIApp(sio, static_files={
    '/': './frontend/dist/index.html',
    '/index.js': './frontend/dist/index.js',
    '/style.css': './frontend/dist/style.css'
})

@sio.event
def connect(sid, environ):
	print(sid, "connected")

@sio.event
def disconnect(sid):
	print(sid, "disconnected")

@sio.event
def move(sid, data):
	x = ord(data[0]) - 97
	y = ord(data[1]) - 49
	targetX = ord(data[2]) - 97
	targetY = ord(data[3]) - 49
	
	if(len(data) == 4):
		game.move(y, x, targetY, targetX, "")
	else:
		game.move(y, x, targetY, targetX, data[4])

if __name__ == '__main__':
	eventlet.wsgi.server(eventlet.listen(('', 5000)), app)