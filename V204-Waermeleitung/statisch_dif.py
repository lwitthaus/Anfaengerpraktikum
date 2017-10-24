import matplotlib.pyplot as plt
import numpy as np


n, T1, T2, T3, T4, T5, T6, T7, T8 = np.genfromtxt('statisch.txt', unpack=True)
y = T2-T1
z = T7-T8
plt.plot(n*5, y, 'r.', label='T2-T1 (Messing)', Markersize=2)
plt.plot(n*5, z, 'b.', label='T7-T8 (Edelstahl)', Markersize=2)
plt.title('Temperaturdifferenzen')
plt.legend()
plt.xlabel('t / s')
plt.ylabel('ΔT / °C')
plt.savefig('Differenzen.pdf')
