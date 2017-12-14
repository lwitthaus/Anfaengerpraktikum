import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from uncertainties import ufloat
import uncertainties.unumpy as unp

f, b, c, a, U, phi = np.genfromtxt('phase.txt', unpack=True)
L = ufloat(10.11*10**(-3), 0.03*10**(-3))
C = ufloat(2.098*10**(-9), 0.006*10**(-9))
R2 = ufloat(509.5, 0.5)

k = np.linspace(4000, 60000, 100)

plt.gcf().subplots_adjust(bottom=0.18)
plt.plot(k, unp.nominal_values(unp.arctan((1-L*C*(2*np.pi*k)**2)/(-k*2*np.pi*R2*C)))+np.pi/2, 'k-', label='Theoriekurve', Markersize=4)
plt.plot(f , phi, 'r.', label='Messwerte', Markersize=4)
plt.title('Phasenverschiebung der Spannungen (halblogarithmisch)')
plt.legend()
plt.xscale('log')
plt.xlabel('$f$ / Hz')
plt.ylabel(r'$\varphi$ / rad')
plt.savefig('build/plot3.pdf')
plt.clf()

plt.gcf().subplots_adjust(bottom=0.18)
plt.plot(k*1e-3, unp.nominal_values(unp.arctan((1-L*C*(2*np.pi*k)**2)/(-k*2*np.pi*R2*C)))+np.pi/2, 'k-', label='Theoriekurve', Markersize=4)
plt.plot(f*1e-3 , phi, 'r.', label='Messwerte', Markersize=4)
plt.title('Phasenverschiebung der Spannungen (linear)')
plt.legend()
plt.grid()
plt.yticks([0, np.pi/4, np.pi/2, (np.pi*3)/4, np.pi], [0, r'$\frac{\pi}{4}$', r'$\frac{\pi}{2}$', r'$\frac{3\pi}{4}$', r'$\pi$'])
plt.xlim((26, 41))
plt.xlabel('$f$ / kHz')
plt.ylabel(r'$\varphi$ / rad')
plt.savefig('build/plot4.pdf')
