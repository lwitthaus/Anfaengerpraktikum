import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['figure.figsize'] = (10, 8)
plt.rcParams['font.size'] = 16
from scipy.optimize import curve_fit
from uncertainties import correlated_values, correlation_matrix
import scipy.constants as const
from uncertainties import ufloat
import uncertainties.unumpy as unp


x, I = np.genfromtxt('doppelspalt2.txt', unpack=True)

p = x / 1010     # x / L
I = I * 1000
l = 635 * 10**(-9)

#np.savetxt('doppelspalt3.txt', np.column_stack([p]), header="phi")
plt.plot(p, I, 'kx', label='Messwerte')


def f(x, a, s, b, d, c):
    return a * ((np.cos((np.pi * s * np.sin(x - d))/(635 * 10**(-9))))**2) * (((635 * 10**(-9))/(np.pi * b * np.sin(x - d)))**2) * ((np.sin((np.pi * b * np.sin(x - d))/(635 * 10**(-9))))**2) 


t = np.linspace(min(p), max(p), 1000)
# plt.plot(t, f(t, (6*10**3), (0.25*10**(-3)), (0.15*10**(-3)), 1, - 0.0002), 'r-')
params, cov = curve_fit(f, p, I, p0=((5*10**3), (0.4*10**(-3)), (0.15*10**(-3)), (22)))  # Gib hier die auf den Geräten stehenden Werte ein
err = np.sqrt(np.diag(cov))
print('A0^2 =', params[0], '+/-', err[0])
print('s =', params[1], '+/-', err[1])
print('b =', params[2], '+/-', err[2])
# print('c =', params[3], '+/-', err[3])
print('d/Verschiebung =', params[3], '+/-', err[3])
#
plt.plot(t, f(t, *params), 'r-', label='Ausgleichskurve')
plt.xlabel(r'$\varphi$ / rad')
# plt.ylabel(r'$\sqrt{E_K}$ / $\sqrt{keV}$')
plt.ylabel('Strom proportional zur Intensität / nA')
# plt.xlim(-0.1, 2.1)
# plt.ylim(26000, 95000)
plt.legend(loc='best')
plt.grid()
plt.tight_layout()
plt.savefig('doppel.pdf')
plt.show()
