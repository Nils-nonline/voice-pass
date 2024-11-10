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

def normalize_with_median(array):
    median = np.median(array)
    mad = np.median(np.abs(array - median))  # Calculate the Median Absolute Deviation
    #print(mad)
    
    # Avoid division by zero by setting mad to a small number if it's zero
    mad = mad if mad != 0 else 1e-10
    
    normalized_array = (array - median) / mad
    return normalized_array

def Vergleich(file_path_reference,file_path_test):
    # # Load .wav file
    # file_path_reference = "Maeau1.wav"
    # file_path_test = "Maeau2.wav"

    #generate the audio data arrays
    sr_reference, data_reference = wavfile.read(file_path_reference)
    data_reference = data_reference[:,0]
    data_reference = data_reference[:(sr_reference * 3)]
    sr_test, data_test = wavfile.read(file_path_test)
    data_test = data_test[:,0]
    data_test = data_test[0:(sr_test * 3)]

    if len(data_reference) > len(data_test):
        data_reference = data_reference[:len(data_test)]
    else:
        data_test = data_test[:len(data_reference)]

    # print(len(data_reference))
    # print(len(data_test))

    Window = 2000
    heatmap_reference = heatmap(data_reference, sr_reference, Window)
    heatmap_test = heatmap(data_test, sr_test, Window)



    heatmap_reference_normalized = normalize_with_median(heatmap_reference)
    heatmap_test_normalized = normalize_with_median(heatmap_test)
    heatmap_reference = heatmap_reference_normalized
    heatmap_test_normalized = heatmap_test_normalized

    # plt.imshow(heatmap_reference_normalized, cmap='viridis', aspect='auto')
    # plt.colorbar(label="Intensity")
    # plt.title("Heatmap of 2D Array")
    # plt.xlabel("Width (Columns)")
    # plt.ylabel("Length (Rows)")
    # plt.show()


    # #Difference
    # heatmap_difference = np.abs(heatmap_reference) - np.abs(heatmap_test)
    # heatmap_difference = np.abs(heatmap_difference)
    # ##create hat map
    # difference = heatmap_difference.sum()
    # difference = difference / len(heatmap_reference)
    # print(difference)

    heatmap_test = np.abs(heatmap_test)
    heatmap_reference = np.abs(heatmap_reference)
    heatmap_test = np.log(heatmap_test)
    heatmap_reference = np.log(heatmap_reference)

    difference = np.abs(heatmap_test - heatmap_reference)
    form = np.shape(heatmap_test)
    # print(form)
    # print(np.sum(difference))
    Durchschnitt = np.sum(difference) / 2*(form[0] * form[1])
    print(Durchschnitt)

    ergebnis = False
    if Durchschnitt < 0.8:
        ergebnis = False
    return ergebnis

print()
print(Vergleich("Maeau1.wav","Maeau2.wav"))





# for i in range(form[0]):
#     for j in range(form[1]):
#         difference[i,j] = heatmap_reference[i,j] / heatmap_test[i,j]

# difference = np.log(difference)
# Durchschnitt = np.sum(difference) / (form[0] * form[1])
# # Durchschnitt = np.log(Durchschnitt)

# print(Durchschnitt)


# Quotien rihtig
# Meau1 vs Meau2            0.05814452763342426
# Meau1 vs Hilfe1           0.07048251568148499







# #Quotient
# heatmap_difference = np.log(np.abs(heatmap_reference)) / np.log(np.abs(heatmap_test))
# difference = np.prod(heatmap_difference)
# difference = difference / len(heatmap_reference)
# print(difference)


# Autokorrelation = np.zeros(len(heatmap_reference))
# Window_Ak = 20
# for i in range((len(heatmap_reference)-Window_Ak)):
#     for ii in range(Window_Ak):
#         Help = (np.sum(heatmap_reference[ii]) * heatmap_test[ii + i])
#         Help = np.abs(Help)
#         Autokorrelation[i] = Autokorrelation[i] + Help
# max_point = max(Autokorrelation)
# max_point = max_point / (len(heatmap_reference)-Window_Ak)
# # min_point = min(Autokorrelation)
# # min_point = min_point / (len(heatmap_reference)-Window_Ak)

# print(max_point)
# plt.plot(Autokorrelation)
# plt.show()



# #print heatmap-ly<dgi
# plt.imshow(heatmap_reference, cmap='viridis', aspect='auto')
# plt.colorbar(label="Intensity")
# plt.title("Heatmap of 2D Array")
# plt.xlabel("Width (Columns)")
# plt.ylabel("Length (Rows)")
# plt.show()

#Mit Difference:
# HIlfe1 vs Hilfe2              22964.26635255197
# Hilfe1 vs HilfeReinhard2      26180.754935458852
# Hilfe1 vs Maeau1              15768.225843046213
# HIlfe1 vs 1234                14465.548970629137







# With normalasation:
# Passwort1 vs Passwort2            2060230.4028899528
# Password1 vs Sokolade             1895270.9268846503

# HIlfe1 vs Hilfe2                  14490.613273417073
# Hilfe1 vs HIlfeReinhard2          63604.67741505837


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




