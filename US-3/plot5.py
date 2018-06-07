import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from uncertainties import ufloat

a, f = np.genfromtxt('rip.txt', unpack=True)

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
plt.plot((f*1800)/(4*(10**6)*np.cos(a*np.pi/180)) , f/np.cos(a*np.pi/180), 'r.', label='Messwerte', Markersize=4)
plt.legend()
#plt.xlim((9, 20))
#plt.ylim((3, 14))
plt.grid()
plt.xlabel(r'Geschwindigkeit $/ m/s$')
plt.ylabel(r'$\frac{\nu}{cos(\alpha)} / Hz$')
plt.savefig('build/plot5.pdf')
