from flask import Flask
from flask_socketio import SocketIO
import os
import random
import json
from random_noise import Random as ran
import FFT_Backend as fft
import librosa
import soundfile as sf
from pydub import AudioSegment

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")
index = 0;
for i in range(0,11):
	ran(44100,72000,index=i)
print("...starting server")
def confirm(audio,passw):
	fft.Vergleich(passw,audio)
	return True

@socketio.on('audio')
def handle_audio(data):
	index = data["index"]
	f = open("audio.wav","wb")
	f.write(data["d"])
	f.close()
	song = AudioSegment.from_wav("never_gonna_give_you_up.wav")
	song.export("audio.wav", format="wav")
	if confirm("audio.wav",'pass.wav'):
		socketio.emit("valid",{})
		try:
			f = open('urls.json',)
			locked_urls = json.load(f)["locked"]
			remove_index = locked_urls.index(data["hash"])
			locked_urls.pop(remove_index)
			print(locked_urls)
			json.dump(locked_urls,f)
			f.close()
		except:
			pass


@socketio.on('pass')
def handle_pass(data):
	print("New password!")
	audio_path = 'pass.wav'
	with open(audio_path, 'wb') as f:
		f.write(data["d"])
	index = data["index"]
if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=1337)
