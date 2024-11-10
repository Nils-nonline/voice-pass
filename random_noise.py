import numpy as np
import matplotlib.pyplot as plt
from scipy.io.wavfile import write
import random 


sr = 44100 
samples = 72000 
ergebnis = np.zeros(samples) 



def Random(sr, samples,index=0):
    Amplitude = 10
    Anzahl_Frequenzen = random.randint (1,10)  
    Frequenz_Uebergabe = np.zeros((Anzahl_Frequenzen, 2))
    low_limit = 200 
    high_limit = 1000 
    frequenz = low_limit
    Abstand = (high_limit - low_limit) / Anzahl_Frequenzen
    Abstand = (high_limit - low_limit) / Anzahl_Frequenzen
    
    for i in range(Anzahl_Frequenzen):
        Frequenz_Uebergabe[i,0] = random.randint (200,1000)
        Frequenz_Uebergabe[i,1] = random.randint (50,100)

    for ii in range(Anzahl_Frequenzen):
        lange_samples = (samples /sr)
        Anzahl_Schwingungen = (frequenz*lange_samples)
        for i in range(len(ergebnis)):
            ergebnis[i] = ergebnis[i] + (Amplitude * np.sin(((2*np.pi)/len(ergebnis)) * i * Anzahl_Schwingungen))
        frequenz = frequenz + Abstand
        Amplitude = Amplitude - 5
    ergebnis_int16 = np.int16(ergebnis *32768)
    write("output"+str(index)+".wav", sr, ergebnis_int16)

#ergebnis = Random(44100,72000)

"""
print(ergebnis)
plt.plot(ergebnis) 
plt.xlabel('Zeit (s)') 
plt.ylabel('Amplitude') 
plt.title('Sinus-Funktion')
plt.grid(True) 
plt.show()
"""
