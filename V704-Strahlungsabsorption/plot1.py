import matplotlib.pyplot as plt
import numpy as np
from scipy.constants import mu_0
from scipy.optimize import curve_fit
from uncertainties import ufloat

D, A = np.genfromtxt('betazahlen.txt', unpack=True)
F =[0.7, 0.3, 0.3, 0.2, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]

def f(x, a, b):
   return a * x + b



plt.errorbar(D*10**(-6)*2700, np.log(A), yerr=[np.log(A+F)-np.log(A), np.log(A)-np.log(A-F)], fmt = 'o',color='r', markersize=2, capsize=2, ecolor='b', elinewidth=0.5, markeredgewidth=0.5)
plt.gcf().subplots_adjust(bottom=0.18)
plt.plot(D*10**(-6)*2700, np.log(A), 'r.', label='Messwerte', Markersize=4)
plt.grid()
plt.xlim((0.2, 1.4))
plt.ylabel(r'$\ln{A/A_0}$ ')
plt.xlabel(r'$R/\frac{kg}{m^3}$')

D, A = np.genfromtxt('betazahlen1.txt', unpack=True)
x_plot = np.linspace(0.2, 1.4)
params, covariance_matrix = curve_fit(f, D*10**(-6)*2700, np.log(A))
errors = np.sqrt(np.diag(covariance_matrix))
plt.plot(x_plot, f(x_plot, *params), 'k-', label='Anpassungsfunktion 1', linewidth=0.5)
print(params)
print(np.sqrt(np.diag(covariance_matrix)))

D, A = np.genfromtxt('betazahlen2.txt', unpack=True)
params, covariance_matrix = curve_fit(f, D*10**(-6)*2700, np.log(A))
errors = np.sqrt(np.diag(covariance_matrix))
plt.plot(x_plot, f(x_plot, *params), 'g-', label='Anpassungsfunktion 2', linewidth=0.5)
print(params)
print(np.sqrt(np.diag(covariance_matrix)))
plt.legend(loc='lower left')

plt.savefig('build/plot1.pdf')
