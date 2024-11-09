import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy.fft import fft, fftfreq, fftshift
import numpy as np


# # Load .wav file
file_path = "Sample_3.wav"  # Replace with your .wav file path
sampling_rate, audio_data = wavfile.read(file_path)

audio_data = audio_data[:,0]
audio_data = audio_data[20000:60000]

N = len(audio_data)

# sample spacing
T = 1 / sampling_rate
x = list(range(len(audio_data)))
y = audio_data
yf = fft(y)
xf = fftfreq(N, T)
xf = fftshift(xf)
yplot = fftshift(yf)
yplot = 1.0/N * np.abs(yplot)
Abschnitt = len(yplot)/2
Abschnitt = np.int16(Abschnitt)
yplot = yplot[Abschnitt:]
xf = xf[Abschnitt:]
plt.plot(xf, yplot)
# plt.plot(xf, 1.0/N * np.abs(yplot))
plt.grid()
plt.show()
