import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from uncertainties import ufloat

t, U = np.genfromtxt('spannung.txt', unpack=True)

def f(t, A, my):
   return A*np.exp(-2*np.pi * my * t *10**(-6))

x_plot = np.linspace(0, 400, 400)
params, covariance_matrix = curve_fit(f, t, U)
errors = np.sqrt(np.diag(covariance_matrix))
plt.plot(x_plot, f(x_plot, *params), 'k-', label='Anpassungsfunktion', linewidth=0.5)
print(params)
print(np.sqrt(np.diag(covariance_matrix)))
print('U_0 gleich ', params[0], ' +- ', errors[0])
print('my gleich ', params[1], ' +-' , errors[1])
plt.gcf().subplots_adjust(bottom=0.18)
plt.plot(t , U, 'r.', label='Messwerte', Markersize=4)
plt.title('Spannungsamplituden und Einhüllende')
plt.legend()
plt.grid()
plt.xlim((0, 400))
plt.xlabel(r'$t/\mathrm{\mu s}$')
plt.ylabel(r'$U/$V')
plt.savefig('build/plot.pdf')
