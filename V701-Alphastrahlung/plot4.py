import matplotlib.pyplot as plt
import numpy as np
from scipy.constants import mu_0
from scipy.optimize import curve_fit
from uncertainties import ufloat

x, E = np.genfromtxt('Energie.txt', unpack=True)

def f(x, a, b):
   return a * x + b


x_plot = np.linspace(-0.1,2)
params, covariance_matrix = curve_fit(f, x, E)
errors = np.sqrt(np.diag(covariance_matrix))
plt.plot(x_plot, f(x_plot, *params), 'k-', label='Anpassungsfunktion', linewidth=0.5)
print(params)
print(np.sqrt(np.diag(covariance_matrix)))

plt.plot(x, E, 'r.', label='Messwerte', Markersize=4)
plt.gcf().subplots_adjust(bottom=0.18)
plt.legend()
plt.grid()
plt.xlim((-0.1,2))
plt.ylabel(r'$E/$MeV')
plt.xlabel(r'$x/$cm')
plt.savefig('build/plot4.pdf')
