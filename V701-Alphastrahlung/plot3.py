import matplotlib.pyplot as plt
import numpy as np
from scipy.constants import mu_0
from scipy.optimize import curve_fit
from uncertainties import ufloat

#p, N, c = np.genfromtxt('abstand1.txt', unpack=True)
x =[0, 0.08, 0.17, 0.25, 0.34, 0.42, 0.50, 0.59, 0.67, 0.76, 0.84, 0.92, 1.01, 1.09, 1.17, 1.26, 1.34, 1.43, 1.51, 1.59, 1.68]
N= np.array([133097, 132258, 132252, 131151, 129489, 127602, 124606, 119948, 117771, 115922, 115965, 114158, 112766, 110443, 109593, 106939, 102803, 98282, 94237, 89703, 85338])

y = [1.26, 1.34, 1.43, 1.51, 1.59, 1.68]
M = np.array([106939, 102803, 98282, 94237, 89703, 85338])

def f(y, a, b):
   return a * y + b


x_plot = np.linspace(0, 1.8)
params, covariance_matrix = curve_fit(f, y, M)
errors = np.sqrt(np.diag(covariance_matrix))
plt.plot(x_plot, f(x_plot, *params), 'k-', label='Anpassungsfunktion', linewidth=0.5)
print(params)
print(np.sqrt(np.diag(covariance_matrix)))

plt.gcf().subplots_adjust(bottom=0.18)
#plt.plot(U, N, 'r.', label='Messwerte', Markersize=4)
plt.legend()
plt.grid()
#plt.xlim((290, 710))
plt.plot(x, N, 'r.', label='Messwerte', Markersize=4)
plt.ylim((80000, 140000))
plt.xlim((-0.01, 1.8))
plt.ylabel(r'$N$')
plt.xlabel(r'$x/$cm')
plt.savefig('build/plot3.pdf')
