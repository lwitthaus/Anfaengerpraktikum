import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from uncertainties import ufloat

E, Z = np.genfromtxt('moseley.txt', unpack=True)


def f(x, a, b):
   return a * x + b

x_plot = np.linspace(34, 42)
params, covariance_matrix = curve_fit(f, Z, np.sqrt(E))
errors = np.sqrt(np.diag(covariance_matrix))
plt.plot(x_plot, f(x_plot, *params), 'k-', label='Anpassungsfunktion', linewidth=0.5)
print(params)
print(np.sqrt(np.diag(covariance_matrix)))
x_plot = np.linspace(34, 42)
plt.gcf().subplots_adjust(bottom=0.18)
plt.plot(Z, np.sqrt(E), 'r.', label='Messwerte', Markersize=4)
plt.legend()
plt.grid()
plt.ylim((3.5, 4.5))
plt.xlim((34, 42))
plt.xlabel(r'$Z$')
plt.ylabel(r'$\sqrt{E_k}/\mathrm{\sqrt{keV}}')
plt.savefig('build/plotmoseley.pdf')
