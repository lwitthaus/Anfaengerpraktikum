import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from uncertainties import ufloat

T, f, S, v = np.genfromtxt('profil3000rpm.txt', unpack=True)

#def f(x, c, b):
#   return c * x + b
#
#x_plot = np.linspace(0, 6)
#params, covariance_matrix = curve_fit(f, t, np.log(U))
#errors = np.sqrt(np.diag(covariance_matrix))
#plt.plot(x_plot, f(x_plot, *params), 'k-', label='Anpassungsfunktion', linewidth=0.5)
#print(params)
#print(np.sqrt(np.diag(covariance_matrix)))
#c = ufloat(params[0], errors[0])
#print('c = ', c)
#print(-1/c)
#plt.gcf().subplots_adjust(bottom=0.18)
plt.plot(T , -v, 'r.', label='Messwerte', Markersize=4)
#plt.title('Streuintensität aufgetragen gegen die Tiefe.')
plt.legend()
plt.xlim((9, 20))
#plt.ylim((-1, 14))
plt.grid()
plt.xlabel(r'Tiefe$/\mu s$')
plt.ylabel(r'|v|$/ \mathrm{\frac{m}{s}}$')

plt.savefig('build/plot3.pdf')
