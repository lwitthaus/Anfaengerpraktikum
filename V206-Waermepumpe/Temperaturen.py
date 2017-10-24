import matplotlib.pyplot as plt
import numpy as np

n, T1, T2, pa, pb, p = np.genfromtxt('daten.txt', unpack=True)
plt.plot(n*60,T1, 'r.', label='T1')
plt.plot(n*60,T2, 'b.', label='T2')
plt.title('Temperaturen')
plt.legend()
plt.xlabel('t / s')
plt.ylabel('T / °C')
plt.savefig('build/Temperaturen.pdf')
