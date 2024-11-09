import eventlet
from eventlet import wsgi
import socketio
import io

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
    print('audiodata:',data)
    with open('myfile.wav', mode='bx') as f:
        f.write(data["wav"])
    sio.emit('newaudio',{'data': 'nodata!'})

@sio.event
def disconnect(sid):
    print('disconnect ', sid)

if __name__ == '__main__':
    eventlet.wsgi.server(eventlet.listen((hostName, serverPort)), app)