import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from uncertainties import ufloat

l = np.array([404.6 ,439.8 ,480.0 ,502.5 ,546.1 ,577.0 ,615.8 ,656.7])
n = np.array([1.813, 1.805, 1.784, 1.781, 1.771, 1.764, 1.760, 1.750])

def f(A, B, l):
   return A + B/(l**2)

x_plot = np.linspace(400, 700)
params, covariance_matrix = curve_fit(f, l, n**2)
errors = np.sqrt(np.diag(covariance_matrix))
plt.plot(x_plot, f(x_plot, *params), 'k-', label='Anpassungsfunktion', linewidth=0.5)
print(params)
print(np.sqrt(np.diag(covariance_matrix)))

plt.gcf().subplots_adjust(bottom=0.18)
plt.plot(l , n**2, 'r.', label='Messwerte', Markersize=4)

plt.legend()
plt.grid()
#plt.xlim((0, 400))
plt.xlabel(r'$\lambda/nm$')
plt.ylabel(r'$n$')
plt.savefig('build/plot.pdf')
