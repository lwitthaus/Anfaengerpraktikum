import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from uncertainties import ufloat

w, U = np.genfromtxt('zirkonium.txt', unpack=True)



x_plot = np.linspace(15, 24)
plt.gcf().subplots_adjust(bottom=0.18)
plt.plot(w, U, 'r.', label='Messwerte', Markersize=4)
plt.legend()
plt.grid()
plt.xlim((15, 24))
plt.ylim((100, 305))
plt.xlabel(r'$2 \cdot \Theta/$Grad')
plt.ylabel(r'I')
plt.savefig('build/plotzirconium.pdf')
