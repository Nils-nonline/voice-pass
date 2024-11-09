import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy.fft import fft, fftfreq, fftshift
import numpy as np

# create reference

def FFT_VP(data, sr):
    N = len(data)
    T = 1 / sr
    x = list(range(len(data)))
    y = data
    yf = fft(y)
    xf = fftfreq(N, T)
    xf = fftshift(xf)
    yplot = fftshift(yf)
    yplot = 1.0/N * np.abs(yplot)
    Abschnitt = len(yplot)/2
    Abschnitt = np.int16(Abschnitt)
    yplot = yplot[Abschnitt:]
    xf = xf[Abschnitt:]
    # plt.plot(xf, 1.0/N * np.abs(yplot))
    # plt.plot(FFT_Ergebnis_reference)
    # plt.plot(FFT_Ergebnis_test)   

    return yplot

def heatmap(data, sr, window):
    lenth = np.int16((len(data) / window))
    hmwith = np.int16(window/2)

    heatmap_reference = np.zeros((lenth,hmwith))

    # fill heat map
    start = 0
    for i in range(lenth):
    # while start+window < lenth:   
        end = start + window
        data_cut = data[start:end]
        heatmap_reference[i] = FFT_VP(data_cut, sr)
        # print(heatmap_reference[i])
        # print()

        start = start + window
    return heatmap_reference

# # Load .wav file
file_path_reference = "Passwort1.wav"
file_path_test = "Schokolade.wav"

#generate the audio data arrays
sr_reference, data_reference = wavfile.read(file_path_reference)
data_reference = data_reference[:,0]
# data_reference = data_reference[:20000]
sr_test, data_test = wavfile.read(file_path_test)
data_test = data_test[:,0]
# data_test = data_test[0:20000]

if len(data_reference) > len(data_test):
    data_reference = data_reference[:len(data_test)]
else:
    data_test = data_test[:len(data_reference)]

# print(len(data_reference))
# print(len(data_test))

Window = 1000
heatmap_reference = heatmap(data_reference, sr_reference, Window)
heatmap_test = heatmap(data_test, sr_test, Window)

heatmap_difference = heatmap_reference * heatmap_test
# create hat map
difference = heatmap_difference.sum()
difference = difference / len(heatmap_reference)
print(difference)

# #print heatmap-ly<dgi
plt.imshow(heatmap_reference, cmap='viridis', aspect='auto')
plt.colorbar(label="Intensity")
plt.title("Heatmap of 2D Array")
plt.xlabel("Width (Columns)")
plt.ylabel("Length (Rows)")
plt.show()

final_Ergebnis = False

if difference > 1000000000:
    final_Ergebnis = True





# Mit Teilung durch die Länge:
#Passwort1 vs Passwort2             796311.814656802
#Passwort1 vs Schokolade            892040.3398877878         



# plt.grid()
# plt.show()

# Password 1 vs. 2:     21 500 418.995733652

# R1 vs R2              14 44 998 502.0170355
# R1 vs Password1       70 505 219.04345512
# R1 vs 1234            92 294 141.56733859

# Kaenguru 1 vs. 2      1 931 719 177.0528028
# Kaenguru 1 vs. R1     584 873 830.8646038
# Kaenguru 1 vs. Meau1: 69 507 944.55388303

# Meau1 vs. Meau2:      25 935 883.854302727
# Meau 1 vs. Hilfe 1:   9 769 465.01539137




