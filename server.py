import eventlet
from eventlet import wsgi
import socketio
import io
import base64
hostName = "localhost"
serverPort = 8080


sio = socketio.Server()
app = socketio.WSGIApp(sio, static_files={
'/': {'content_type': 'text/html', 'filename': 'index.html'}
})

@sio.event
def connect(sid, environ):
	print('connect ', sid)

@sio.event
def audio(sid, data):
	print('audiodata:',data['blob'])
	encoded = data['blob'].encode()
	content = base64.b64decode(encoded)
	with open('data.wav', 'wb') as fw:
		fw.write(content)

@sio.event
def disconnect(sid):
    print('disconnect ', sid)

if __name__ == '__main__':
    eventlet.wsgi.server(eventlet.listen((hostName, serverPort)), app)
