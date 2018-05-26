import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from uncertainties import ufloat
import uncertainties.unumpy as unp

U, N, I = np.genfromtxt('datenfit.txt', unpack=True)
F = I*60* 10**(-6)/(np.sqrt(N)*1.6*10**(-19))
R = unp.uarray([N],[F])
#H = np.array[0.01, 0.02, 0.02, 0.02, 0.03, 0.03, 0.04, 0.04, 0.04, 0.04, 0.04, 0.05, 0.05, 0.05, 0.05, 0.06, 0.06, 0.06, 0.07, 0.07, 0.07, 0.08, 0.08, 0.08, 0.08, 0.09, 0.09, 0.09, 0.10, 0.10, 0.10]
#0.10, 0.11, 0.11, 0.11, 0.11, 0.11, 0.12, 0.12]

Q = I*60* 10**(-6)/(N*1.6*10**(-19))
K = np.sqrt(Q)

#plt.plot(U, Q, 'b.', label='Messwerte', Markersize=4)
plt.errorbar(U, Q, yerr=K, fmt = 'o',color='r', markersize=2, capsize=2, ecolor='b', elinewidth=0.5, markeredgewidth=0.5)

plt.legend()
plt.grid()
plt.ylabel(r'$Q/e$')
plt.xlabel(r'$U/$V')
plt.savefig('build/rechnung.pdf')
