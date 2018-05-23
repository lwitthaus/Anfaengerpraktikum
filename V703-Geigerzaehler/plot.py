import matplotlib.pyplot as plt
import numpy as np
from scipy.constants import mu_0
from scipy.optimize import curve_fit
from uncertainties import ufloat

U, N, I = np.genfromtxt('daten.txt', unpack=True)
#F =[1.7, 1.4, 1.3, 1.1, 1.0, 0.9, 0.8, 0.7, 0.7, 0.7]

def f(x, a, b):
   return a * x + b



#plt.errorbar(D, np.log(A), yerr= np.log(F), fmt = '.')
plt.gcf().subplots_adjust(bottom=0.18)
plt.plot(U, N, 'r.', label='Messwerte', Markersize=4)
plt.legend()
plt.grid()
plt.xlim((290, 710))
#plt.ylim((-1000, 30000))
plt.ylabel(r'$N$')
plt.xlabel(r'$U/$V')

U, N, I = np.genfromtxt('datenfit.txt', unpack=True)
x_plot = np.linspace(290, 710)
params, covariance_matrix = curve_fit(f, U, N)
errors = np.sqrt(np.diag(covariance_matrix))
plt.plot(x_plot, f(x_plot, *params), 'k-', label='Anpassungsfunktion', linewidth=0.5)
print(params)
print(np.sqrt(np.diag(covariance_matrix)))

plt.savefig('build/plot.pdf')
