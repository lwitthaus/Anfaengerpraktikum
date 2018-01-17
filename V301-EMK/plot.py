import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from uncertainties import ufloat

I, U = np.genfromtxt('spannung1.txt', unpack=True)

def f(I, a, b):
   return a*I + b

x_plot = np.linspace(0, 100, 400)
params, covariance_matrix = curve_fit(f, I, U)
errors = np.sqrt(np.diag(covariance_matrix))
plt.plot(x_plot, f(x_plot, *params), 'k-', label='Anpassungsfunktion', linewidth=0.5)
print(params)
print(np.sqrt(np.diag(covariance_matrix)))
plt.gcf().subplots_adjust(bottom=0.18)
plt.plot(I , U, 'r.', label='Messwerte', Markersize=4)
plt.legend()
plt.grid()
plt.xlim((0, 90))
plt.xlabel(r'$I/\mathrm{mA}$')
plt.ylabel(r'$U/$V')
plt.savefig('build/plot.pdf')
