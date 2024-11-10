import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy.fft import fft, fftfreq, fftshift
import numpy as np

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

def normalize_with_median(array):
    median = np.median(array)
    mad = np.median(np.abs(array - median))  # Calculate the Median Absolute Deviation
    #print(mad)
    
    # Avoid division by zero by setting mad to a small number if it's zero
    mad = mad if mad != 0 else 1e-10
    
    normalized_array = (array - median) / mad
    return normalized_array

def Vergleich(file_path_reference,file_path_test, threshold):

    #generate the audio data arrays
    sr_reference, data_reference = wavfile.read(file_path_reference)
    data_reference = data_reference[:,0]
    # data_reference = data_reference[:(sr_reference * 4)]
    sr_test, data_test = wavfile.read(file_path_test)
    data_test = data_test[:,0]
    # data_test = data_test[0:(sr_test * 4)]

    if len(data_reference) > len(data_test):
        data_reference = data_reference[:len(data_test)]
    else:
        data_test = data_test[:len(data_reference)]

    Window = 500
    heatmap_reference = heatmap(data_reference, sr_reference, Window)
    heatmap_test = heatmap(data_test, sr_test, Window)

    # heatmap_reference_normalized = normalize_with_median(heatmap_reference)
    # heatmap_test_normalized = normalize_with_median(heatmap_test)
    # heatmap_reference = heatmap_reference_normalized
    # heatmap_test_normalized = heatmap_test_normalized

    heatmap_test = np.abs(heatmap_test)
    heatmap_reference = np.abs(heatmap_reference)
    heatmap_test = np.log(heatmap_test)
    heatmap_reference = np.log(heatmap_reference)

    difference = np.abs(heatmap_test - heatmap_reference)
    Durchschnitt = np.mean(difference)
    form = np.shape(heatmap_test)
    Durchschnitt = Durchschnitt / (2*(form[0] * form[1]))
    Durchschnitt = Durchschnitt * 10000000
    print(Durchschnitt)

    #print heatmap-ly<dgi
    plt.imshow(difference, cmap='viridis', aspect='auto')
    plt.colorbar(label="Intensity")
    plt.title("Heatmap of 2D Array")
    plt.xlabel("Width (Columns)")
    plt.ylabel("Length (Rows)")
    plt.show()

    ergebnis = False
    if Durchschnitt < threshold:
        ergebnis = True
    return ergebnis

print()
print(Vergleich("Hilfe1_short.wav","1234.wav",250))



