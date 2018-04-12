import matplotlib.pyplot as plt
import numpy as np
from scipy.constants import mu_0
from scipy.optimize import curve_fit
from uncertainties import ufloat

U, a = np.genfromtxt('kehrwert.txt', unpack=True)

L = 0.143
N = 20
R = 0.282

def f(x, a, b):
   return a * x + b

x_plot = np.linspace(0.002, 0.006)
params, covariance_matrix = curve_fit(f, U, a)
errors = np.sqrt(np.diag(covariance_matrix))
plt.plot(x_plot, f(x_plot, *params), 'k-', label='Anpassungsfunktion', linewidth=0.5)
print(params)
print(np.sqrt(np.diag(covariance_matrix)))
plt.gcf().subplots_adjust(bottom=0.18)
plt.plot(U, a, 'r.', label='Messwerte', Markersize=4)

plt.legend()
plt.grid()
plt.xlim((0.002, 0.0055))
plt.xlabel(r'$\frac{1}{U} / \mathrm{\frac{1}{V}}$')
plt.ylabel(r'$\frac{D}{U_d} / (\mathrm{\frac{mm}{V}})$')
plt.savefig('build/plot12.pdf')
