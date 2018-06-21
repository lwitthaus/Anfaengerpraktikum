import matplotlib.pyplot as plt
import numpy as np
from scipy.constants import mu_0
from scipy.optimize import curve_fit
from uncertainties import ufloat

#p, N, c = np.genfromtxt('abstand1.txt', unpack=True)
x =[0, 0.11, 0.23, 0.34, 0.45, 0.57, 0.68, 0.79, 0.91, 1.02, 1.14, 1.25, 1.36, 1.48, 1.59, 1.70, 1.82, 1.93, 2.04, 2.16, 2.27]
N = np.array([81389, 81648, 79218, 78200, 78330, 77252, 76070, 74155, 73737, 72061, 70654, 68438, 65735, 64206, 57280, 49102, 40228, 26130, 17869, 9083, 3592])


y =[1.70, 1.82, 1.93, 2.04]
M = np.array([49102, 40228, 26130, 17869])

def f(y, a, b):
   return a * y + b


x_plot = np.linspace(0, 2.3)
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
plt.ylim((0, 85000))
plt.ylabel(r'$N$')
plt.xlabel(r'$x/$cm')
plt.savefig('build/plot2.pdf')
