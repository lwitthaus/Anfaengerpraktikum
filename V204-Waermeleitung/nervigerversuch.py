import numpy as np
from scipy.signal import argrelextrema
from scipy import signal

n, T7, T8 = np.genfromtxt('dynamisch200.txt', unpack=True)

T7ext = signal.find_peaks_cwt(T7, np.arange(1, 10))
T8ext = signal.find_peaks_cwt(T8, np.arange(1, 10))

# for local maxima
print('Lokale Extrema in T7 sind an den Stellen:', T7ext)
print('Lokale Minima in T8 sind an den Stellen:', T8ext)
