import matplotlib.pyplot as plt
import numpy as np
from scipy.constants import mu_0
from scipy.optimize import curve_fit
from uncertainties import ufloat

D, A = np.genfromtxt('gammazahlen.txt', unpack=True)
#F =[1.7,]

def f(x, a, b):
   return a * x + b


x_plot = np.linspace(1, 21)
params, covariance_matrix = curve_fit(f, D, np.log(A))
errors = np.sqrt(np.diag(covariance_matrix))
plt.plot(x_plot, f(x_plot, *params), 'k-', label='Anpassungsfunktion', linewidth=0.5)
print(params)
print(np.sqrt(np.diag(covariance_matrix)))
#errA = np.sqrt(A)
plt.errorbar(D, np.log(A), yerr= np.log(A), fmt = '.')
plt.gcf().subplots_adjust(bottom=0.18)
plt.plot(D, np.log(A), 'r.', label='Messwerte', Markersize=4)
plt.legend()
plt.grid()
plt.xlim((1, 21))
#plt.ylim((2, 20))
plt.ylabel(r'$A/$s')
plt.xlabel(r'$D/$mm')
plt.savefig('build/plot.pdf')
