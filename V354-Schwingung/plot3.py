import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from uncertainties import ufloat
import uncertainties.unumpy as unp

f, b, c, a, U, phi = np.genfromtxt('phase.txt', unpack=True)
L = ufloat(10.11*10**(-3), 0.03*10**(-3))
C = ufloat(2.098*10**(-9), 0.006*10**(-9))
R2 = ufloat(559.5, 0.5)
q = ufloat(3.99, 0.01)
k = np.linspace(4000, 60000, 100)

print(unp.sqrt(1/(L*C)-R2**2/(2*L**2))/(2*np.pi))
print(34000/(unp.sqrt(1/(L*C)-R2**2/(2*L**2))/(2*np.pi)))
print('------------')
print(1/(unp.sqrt(L*C)*q*2*np.pi))
print(7500/(1/(unp.sqrt(L*C)*q*2*np.pi)))

plt.gcf().subplots_adjust(bottom=0.18)
plt.plot(k, unp.nominal_values(unp.arctan((1-L*C*(2*np.pi*k)**2)/(-k*2*np.pi*R2*C)))+np.pi/2, 'k-', label='Theoriekurve', linewidth=0.5)
plt.plot(f , phi, 'r.', label='Messwerte', Markersize=4)
plt.yticks([0, np.pi/4, np.pi/2, (np.pi*3)/4, np.pi], [0, r'$\frac{\pi}{4}$', r'$\frac{\pi}{2}$', r'$\frac{3\pi}{4}$', r'$\pi$'])
plt.title('Phasenverschiebung der Spannungen (halblogarithmisch)')
plt.legend()
plt.xscale('log')
plt.xlabel('$f$ / Hz')
plt.ylabel(r'$\varphi$ / rad')
plt.savefig('build/plot3.pdf')
plt.clf()

plt.gcf().subplots_adjust(bottom=0.18)
plt.plot(k*1e-3, unp.nominal_values(unp.arctan((1-L*C*(2*np.pi*k)**2)/(-k*2*np.pi*R2*C)))+np.pi/2, 'k-', label='Theoriekurve', linewidth=0.5)
plt.plot(f*1e-3 , phi, 'r.', label='Messwerte', Markersize=4)
plt.title('Phasenverschiebung der Spannungen (linear)')
plt.legend()
plt.axhline(np.pi/2, color='blue', linestyle=':')
plt.axhline(np.pi/4, color='black', linestyle=':')
plt.axhline((3*np.pi)/4, color='black', linestyle=':')
plt.grid()
plt.yticks([0, np.pi/4, np.pi/2, (np.pi*3)/4, np.pi], [0, r'$\frac{\pi}{4}$', r'$\frac{\pi}{2}$', r'$\frac{3\pi}{4}$', r'$\pi$'])
plt.xlim((26, 41))
plt.xlabel('$f$ / kHz')
plt.ylabel(r'$\varphi$ / rad')
plt.savefig('build/plot4.pdf')
