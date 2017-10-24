import matplotlib.pyplot as plt
import numpy as np


n, T1, T2, T3, T4, T5, T6, T7, T8 = np.genfromtxt('statisch.txt', unpack=True)
plt.plot(n*5,T1, 'r.', label='Messing (breit)', Markersize=2)
plt.plot(n*5,T4, 'b.', label='Messing (schmal)', Markersize=2)
plt.title('Temperaturen Messing')
plt.legend()
plt.xlabel('t / s')
plt.ylabel('T / °C')
plt.savefig('T1_T4.pdf')

plt.clf()

plt.plot(n*5,T5, 'r.', label='Aluminium', Markersize=2)
plt.plot(n*5,T8, 'b.', label='Edelstahl', Markersize=2)
plt.title('Temperaturen Aluminium und Edelstahl')
plt.legend()
plt.xlabel('t / s')
plt.ylabel('T / °C')
plt.savefig('T5_T8.pdf')
