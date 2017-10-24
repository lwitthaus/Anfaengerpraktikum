import matplotlib.pyplot as plt
import numpy as np


n, T1, T2, T5, T6 = np.genfromtxt('dynamisch80.txt', unpack=True)
plt.plot(n*2,T1, 'b.', label='T1', Markersize=2)
plt.plot(n*2,T2, 'r.', label='T2', Markersize=2)
plt.title('Messing (breit)')
plt.legend()
plt.xlabel('t / s')
plt.ylabel('T / °C')
plt.savefig('T1_T2_dyn80.pdf')

plt.clf()

plt.plot(n*2,T5, 'b.', label='T5', Markersize=2)
plt.plot(n*2,T6, 'r.', label='T6', Markersize=2)
plt.title('Aluminium')
plt.legend()
plt.xlabel('t / s')
plt.ylabel('T / °C')
plt.savefig('T5_T6_dyn80.pdf')
