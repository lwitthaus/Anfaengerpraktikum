import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

n, U = np.genfromtxt('saegezahn.txt', unpack=True)

def f(x, c, b):
   return c * x + b

x_plot = np.linspace(0,3)
params, covariance_matrix = curve_fit(f, n, np.log(U))
plt.plot(x_plot, f(x_plot, *params), 'k-', label='Anpassungsfunktion', linewidth=0.5)
print(params)
print(np.sqrt(np.diag(covariance_matrix)))
plt.gcf().subplots_adjust(bottom=0.18)
plt.plot(n , np.log(U), 'r.', label='Messwerte', Markersize=4)
plt.title('Lineare Regression der Sägezahnschwingung')
plt.legend()
plt.grid()
plt.xlabel(r'$\ln{(n)}$')
plt.ylabel(r'$\ln { \left( \frac{U_n}{U_1} \right)}$')
#plt.xscale('log')
#plt.yscale('log')
plt.tight_layout()
plt.savefig('build/plot2.pdf')
