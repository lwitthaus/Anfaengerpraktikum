import matplotlib.pyplot as plt
import numpy as np
from scipy.constants import mu_0
from scipy.optimize import curve_fit
from uncertainties import ufloat

U, I = np.genfromtxt('orange.txt', unpack=True)


def f(x, a, b):
   return a * x + b

plt.gcf().subplots_adjust(bottom=0.18)
plt.plot(U, I**(1/2), 'r.', label='Messwerte', Markersize=4)
plt.legend()
plt.grid()
plt.ylabel(r'$\sqrt{I} / \mathrm{\sqrt{nA}}$')
plt.xlabel(r'$U / V$')
plt.savefig('build/plotorange.pdf')

plt.clf()

U, I = np.genfromtxt('orangeint.txt', unpack=True)

x_plot = np.linspace(-1.5, 5)
params, covariance_matrix = curve_fit(f, U, I**(1/2))
errors = np.sqrt(np.diag(covariance_matrix))
plt.plot(x_plot, f(x_plot, *params), 'k-', label='Anpassungsfunktion', linewidth=0.5)
print(params)
print(np.sqrt(np.diag(covariance_matrix)))
plt.gcf().subplots_adjust(bottom=0.18)
plt.plot(U, I**(1/2), 'r.', label='Messwerte', Markersize=4)
plt.legend()
plt.grid()
plt.xlim((-0.5, 5))
plt.ylabel(r'$\sqrt{I} / \mathrm{\sqrt{nA}}$')
plt.xlabel(r'$U / V$')
plt.savefig('build/plotorangeint.pdf')
