import matplotlib.pyplot as plt
import numpy as np
from scipy.constants import mu_0
from scipy.optimize import curve_fit
from uncertainties import ufloat

f, U = np.genfromtxt('spannung.txt', unpack=True)
plt.gcf().subplots_adjust(bottom=0.18)
plt.plot(f, U, 'r.', label='Messwerte $U_B=200$V', Markersize=4)
plt.grid()
#plt.xlim((-0.1, 1.8))
plt.xlabel(r'$f/$kHz')
plt.ylabel(r'$U/$mV')
plt.axhline(222.74, color='black', linestyle=':')
plt.axvline(34.8, color='blue', linestyle=':')
plt.axvline(35.8, color='blue', linestyle=':')
plt.savefig('build/plot.pdf')
