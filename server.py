from flask import Flask
from flask_socketio import SocketIO
import os
import random
from random_noise import Random as ran
import FFT_Backend as fft
app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")
index = 0;
for i in range(0,11):
	ran(44100,72000,index=i)
print("...starting server")
def confirm(audio,passw):
	result = random.randint(0,3)==1#fft.check(audio,passw)
	os.remove(audio)
	return result

@socketio.on('audio')
def handle_audio(data):
	index = data["index"]
	f = open("{}audio.wav".format(index),"wb")
	f.write(data["d"])
	f.close()
	if confirm(str(index)+"audio.wav",'pass.wav'):
		socketio.emit("valid",{})
		f = open('urls.json',)
		locked_urls = json.load(f)["locked"].remove(data["hash"])
		json.dump(locked_urls,f)
		f.close()

@socketio.on('pass')
def handle_pass(data):
	print("New password!")
	audio_path = 'pass.wav'
	with open(audio_path, 'wb') as f:
		f.write(data["d"])
	index = data["index"]
if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=1337)
