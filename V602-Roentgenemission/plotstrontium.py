import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from uncertainties import ufloat

w, U = np.genfromtxt('stronzium.txt', unpack=True)



x_plot = np.linspace(17, 25)
plt.gcf().subplots_adjust(bottom=0.18)
plt.plot(w, U, 'r.', label='Messwerte', Markersize=4)
plt.legend()
plt.grid()
plt.xlim((17, 25))
plt.ylim((40, 205))
plt.xlabel(r'$\Theta/$Grad')
plt.ylabel(r'I')
plt.savefig('build/plotstrontium.pdf')
