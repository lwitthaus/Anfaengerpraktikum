import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

w, A, phi = np.genfromtxt('amplitude.txt', unpack=True)

a = np.linspace(0,np.pi/2,200)
plt.polar(phi/360*np.pi, A/3.6, 'rx', label='Messwerte', Markersize=3)
plt.polar(a, np.cos(a), 'k-', label='Theoriekurve', linewidth=1)
plt.title('Polarplot')
plt.legend()
plt.savefig('build/plot3.pdf')
