import matplotlib.pyplot as plt
import numpy as np
from scipy.constants import mu_0
from scipy.optimize import curve_fit
from uncertainties import ufloat

#p, N, c = np.genfromtxt('abstand1.txt', unpack=True)
R =[24.80, 23.14, 22.60, 21.53, 20.39, 20.12, 18.42, 17.66, 16.59, 15.71, 14.76, 13.68, 12.70, 11.96, 10.88, 9.84, 8.83, 8.44]
N = [81389, 81648, 79218, 78200, 78330, 77252, 76070, 74155, 73737, 72061, 70654, 68438, 65735, 64206, 57280, 49102, 40228, 26130]


#def f(x, a, b):
#   return a * x + b


#x_plot = np.linspace(290, 710)
#params, covariance_matrix = curve_fit(f, U, N/60)
#errors = np.sqrt(np.diag(covariance_matrix))
#plt.plot(x_plot, f(x_plot, *params), 'k-', label='Anpassungsfunktion', linewidth=0.5)
#print(params)
#print(np.sqrt(np.diag(covariance_matrix)))

plt.gcf().subplots_adjust(bottom=0.18)
#plt.plot(U, N, 'r.', label='Messwerte', Markersize=4)
plt.legend()
plt.grid()
#plt.xlim((290, 710))
plt.plot(R, N, 'r.', label='Messwerte', Markersize=4)
#plt.ylim((-1000, 30000))
#plt.ylabel(r'$N / \frac{1}{s}$')
#plt.xlabel(r'$U/$V')
plt.savefig('build/plot2.pdf')
