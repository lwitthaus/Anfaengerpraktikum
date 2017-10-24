import matplotlib.pyplot as plt
import numpy as np


n, T7, T8 = np.genfromtxt('dynamisch200.txt', unpack=True)
plt.plot(n*2,T8, 'b.', label='T8', Markersize=2
plt.plot(n*2,T7, 'r.', label='T7', Markersize=2)
plt.title('Edelstahl')
plt.legend()
plt.xlabel('t / s')
plt.ylabel('T / °C')
plt.savefig('T7_T8_dyn200.pdf')
