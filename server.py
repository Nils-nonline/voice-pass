from flask import Flask
from flask_socketio import SocketIO
import os

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
index = 0;

@socketio.on('audio')
def handle_audio(data):
    print(data["d"])
    audio_path = os.path.join(UPLOAD_FOLDER, 'audio'+str(data["index"])+'.wav')
    with open(audio_path, 'ab') as f:
        f.write(data["d"])
	index = data["index"]

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=1337)
