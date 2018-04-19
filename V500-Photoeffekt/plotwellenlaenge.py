import matplotlib.pyplot as plt
import numpy as np
from scipy.constants import mu_0
from scipy.optimize import curve_fit
from uncertainties import ufloat

n, U = np.genfromtxt('wellenlaenge.txt', unpack=True)
c = 299792458 

def f(x, a, b):
   return a * x + b

x_plot = np.linspace(400000, 900000)
params, covariance_matrix = curve_fit(f, c/n, U)
errors = np.sqrt(np.diag(covariance_matrix))
plt.plot(x_plot, f(x_plot, *params), 'k-', label='Anpassungsfunktion', linewidth=0.5)
print(params)
print(np.sqrt(np.diag(covariance_matrix)))
plt.gcf().subplots_adjust(bottom=0.18)
plt.plot(c/n, U, 'r.', label='Messwerte', Markersize=4)
plt.legend()
plt.grid()
#plt.xlim((400000, 900000))
plt.xlabel(r'$\nu / 10**9 \mathrm{Hz}$')
plt.ylabel(r'$U / V$')
plt.savefig('build/plotwellenlaenge.pdf')
