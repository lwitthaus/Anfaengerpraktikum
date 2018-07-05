import matplotlib.pyplot as plt
import numpy as np
from scipy.constants import mu_0
from scipy.optimize import curve_fit
from uncertainties import ufloat

g, b, B = np.genfromtxt('abbe.txt', unpack=True)
G = 2.8

def f(x, a, b):
   return a * x + b

x_plot = np.linspace(1.2, 2)
params, covariance_matrix = curve_fit(f, 1+1/(B/G) , g)
errors = np.sqrt(np.diag(covariance_matrix))
plt.plot(x_plot, f(x_plot, *params), 'k-', label='Anpassungsfunktion', linewidth=0.5)
print(params)
print(np.sqrt(np.diag(covariance_matrix)))
plt.gcf().subplots_adjust(bottom=0.18)
plt.plot(1+1/(B/G), g, 'r.', label='Messwerte', Markersize=4)
plt.legend()
plt.grid()
plt.xlim((1.28, 2))
plt.ylabel(r'$g`$')
plt.xlabel(r'$1+1/V$')
plt.savefig('build/plot1.pdf')

plt.clf()

print('-------------------------------------------------')
x_plot = np.linspace(2, 4.5)
params, covariance_matrix = curve_fit(f, 1+(B/G) , b)
errors = np.sqrt(np.diag(covariance_matrix))
plt.plot(x_plot, f(x_plot, *params), 'k-', label='Anpassungsfunktion', linewidth=0.5)
print(params)
print(np.sqrt(np.diag(covariance_matrix)))
plt.gcf().subplots_adjust(bottom=0.18)
plt.plot(1+(B/G), b, 'r.', label='Messwerte', Markersize=4)
plt.legend()
plt.grid()
plt.xlim((2, 4.5))
plt.ylabel(r'$b`$')
plt.xlabel(r'$1+V$')
plt.savefig('build/plot3.pdf')
