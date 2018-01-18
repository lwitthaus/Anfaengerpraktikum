import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from uncertainties import ufloat

r, U = np.genfromtxt('diode.txt', unpack=True)

def f(r, A, B):
   return A*1/r**B

x_plot = np.linspace(1, 80, 400)
params, covariance_matrix = curve_fit(f, r, U)
errors = np.sqrt(np.diag(covariance_matrix))
plt.plot(x_plot, f(x_plot, *params), 'k-', label='Anpassungsfunktion', linewidth=0.5)
print(params)
print(np.sqrt(np.diag(covariance_matrix)))
plt.gcf().subplots_adjust(bottom=0.18)
plt.plot(r , U, 'r.', label='Messwerte', Markersize=4)
plt.legend()
plt.grid()
plt.xscale('log')
plt.yscale('log')
plt.xlim((1, 80))
plt.xlabel(r'$r / $cm')
plt.ylabel(r'$U/$mV')
plt.savefig('build/plot3.pdf')
