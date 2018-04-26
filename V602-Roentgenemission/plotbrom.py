import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from uncertainties import ufloat

w, U = np.genfromtxt('brom.txt', unpack=True)



x_plot = np.linspace(22, 32)
plt.gcf().subplots_adjust(bottom=0.18)
plt.plot(w, U, 'r.', label='Messwerte', Markersize=4)
plt.legend()
plt.grid()
plt.xlim((22, 32))
plt.ylim((15, 60))
plt.xlabel(r'$\Theta/$Grad')
plt.ylabel(r'I')
plt.savefig('build/plotbrom.pdf')
