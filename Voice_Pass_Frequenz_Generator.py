import numpy as np
import matplotlib.pyplot as plt
from scipy.io.wavfile import write
import random 
rand = random.random()

# Print = drucken
# time.sleep  = delay
# int = ist nicht nötig
# 

sr = 44100 # Sampling rate
samples = 36000 #Anzahl der Messpunkt4
Amplitude = 10

Anzahl_Frequenzen = random.randint (1,10)  #Anzahl der Frequenzen, aus denen das Sample aufgebaut sein soll.
Frequenz_Uebergabe = np.zeros((Anzahl_Frequenzen, 2))
low_limit = 200 #hertz niedrigster Wert
high_limit = 1000 #hertz höchster Wert
frequenz = low_limit

print(Anzahl_Frequenzen)

Abstand = (high_limit - low_limit) / Anzahl_Frequenzen #zwischen den Frequenzen
print(Abstand) #Ausgeben

ergebnis = np.zeros(samples) #erstellt 1000 leere spots

 # Wie viele Schwingungen



for i in range(Anzahl_Frequenzen):
        Frequenz_Uebergabe[i,0] = random.randint (200,5000)
        Frequenz_Uebergabe[i,1] = random.randint (50,100)




print(Frequenz_Uebergabe)

    

for ii in range(Anzahl_Frequenzen):
    lange_samples = (samples /sr)
    Anzahl_Schwingungen = (frequenz*lange_samples)
    for i in range(len(ergebnis)):
        ergebnis[i] = ergebnis[i] + (Amplitude * np.sin(((2*np.pi)/len(ergebnis)) * i * Anzahl_Schwingungen))
    frequenz = frequenz + Abstand
    Amplitude = Amplitude - 5




plt.plot(ergebnis) 
plt.xlabel('Zeit (s)') 
plt.ylabel('Amplitude') 
plt.title('Sinus-Funktion')
plt.grid(True) 
plt.show()


ergebnis_int16 = np.int16(ergebnis *32768)
write("output.wav", sr, ergebnis_int16)




