import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from uncertainties import ufloat

r, U = np.genfromtxt('diode.txt', unpack=True)

def f(r, A, B):
   return A*r + B

x_plot = np.linspace(0.1, 4.5, 400)
params, covariance_matrix = curve_fit(f, np.log(r), np.log(U))
errors = np.sqrt(np.diag(covariance_matrix))
plt.plot(x_plot, f(x_plot, *params), 'k-', label='Anpassungsfunktion', linewidth=0.5)
print(params)
print(np.sqrt(np.diag(covariance_matrix)))
plt.gcf().subplots_adjust(bottom=0.18)
plt.plot(np.log(r) , np.log(U), 'r.', label='Messwerte', Markersize=4)
plt.legend()
plt.grid()
plt.xlim((1, 4.5))
plt.xlabel(r'$ln(r)')
plt.ylabel(r'$ln(U)')
plt.savefig('build/plot4.pdf')
