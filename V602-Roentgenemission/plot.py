import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from uncertainties import ufloat

w, U = np.genfromtxt('emission.txt', unpack=True)



x_plot = np.linspace(7, 55)
plt.gcf().subplots_adjust(bottom=0.18)
plt.plot(w, U, 'r.', label='Messwerte', Markersize=4)
plt.legend()
plt.grid()
plt.xlim((7, 55))
plt.ylim((30, 5000))
plt.xlabel(r'$2 \cdot \Theta/$Grad')
plt.ylabel(r'I')
plt.savefig('build/plot.pdf')
plt.clf()

w, U = np.genfromtxt('interessant.txt', unpack=True)
plt.gcf().subplots_adjust(bottom=0.18)
plt.plot(w, U, 'r.', label='Messwerte', Markersize=4)
plt.plot(w, U, 'r-', label='Messwerte', linewidth=0.5)
plt.axhline(4278, color='black', linestyle=':')
plt.axhline(155, color='black', linestyle=':')
plt.axhline(1624, color='black', linestyle=':')
plt.axhline(2216.5, color='seagreen', linestyle=':')
plt.axhline(889.5, color='seagreen', linestyle=':')
plt.axvline(44.19, color='blue', linestyle=':')
plt.axvline(45.36, color='blue', linestyle=':')
plt.axvline(39.77, color='purple', linestyle=':')
plt.axvline(40.64, color='purple', linestyle=':')
plt.legend()
plt.grid()
plt.xlabel(r'$\Theta/$Grad')
plt.ylabel(r'I')
plt.savefig('build/plot1.pdf')
