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
plt.xlabel(r'$Winkel/$Grad')
plt.ylabel(r'Intensität')
plt.savefig('build/plot.pdf')
