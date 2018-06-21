import matplotlib.pyplot as plt
import numpy as np
from scipy.constants import mu_0
from scipy.optimize import curve_fit
from uncertainties import ufloat

#p, N, c = np.genfromtxt('abstand1.txt', unpack=True)
R =[24.80, 23.97, 23.33, 22.60, 21.97, 20.56, 19.18, 18.08, 17.17, 16.59, 15.79, 15.23, 14.52, 13.75, 13.60, 12.55, 11.82, 11.03, 10.46, 9.77, 9.50]
N= [133097, 132258, 132252, 131151, 129489, 127602, 124606, 119948, 117771, 115922, 115965, 114158, 112766, 110443, 109593, 106939, 102803, 98282, 94237, 89703, 85338]



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
plt.savefig('build/plot3.pdf')
